import warnings
from time import sleep

from behave import step
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@step('Open URL "{url}"')
def open_browser(context, url) -> None:
    """ Create instance of driver and run Chrome browser with provided URL

    :param context: self
    :param url: URL to run in a browser
    :return: None
    """
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get(f"https://{url}")
    sleep(2)


@step('Click "{menu_item}" on the top menu')
def click_top_menu_item(context, menu_item) -> None:
    """ Click top menu item provided by parameter

    :param context: self
    :param menu_item: keyword contains in the menu item to click
    :return: None
    """
    top_menu_item_path = f"//a[@class='gh-p' and contains(text(), '{menu_item}')]"
    try:
        top_menu_item = context.driver.find_element(By.XPATH, top_menu_item_path)
        top_menu_item.click()
        sleep(2)
    except NoSuchElementException:
        raise Exception(f'Menu item contains "{menu_item}" not found!')


@step('Click menu item from a table on the top menu and verify opened page')
def click_top_menu_item(context) -> None:
    """ Click top menu item in a loop with data from context.table

    :param context: self
    :return: None
    """
    for num, row in enumerate(context.table.rows, 1):
        menu_item, page_title = row
        top_menu_item_path = f"//a[@class='gh-p' and contains(text(), '{menu_item}')]"
        try:
            top_menu_item = context.driver.find_element(By.XPATH, top_menu_item_path)
            top_menu_item.click()
            sleep(2)
            verify_page_by_title(context, page_title)
            print(num, menu_item, "- Done!")
        except NoSuchElementException:
            raise Exception(f'Menu item contains "{menu_item}" not found!')


@step('Verify page "{page_title}" was opened')
def verify_page_by_title(context, page_title) -> None:
    """ Verify page by header title

    :param context: self
    :param page_title: page title to verify
    :return: Exception if Failed, None if Pass
    """
    path_found = True
    try:
        title_path = f"//div[@class='navigation-desktop']//a[text()='{page_title}']"
        context.driver.find_element(By.XPATH, title_path)
    except NoSuchElementException:
        path_found = False
    if not path_found:
        try:
            title_path = f"//h1[@class='b-pageheader']//*[text()='{page_title}']"
            context.driver.find_element(By.XPATH, title_path)
            path_found = True
        except NoSuchElementException:
            path_found = False
    if not path_found:
        try:
            title_path = f"//div[@class='title-banner__layer']//*[text()='{page_title}']"
            context.driver.find_element(By.XPATH, title_path)
            path_found = True
        except NoSuchElementException:
            path_found = False

    assert path_found, f'Page with title "{page_title}" not found'


@step('Click flying out menu "Shop by category" and verify correct page was opened')
def flying_out_menu_test(context) -> None:
    """ Click subcategory from related category and verify correct page was opened by title.
    Data from context.table

    :param context: self
    :return: None
    """
    test_pass = True
    subcategory_item_path = None
    for num, row in enumerate(context.table.rows, 1):
        category, subcategory, page_title = row
        try:
            open_menu_btn_path = f"//button[@id='gh-shop-a']"
            open_menu_btn = context.driver.find_element(By.XPATH, open_menu_btn_path)
            open_menu_btn.click()
            sleep(1)
            subcategory_item_path = f"//td[not(@class)][.//a[text()='{category}']]//a[text()='{subcategory}']"
            subcategory_item = context.driver.find_element(By.XPATH, subcategory_item_path)
            subcategory_item.click()
            sleep(2)

            verify_page_by_title(context, page_title)
            print(f'{num}. "{subcategory}" in "{category}" - Done!')
        except NoSuchElementException:
            warnings.warn(f'Menu item "{subcategory}" in "{category}" not found!')
            print(subcategory_item_path)
            test_pass = False
        except ElementNotInteractableException:
            warnings.warn(f"Path {subcategory_item_path} not found or page title '{page_title}' incorrect.")
            test_pass = False

    assert test_pass, 'Test failed. Read warnings.'


