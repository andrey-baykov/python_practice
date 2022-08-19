import warnings
from time import sleep

from behave import step
from selenium import webdriver
from selenium.common import NoSuchElementException
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
    for row in context.table.rows:
        menu_item = row[0]
        page_title = row[1]
        top_menu_item_path = f"//a[@class='gh-p' and contains(text(), '{menu_item}')]"
        try:
            top_menu_item = context.driver.find_element(By.XPATH, top_menu_item_path)
            top_menu_item.click()
            sleep(2)
            verify_page_by_title(context, page_title)
            print(page_title)
        except NoSuchElementException:
            raise Exception(f'Menu item contains "{menu_item}" not found!')


@step('Verify page "{page_title}" was opened')
def verify_page_by_title(context, page_title) -> None:
    """

    :param context: self
    :param page_title: page title to verify
    :return: None
    """
    try:
        title_path = f"//div[@class='navigation-desktop']//a[text()='{page_title}']"
        page_to_verify = context.driver.find_element(By.XPATH, title_path)
        warnings.warn('First type of page')
    except NoSuchElementException:
        title_path = f"//h1[@class='b-pageheader']//*[text()='{page_title}']"
        page_to_verify = context.driver.find_element(By.XPATH, title_path)
        warnings.warn('Second type of page')
    assert page_to_verify, f'Page with title "{page_title}" not found'
