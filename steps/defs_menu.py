from time import sleep

from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@step('open eBay.com website')
def open_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get("https://www.eBay.com/")


@step('type "{something}" to search string and click search button')
def search_tv(context, something):
    search_string = context.driver.find_element(by=By.XPATH,
                                                value="//input[@aria-label='Search for anything' and "
                                                      "@class='gh-tb ui-autocomplete-input']")
    search_string.send_keys(f"{something}")
    search_button = context.driver.find_element(by=By.XPATH,
                                                value="//input[@id='gh-btn' and @value='Search']")
    search_button.click()
    sleep(2)


@step('choose "{category}" and "{subcategory}" in left menu')
def choose_left_menu(context, category, subcategory):
    menu_item = context.driver.find_element(by=By.XPATH,
                                            value=f"//li[@class='x-refine__main__list '][.//h3[text()='{category}']]"
                                                  f"//span[text()='{subcategory}']")
    menu_item.click()
    sleep(5)


@step('verify item is "{param}"')
def verify_item(context, param):
    current_item = context.driver.find_element(by=By.XPATH,
                                               value=f"//div[@class='s-item__info clearfix'][.//*[contains(text(), '{param}')]]")
    assert current_item
    sleep(2)


@step('verify filter is applied "{param}"')
def verify_applied_param(context, param):
    applied_param = context.driver.find_element(by=By.XPATH,
                                                value=f"//ul[@class='carousel__list']"
                                                      f"//div[text()='{param}']")
    assert applied_param
    sleep(2)


@step('choose with category "{category}" from {minimum} to {maximum}')
def by_price(context, category, minimum, maximum):
    price_min = context.driver.find_element(by=By.XPATH,
                                            value=f"//li[@class='x-refine__main__list '][.//h3[text()='{category}']]"
                                                  f"//input[@aria-label='Minimum Value in $']")
    price_min.send_keys(f"{minimum}")
    price_max = context.driver.find_element(by=By.XPATH,
                                            value=f"//li[@class='x-refine__main__list '][.//h3[text()='{category}']]"
                                                  f"//input[@aria-label='Maximum Value in $']")
    price_max.send_keys(f"{maximum}")
    button_apply = context.driver.find_element(by=By.XPATH,
                                               value=f"//li[@class='x-refine__main__list '][.//h3[text()='{category}']]"
                                                     f"//button[@aria-label='Submit price range']")
    button_apply.click()
    sleep(2)


@step('verify price between {min_price} and {max_price}')
def verify_price(context, min_price, max_price):
    price = context.driver.find_element(by=By.XPATH,
                                        value=f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']"
                                              f"//div[@class='s-item__info clearfix']"
                                              f"//span[contains(text(), '$')][@class='s-item__price']")
    current_price = price.text.strip('$')
    assert float(min_price) <= float(current_price) <= float(max_price)