@step('Input "{search_string}" in the search field')
def input_search_string(context, search_string) -> None:
    """Function fill out string to search in to search field

    :param context: self
    :param search_string:  string to insert in to search field
    :return: None
    """
    search_string_field_path = f"//input[@aria-label='Search for anything']"
    search_string_field = context.driver.find_element(By.XPATH, search_string_field_path)
    search_string_field.send_keys(search_string)
    sleep(1)


@step('Click search button')
def click_search_button(context):
    """Click on the search button

    :param context: self
    :return: None
    """
    search_button_path = f"//input[@id='gh-btn' and @value='Search']"
    search_button = context.driver.find_element(By.XPATH, search_button_path)
    search_button.click()
    sleep(2)


@step('Apply left menu with filters from the table')
def apply_left_menu_filter(context):
    """Applies filter from left menu. Filter menu and filter from context.table

    :param context: self
    :return: None
    """
    for row in context.table.rows:
        filter_menu_name, filter_item_name = row
        aria_expanded_path = f"//ul[@class='x-refine__left__nav']//div[./h3[text()='{filter_menu_name}']]"
        aria_expanded = context.driver.find_element(By.XPATH, aria_expanded_path)
        if not aria_expanded.get_attribute("aria-expanded"):
            filter_menu_path = f"//ul[@class='x-refine__left__nav']//h3[text()='{filter_menu_name}']"
            filter_menu = context.driver.find_element(By.XPATH, filter_menu_path)
            filter_menu.click()
            sleep(1)

        filter_item_path = f"//li[@class='x-refine__main__list '][.//h3[text()='{filter_menu_name}']]" \
                           f"//span[text()='{filter_item_name}']"
        filter_item = context.driver.find_element(By.XPATH, filter_item_path)
        filter_item.click()
        sleep(2)


@step('Validate filters was applied and shows above result table')
def validate_filter_above_result_table(context) -> bool:
    """Validate that filters above the results table are present. Filters data in one column
    table.

    :param context: self
    :return: True if Pass, False if Failed
    """
    verify_result = False
    for num, row in enumerate(context.table.rows, 1):
        filter_data = row[0]
        try:
            filter_path = f"//div[@class ='carousel__viewport'][.// ul[@class ='carousel__list']]" \
                          f"// div[text()='{filter_data}']"
            context.driver.find_element(By.XPATH, filter_path)
            verify_result = True
            print(f'{num}. Filter "{filter_data}" - pass.')
        except NoSuchElementException:
            warnings.warn(f'Filter "{filter_data}" not found')
            verify_result = False

    assert verify_result, "Verify filters are failed"


@step('Validate item with parameters from the table')
def validate_item(context):
    test_set = {}
    test_set_pass = []
    for row in context.table.rows:
        apply, parameter, value = row
        if apply == "Yes":
            test_set[parameter] = value
    for test, test_value in test_set.items():
        if test in ("Description contains", "Shipping", "Returns"):
            try:
                element = context.driver.find_element(By.XPATH, get_xpath_type_1(test))
            except NoSuchElementException:
                warnings.warn("Screen type 2")
                element = context.driver.find_element(By.XPATH, get_xpath_type_2(test))
            if test_value in element.text:
                print(f'Test "{test}" with value "{test_value}" in "{element.text}"- pass.')
                test_set_pass.append(True)
            else:
                warnings.warn(f'Test "{test}" with value "{test_value}" in "{element.text}" - fail.')
                test_set_pass.append(False)
        elif "Price" in test:
            try:
                element = context.driver.find_element(By.XPATH, get_xpath_type_1(test))
            except NoSuchElementException:
                warnings.warn("Screen type 2")
                element = context.driver.find_element(By.XPATH, get_xpath_type_2(test))
            web_price = float(element.text[1:].replace(",", ""))
            if 'lower' in test:
                if web_price < float(test_value):
                    print(f'Test "{test}". Web price "{web_price}" lower then "{float(test_value)}" - pass.')
                    test_set_pass.append(True)
                else:
                    warnings.warn(f'Test "{test}". Web price "{web_price}" higher or equal then "{float(test_value)}"'
                                  f' - fail.')
                    test_set_pass.append(False)
            elif 'higher' in test:
                if web_price > float(test_value):
                    print(f'Test "{test}". Web price "{web_price}" higher then "{float(test_value)}" - pass.')
                    test_set_pass.append(True)
                else:
                    warnings.warn(f'Test "{test}". Web price "{web_price}" lower or equal then "{float(test_value)}"'
                                  f' - fail.')
                    test_set_pass.append(False)
            else:
                min_value, max_value = test_value.split()
                if float(min_value) <= web_price <= float(max_value):
                    print(f'Test "{test}". Web price "{web_price}" between "{float(min_value)}" and '
                          f'"{float(max_value)}" - pass.')
                    test_set_pass.append(True)
                else:
                    warnings.warn(f'Test "{test}". Web price "{web_price}" not between "{float(min_value)}" and '
                                  f'"{float(max_value)}" - fail.')
                    test_set_pass.append(False)

    assert all(test_set_pass), "Test set failed. See log."


