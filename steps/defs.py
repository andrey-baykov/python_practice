from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('Open {url} website')
def open_url(context, url):
    context.driver.get(url)
    context.list_validate = []
    context.page_validate = []


@step('Search {item} tires')
def search_item(context, item):
    path = "//input[@id='gh-ac']"
    search_string = WebDriverWait(context.driver, 60).until(EC.presence_of_element_located((By.XPATH, path)))
    search_string.send_keys(item)

    path = "//input[@id='gh-btn']"
    button = WebDriverWait(context.driver, 60).until(EC.presence_of_element_located((By.XPATH, path)))
    button.click()


@step('Apply filters')
def apply_filters(context):
    for cat, fil in context.table.rows:
        expander_path = f"//li[@class='x-refine__main__list '][.//h3[text()='{cat}']]/div[@role='button']"
        expander = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, expander_path)),
                                                           message=f'No such category: {cat}')
        if expander.get_attribute('aria-expanded') == 'false':
            expander.click()
        filters_path = f"//li[@class='x-refine__main__list '][.//*[text()='{cat}']]" \
                       f"/div[@class='x-refine__group']//span[text()='{fil}']"
        filters = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, filters_path)),
                                                          message=f'No such parameter: {fil} in category: {cat}')
        filters.click()
    sleep(1)


@step('Validate all listing results by parameters')
def validate_lists(context):
    results_path = "//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']" \
                   "/div[@class='s-item__wrapper clearfix']"
    results = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, results_path)),
                                                      message=f'No results on page')
    page_bad_results = []
    for result_item in results:
        result_title = result_item.find_element(By.XPATH, "descendant::span[@role='heading']")
        for param in context.table.rows:
            if param[0].lower() not in result_title.text.lower():
                page_bad_results.append([param[0], result_title.text])
    context.list_validate = page_bad_results


@step('Validate all results on each result page')
def validate_on_page(context):
    all_items_path = "//ul[@class='srp-results srp-list clearfix']//li[.//div[@class='s-item__wrapper clearfix']]"
    all_items = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, all_items_path)),
                                                        message="No items found on the page.")
    errors = []
    elements = []
    for item in all_items:
        title = item.find_elements(By.XPATH, "descendant::span[@role='heading']")
        link = item.find_elements(By.XPATH, "descendant::a[@class='s-item__link']")

        if not title or not link:
            errors.append('No title or link for item')
            continue

        elements.append((title[0].text, link[0].get_attribute('href')))

    results_window = context.driver.current_window_handle

    for title, link in elements:
        context.driver.execute_script(f"window.open('{link}')")
        context.driver.switch_to.window(context.driver.window_handles[-1])

        labels_path = "//div[@data-testid='ux-layout-section-module'][.//span[text()='Item specifics']]//div[@class='ux-labels-values__labels']//span[text()]"
        values_path = "//div[@data-testid='ux-layout-section-module'][.//span[text()='Item specifics']]//div[@class='ux-labels-values__values']//span[text()]"
        labels = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, labels_path)))
        values = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, values_path)))

        labels = [label.text for label in labels]
        values = [value.text for value in values]

        item_specifics = dict(zip(labels, values))
        err_desc = {}
        for param, val in context.table.rows:
            if item_specifics[param].lower() != val.lower():
                err_desc[param] = val
        if err_desc:
            errors.append(f"Item {title} not related to search. Parameters: {err_desc}. Link: {link} ")

        context.driver.close()
        context.driver.switch_to.window(results_window)

    context.page_validate = errors


@step('Print tests results')
def print_results(context):
    print("Listing results failed:")
    print(*context.list_validate, sep='\n')
    print()
    print("Page errors: ")
    print(*context.page_validate, sep='\n')

    assert not context.list_validate and not context.page_validate, "Test failed. See results"
