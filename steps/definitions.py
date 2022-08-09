from time import sleep

from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@step('open eBay.com')
def open_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
    # Close tool tip window because it covered main element and result cannot be clicked
    try:
        tool_tip = context.driver.find_element(by=By.XPATH,
                                               value="//button[@class='srp-save-search__tooltip-close']")
        tool_tip.click()
    except Exception as e:
        print(e)

    sleep(3)

    first_result = context.driver.find_element(by=By.XPATH,
                                               value="//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']"
                                                     "//div[@class='s-item__image-wrapper']/img")
    first_result.click()
    sleep(5)


@step('click "Add to the cart"')
def add_to_cart(context):
    if len(context.driver.window_handles) == 2:
        context.driver.switch_to.window(context.driver.window_handles[1])
    else:
        context.driver.switch_to.window(context.driver.window_handles[0])
    button_add_to_cart = context.driver.find_element(by=By.XPATH,
                                                     value="//a[@id='atcRedesignId_btn' and contains(text(), 'to cart')]")
    button_add_to_cart.click()
    sleep(2)


@step('Make sure you\'ve been navigated to Daily Deals')
def validate_page(context):
    page_title = context.driver.find_element(by=By.XPATH,
                                             value="//div[@class='navigation-desktop']/h1/a[text()='Deals']")
    assert page_title.text == 'Deals'


@step('click Daily Deals')
def click_daily_deals(context):
    daily_deals_link = context.driver.find_element(by=By.XPATH,
                                                   value="//a[@class='gh-p' and contains(text(), 'Deals')]")
    daily_deals_link.click()
    sleep(2)


@step('click SPOTLIGHT DEAL')
def validate_page_dd(context):
    first_item = context.driver.find_element(by=By.XPATH,
                                             value="//span[@class='ebayui-ellipsis-3']")
    first_item.click()
    sleep(2)


@step('click "Go to cart"')
def click_go_to_cart(context):
    btn_go_to_cart = context.driver.find_element(by=By.XPATH,
                                                 value="//div[@role='document']//span[text()='Go to cart']")
    btn_go_to_cart.click()
    sleep(3)


@step('click Brand Outlet')
def go_to_brand_outlet(context):
    brand_otlet = context.driver.find_element(by=By.XPATH,
                                              value="//a[@class='gh-p' and contains(text(), 'Outlet')]")
    brand_otlet.click()
    sleep(2)


@step('Make sure you\'ve been navigated to Brand Outlet')
def validate_page_bo(context):
    page_bo = context.driver.find_element(by=By.XPATH,
                                          value="//span[@class='b-pageheader__text']")
    assert page_bo.text == 'The Brand Outlet'


@step('choose Champion - up to 50 percent off')
def choose_champion(context):
    cat = context.driver.find_element(by=By.XPATH,
                                      value="//span[@class='b-accordion-text' and contains(text(), 'Clothing')]")
    cat.click()
    sub_cat = context.driver.find_element(by=By.XPATH,
                                          value="//ul[@class = 'b-accordion-subtree']//a[contains(text(), 'Champion')]")
    sub_cat.click()
    sleep(2)


@step('choose shop category "cameras & photo"')
def choose_cat_cameras(context):
    btn_list_of_cat = context.driver.find_element(by=By.XPATH,
                                                  value="//button[@id='gh-shop-a']")
    btn_list_of_cat.click()
    cat = context.driver.find_element(by=By.XPATH,
                                      value="//li/a[@class='scnd' and text()='Cameras & Photo']")
    cat.click()
    sleep(2)


@step('choose category "camera drones"')
def choose_cet_camera_drones(context):
    cat = context.driver.find_element(by=By.XPATH,
                                      value="//div[@class='b-visualnav__title' and text()='Camera Drones']")
    cat.click()
    sleep(2)


@step('choose "DJI camera drones"')
def choose_dji(context):
    vendor = context.driver.find_element(by=By.XPATH,
                                         value="//p[@class='b-guidancecard__title' and contains(text(), 'DJI')]")
    vendor.click()
    sleep(2)


@step('choose model "DJI Mavic 2 Pro"')
def choose_model(context):
    model = context.driver.find_element(by=By.XPATH,
                                        value="//p[@class='b-guidancecard__title' and contains(text(), 'Mavic 2 Pro')]")
    model.click()
    sleep(2)


@step('choose only "buy it now"')
def choose_by_now(context):
    buy_it_now = context.driver.find_element(by=By.XPATH,
                                             value="//h2[@class='srp-format-tabs-h2' and text()='Buy It Now']")
    buy_it_now.click()
    sleep(2)


@step('choose first deal from the list')
def choose_first_deal(context):
    deal = context.driver.find_element(by=By.XPATH,
                                       value="//li[@class='s-item s-item--large']")
    deal.click()
    sleep(2)


@step('click to Sell')
def go_to_sell(context):
    sell_page = context.driver.find_element(by=By.XPATH,
                                            value="//a[@class='gh-p' and contains(text(), 'Sell')]")
    sell_page.click()
    sleep(2)


@step('Make sure you\'ve been navigated to Sell')
def validate_sell_page(context):
    sell_page = context.driver.find_element(by=By.XPATH,
                                            value="//h1[@class='textual-display sell-home__page-title']/span")
    sell_page_footer = context.driver.find_element(by=By.XPATH,
                                                   value="//h3[@class = 'textual-display footer-links__title' "
                                                         "and contains(text(), 'Selling')]")
    assert sell_page.text == 'You are on selling home page'
    assert sell_page_footer.text == 'Selling on eBay'


# sometimes need to use this code when choose from category
@step('click "Add to the cart second way"')
def add_to_cart(context):
    button_add_to_cart = context.driver.find_element(by=By.XPATH,
                                                     value="//div[@class='item-desc']"
                                                           "//a[@data-action-name='ADDTOCART' and text()='Add to cart']")
    button_add_to_cart.click()
    sleep(2)
