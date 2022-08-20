import warnings
from time import sleep

from behave import step
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
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
    :return: None
    """
    path_found = True
    # title_path = None
    page_to_verify = None
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

    assert test_pass, 'Test failed. Read warnings.'
