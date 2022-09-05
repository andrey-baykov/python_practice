from behave import step
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('Open ebay website')
def open_website(context):
    context.driver.get('https://www.ebay.com/')


@step('Type "{search_item}" in string and press search button')
def search(context, search_item):
    path_search_string = "//input[@id='gh-ac']"

    WebDriverWait(context.driver, 60).until(
        EC.presence_of_element_located((By.XPATH, path_search_string)))
    search_field = context.driver.find_element(By.XPATH, path_search_string)
    search_field.send_keys(search_item)

    path_search_button = "//input[@id='gh-btn']"

    WebDriverWait(context.driver, 60).until(
        EC.presence_of_element_located((By.XPATH, path_search_button)))
    search_button = context.driver.find_element(By.XPATH, path_search_button)
    search_button.click()


@step('Apply filters from the tables')
def filters_apply(context):
    for row in context.table.rows:
        filter_menu_name, filter_item_name = row
        aria_expanded_path = f"//ul[@class='x-refine__left__nav']//div[./h3[text()='{filter_menu_name}']]"
        WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, aria_expanded_path)))
        aria_expanded = context.driver.find_element(By.XPATH, aria_expanded_path)
        if aria_expanded.get_attribute("aria-expanded") == 'false':
            filter_menu_path = f"//ul[@class='x-refine__left__nav']//h3[text()='{filter_menu_name}']"
            filter_menu = context.driver.find_element(By.XPATH, filter_menu_path)
            filter_menu.click()

        filter_item_path = f"//li[@class='x-refine__main__list '][.//h3[text()='{filter_menu_name}']]" \
                           f"//span[text()='{filter_item_name}']"
        WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, filter_item_path)))
        filter_item = context.driver.find_element(By.XPATH, filter_item_path)
        filter_item.click()


@step('Validate results on {number_of_pages} pages')
def validate_results(context, number_of_pages):
    divider_path = "//li[contains(@class, 'REWRITE_START')]"
    # Some results lists have list divider but some haven't
    try:
        context.driver.find_element(By.XPATH, divider_path)
        divider = "[following-sibling::li[contains(@class, 'REWRITE_START')]]"
    except NoSuchElementException:
        divider = ""
    results_list_origin_path = f"//div[@class='srp-river-results clearfix']" \
                               f"//li[./div[@class='s-item__wrapper clearfix']]{divider}"

    current_page_path = "//a[@class='pagination__item' and @aria-current]"
    next_button_path = "//a[@class='pagination__next icon-link']"
    page_to_check = True
    wrong_items = []
    while page_to_check:
        WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, current_page_path)))
        current_page = context.driver.find_element(By.XPATH, current_page_path)

        WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, results_list_origin_path)))
        results_list_origin = context.driver.find_elements(By.XPATH, results_list_origin_path)
        # print(f"page to check: {current_page.text}")
        if not results_list_origin:
            raise Exception(f'No results to validate on page {current_page.text}')

        for result_item in results_list_origin:
            results = []
            title_path = f"descendant::span[@role='heading']"
            title = result_item.find_elements(By.XPATH, title_path)
            subtitle_path = f"descendant::span[@class='SECONDARY_INFO']"
            subtitle = result_item.find_elements(By.XPATH, subtitle_path)
            for filter_item in context.table:
                filter_value = filter_item['filters']
                if filter_value.lower() in title[0].text.lower() or filter_value.lower() in subtitle[0].text.lower():
                    results.append(True)
                else:
                    results.append(False)
            if not all(results):
                wrong_items.append([title[0].text, current_page.text])

        WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, next_button_path)))
        next_button = context.driver.find_element(By.XPATH, next_button_path)
        if int(current_page.text) <= int(number_of_pages) and next_button.get_attribute('aria-disabled') != 'true':
            next_button.click()
        else:
            page_to_check = False

    if wrong_items:
        for num, item in enumerate(wrong_items, 1):
            print(f"{num}. Item '{item[0]}' on page: {item[1]}")
        raise Exception('Validate is failed.')
