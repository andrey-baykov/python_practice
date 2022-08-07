from time import sleep

from behave import step
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@step('open eBay.com')
def open_browser(context):
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.eBay.com/")


@step('search for "Sony XR77A80J" TV')
def search_tv(context):
    search_string = context.driver.find_element(by=By.XPATH,
                                                value="//input[@aria-label='Search for anything' and "
                                                      "@class='gh-tb ui-autocomplete-input']")
    search_string.send_keys("Sony XR77A80J")


@step('click the "search" button')
def click_search_button(context):
    search_button = context.driver.find_element(by=By.XPATH,
                                                value="//input[@id='gh-btn' and @value='Search']")
    search_button.click()
    sleep(2)


@step('click first available item from results list')
def click_first_result(context):
    first_result = context.driver.find_element(by=By.XPATH,
                                               value="//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']//a[@class='s-item__link']")
    first_result.click()
    sleep(5)


@step('click "Add to the cart"')
def add_to_cart(context):
    button_add_to_cart = context.driver.find_element(by=By.XPATH,
                                                     value="//a[@id='atcRedesignId_btn' and contains(text(), 'to cart')]")
    button_add_to_cart.click()
    sleep(3)


@step('click Daily Deals')
def click_daily_deals(context):
    daily_deals_link = context.driver.find_element(by=By.XPATH,
                                                   value="//a[@class='gh-p' and contains(text(), 'Deals')]")
    daily_deals_link.click()
    sleep(3)


@step('click SPOTLIGHT DEAL')
def validate_page_dd(context):
    first_item = context.driver.find_element(by=By.XPATH,
                                             value="//span[@class='ebayui-ellipsis-3']")
    first_item.click()
    sleep(3)


@step('click "Go to cart"')
def click_go_to_cart(context):
    btn_go_to_cart = context.driver.find_element(by=By.XPATH,
                                                 value="//div[@role='document']//span[text()='Go to cart']")
    btn_go_to_cart.click()
    sleep(3)
