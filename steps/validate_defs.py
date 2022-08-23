import warnings
from time import sleep

from behave import step
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@step('Open a home page on the eBay website')
def open_browser(context) -> None:
    """
    Function create an instance of browser with URL 'https://www.eBay.com/'
    :param context: driver
    :return: None
    """
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
    search_string_path = "//input[@aria-label='Search for anything']"
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
    button_search_path = "//input[@id='gh-btn'][@value='Search']"
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
        sleep(2)


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
    print(results_list_origin_path)
    print(results_list_filtered_path)
    print(result_o)
    sleep(5)
    assert result_o == result_f, f"Validate is failed. Filtered results {result_f} items are not equal {result_o} " \
                                 f"items of original results."
