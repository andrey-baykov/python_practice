from time import sleep

from behave import step
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@step('Set regular or incognito mode for browser: {mode}')
def set_browser_mode(context, mode) -> None:
    """
    Set browser to regular or incognito mode for all scenarios.
    :param context: mode
    :param mode: regular - open browser in regular, incognito - open browser in incognito mode.
    :return: None
    """
    if mode in ('regular', 'incognito'):
        context.browser_mode = mode
    else:
        raise Exception('Incorrect browser mode. Allow only regular or incognito mode.')


@step('Open a home page on the eBay website')
def open_browser(context) -> None:
    """
    Function create an instance of browser with URL 'https://www.eBay.com/'\n
    :param context: driver, browser_mode
    :return: None
    """
    if context.browser_mode == 'incognito':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                          chrome_options=chrome_options)
    else:
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    context.driver.get("https://www.eBay.com/")


@step('Type "{string_to_search}" in the search string')
def type_string_to_search(context, string_to_search) -> None:
    """
    Function input value of parameter 'string_to_search' into search string.
    :param context: driver
    :param string_to_search: string to search
    :return: None
    """
    # Home page and advanced search page have different paths to search field
    try:
        search_string_path = "//input[@aria-label='Search for anything']"
        search_string = context.driver.find_element(By.XPATH, search_string_path)
    except NoSuchElementException:
        search_string_path = "//fieldset[./legend[text()='Enter keywords or item number']]" \
                             "//input[@placeholder='Enter keywords or item number']"
        search_string = context.driver.find_element(By.XPATH, search_string_path)

    search_string.send_keys(string_to_search)
    sleep(1)


@step('Click search button')
def click_button_search(context) -> None:
    """
    Function find element 'search button' and click it.
    :param context: driver
    :return: None
    """
    # Home page and advanced search page have different paths to search button
    try:
        button_search_path = "//input[@id='gh-btn'][@value='Search']"
        button_search = context.driver.find_element(By.XPATH, button_search_path)
    except NoSuchElementException:
        button_search_path = "//fieldset[./legend[text()='Enter keywords or item number']]" \
                             "//button[text()='Search']"
        button_search = context.driver.find_element(By.XPATH, button_search_path)

    button_search.click()
    sleep(2)


@step('Apply filters to results')
def apply_filters_from_table(context) -> None:
    """
    Function read filters from table in context and apply it.\n
    Table headers:
    | category | filter | \n
    :param context: driver, table
    :return: None
    """
    for item_row in context.table:
        category = item_row['category']
        category_filter = item_row['filter']

        items_filter_path = f"//li[@class='x-refine__main__list '][.//*[text()='{category}']]" \
                            f"//*[text()='{category_filter}']"
        items_filter = context.driver.find_element(By.XPATH, items_filter_path)
        items_filter.click()
        sleep(5)


@step('Validate that items in the result list matched to filters')
def validate_items_in_result_list(context) -> None:
    """
    Function read parameters from a table in context and validate list with all applied parameters
    equal to original results list. Function check that page has divider 'Results matching fewer words' or not.
    If divider is present function use only results before divider else function use all results to compare\n
    :param context: driver, table
    :return: None
    """
    divider_path = "//li[contains(@class, 'REWRITE_START')]"
    # Some results lists have list divider but some haven't
    try:
        context.driver.find_element(By.XPATH, divider_path)
        divider = "[following-sibling::li[contains(@class, 'REWRITE_START')]]"
    except NoSuchElementException:
        divider = ""
    results_list_origin_path = f"//div[@class='srp-river-results clearfix']" \
                               f"//li[./div[@class='s-item__wrapper clearfix']]{divider}"
    results_list_origin = context.driver.find_elements(By.XPATH, results_list_origin_path)

    results_list_filtered_path = f"//div[@class='srp-river-results clearfix']" \
                                 f"//li[./div[@class='s-item__wrapper clearfix']]{divider}[.//*"
    for filter_item in context.table:
        filter_value = filter_item['filters']
        results_list_filtered_path += f"[contains(text(), '{filter_value}')]"
    results_list_filtered_path += "]"
    results_list_filtered = context.driver.find_elements(By.XPATH, results_list_filtered_path)

    result_o = len(results_list_origin)
    result_f = len(results_list_filtered)
    sleep(5)
    assert result_o == result_f, f"Validate is failed. Filtered results {result_f} items are not equal {result_o} " \
                                 f"items of original results."


@step('Choose in dropdown list "{menu_item}"')
def cats(context, menu_item) -> None:
    """
    Choose an element in the category dropdown list in the search string.
    :param context: driver
    :param menu_item: category in the dropdown list
    :return: None
    """
    dropdown_menu_path = "//select[@id='gh-cat']"
    cat = context.driver.find_element(By.XPATH, dropdown_menu_path)
    cat.click()
    sleep(1)

    menu_cat_path = f"//select[@id='gh-cat']/option[text()='{menu_item}']"
    art_opt = context.driver.find_element(By.XPATH, menu_cat_path)
    art_opt.click()
    sleep(1)


@step('Click "Advanced search" link')
def click_advanced_search_link(context) -> None:
    """
    Click a link "Advanced Search"
    :param context: driver
    :return: None
    """
    adv_search_link_path = "//a[@aria-label='Advanced Search']"
    adv_search_link = context.driver.find_element(By.XPATH, adv_search_link_path)
    adv_search_link.click()
    sleep(2)


@step('Verify "Advanced search" page was opened')
def verify_adv_page(context) -> None:
    """
    Validate current opened page is "Advanced Search"
    :param context: driver
    :return: None
    """
    adv_page_path = "//div[@id='AreaTitle']//*[text()='Advanced Search']"
    adv_page = context.driver.find_element(By.XPATH, adv_page_path)
    assert adv_page.text == 'Advanced Search', "Present page isn't Advanced Search page"


@step('Choose parameters on the page')
def choose_param_adv_page(context) -> None:
    """
    Choose provided in the table parameters for page 'Advanced search'
    :param context: driver, table
    :return: None
    """
    for item in context.table:
        param_path = f"//*[normalize-space() = '{item['parameter']}']"
        param = context.driver.find_element(By.XPATH, param_path)
        param.click()
        sleep(2)
