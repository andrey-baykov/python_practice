from time import sleep

from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@step('open eBay website')
def open_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get("https://www.eBay.com/")


@step('click "{shop_by}" then choose category "{cat}"')
def choose_cat(context, shop_by, cat):
    cat_list = context.driver.find_element(by=By.XPATH,
                                           value=f"//button[text()='{shop_by}']")
    cat_list.click()
    sleep(1)
    category = context.driver.find_element(by=By.XPATH,
                                           value=f"//div[./h2[text()='Shop by category']]//a[text()='{cat}']")
    category.click()
    sleep(1)


@step('verify page "{title}" was opened')
def verify_page(context, title):
    page = context.driver.find_element(by=By.XPATH,
                                       value=f"//nav[@class='breadcrumbs']//span[text()='{title}']")
    assert page.text == title