def get_xpath_type_1(parameter) -> str:
    """Function return XPATH for provided parameter

    :param parameter: parameter for validate
    :return:
    """
    if parameter == "Description contains":
        output = f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']" \
                 f"//h3[@class='s-item__title']"
    elif parameter == "Shipping":
        output = f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']" \
                 f"//*[@class='s-item__shipping s-item__logisticsCost']"
    elif parameter == "Returns":
        output = f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']" \
                 f"//*[@class='s-item__free-returns s-item__freeReturnsNoFee']"
    elif parameter in ("Price lower then", "Price higher then", "Price between"):
        output = f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']" \
                 f"//*[@class='s-item__price']"
    else:
        output = "No xpath for particular parameter."
    return output


def get_xpath_type_2(parameter) -> str:
    """Function return XPATH for provided parameter

    :param parameter: parameter for validate
    :return:
    """
    if parameter == "Description contains":
        output = f"//div[@class='s-item__wrapper clearfix']//h3[contains(@class, 's-item__title')]"
    elif parameter == "Shipping":
        output = f"//div[@class='s-item__wrapper clearfix']" \
                 f"//*[@class='s-item__shipping s-item__logisticsCost']"
    elif parameter == "Returns":
        output = f"//div[@class='s-item__wrapper clearfix']" \
                 f"//*[@class='s-item__free-returns s-item__freeReturnsNoFee']"
    elif parameter in ("Price lower then", "Price higher then", "Price between"):
        output = f"//div[@class='s-item__wrapper clearfix']" \
                 f"//*[@class='s-item__price']"
    else:
        output = "No xpath for particular parameter."
    return output


@step('Click item "{menu_item}" in mosaic menu')
def choose_mosaic_menu(context, menu_item):
    menu_items_list_path = f"//div[@class='b-visualnav__grid']//div[@class='b-visualnav__title']"
    menu_items_list = context.driver.find_elements(By.XPATH, menu_items_list_path)
    for item in menu_items_list:
        if item.text == menu_item:
            item.click()
            break
    sleep(3)


@step('Click item "{menu}" in carousel menu')
def choose_in_carousel_menu(context, menu):
    menu_item_path = f"//div[@class='carousel__viewport carousel__viewport--mask'][./ul[@class='carousel__list']]" \
                     f"//li[.//p[text()='{menu}']]"
    menu_item = context.driver.find_element(By.XPATH, menu_item_path)
    button_right_path = f"//div[./div[@class='carousel__viewport carousel__viewport--mask']" \
                        f"[./ul[@class='carousel__list']][.//li[.//p[text()='{menu}']]]]" \
                        f"//button[@aria-label='Next Slide']"
    button_right = context.driver.find_element(By.XPATH, button_right_path)
    for _ in range(3):
        try:
            menu_item.click()
        except ElementClickInterceptedException:
            button_right.click()
            sleep(3)
            warnings.warn('Next Slide click')
    sleep(3)
