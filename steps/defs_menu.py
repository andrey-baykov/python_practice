import warnings
from time import sleep

from behave import step
from selenium import webdriver
from selenium.common import NoSuchElementException
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
    if not current_item:
        raise Exception(f'Item {param} is not found')
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


@step('click "Shop by category" and choose "{category}"')
def choose_subcat(context, category):
    shop_by_cat = context.driver.find_element(by=By.XPATH,
                                              value=f"//button[@id='gh-shop-a' and text()='Shop by category']")
    shop_by_cat.click()
    cat = context.driver.find_element(by=By.XPATH,
                                      value=f"//a[text()='{category}'][ancestor::div[@id='gh-sbc-o']]")
    cat.click()
    sleep(2)


@step('verify page "{title}" was opened')
def verify_page(context, title):
    try:
        page = context.driver.find_element(by=By.XPATH,
                                           value=f"//h1[@class='title-banner__title']")
        warnings.warn('Worked first type of page')
    except NoSuchElementException:
        warnings.warn('Worked second type of page')
        page = context.driver.find_element(by=By.XPATH,
                                           value=f"//h1[@class='b-pageheader']/span")
    assert page.text == title, f"Inspected page title: '{title}', but actual title is: '{page.text}'"


@step('choose left menu "{menu}"')
def choose_left_menu_item(context, menu):
    menu = context.driver.find_element(by=By.XPATH,
                                       value=f"//div[@class='dialog__cell'][.//h2[text()='Shop by Category']]"
                                             f"//a[text()='{menu}']")
    menu.click()
    sleep(3)


@step('choose slide menu "{menu}"')
def choose_slide_menu_item(context, menu):
    slider = context.driver.find_element(by=By.XPATH,
                                         value=f"//div[@class='carousel'][.//p[text()='{menu}']]"
                                               f"//button[@class='carousel__control carousel__control--next']")
    slider.click()
    menu = context.driver.find_element(by=By.XPATH,
                                       value=f"//ul[@class='carousel__list'][.//p[@class='b-guidancecard__title']]"
                                             f"//p[text()='{menu}']")
    menu.click()


@step('choose block menu "{menu}"')
def choose_blocks_menu(context, menu):
    menu = context.driver.find_element(by=By.XPATH,
                                       value=f"//div[@class='b-visualnav__grid'][.//div[@class='b-visualnav__title']]"
                                             f"//div[text()='{menu}']")
    menu.click()


@step('choose in top menu "{category}"')
def choose_top_menu(context, category):
    cat_top = context.driver.find_element(by=By.XPATH,
                                          value=f"//li[@class='hl-cat-nav__js-tab']/a[text()='{category}']")
    cat_top.click()
    sleep(2)


@step('open list of "{category}"')
def open_cat_list(context, category):
    cat = context.driver.find_element(by=By.XPATH,
                                      value=f"//div[@class='dialog__cell'][.//h2[text()='Shop by Category']]"
                                            f"//span[text()='{category}']")
    cat.click()
    sleep(2)


@step('quick top filter "{filter}"')
def choose_top_filter(context, filter):
    cat = context.driver.find_element(by=By.XPATH,
                                      value=f"//div[@class='b-visualnav__grid']"
                                            f"//*[text()='{filter}']")
    cat.click()
    sleep(2)


@step('verify item contains text "{param}"')
def verify_item(context, param):
    current_item = context.driver.find_element(by=By.XPATH,
                                               value=f"//div[@class='s-item__info clearfix']"
                                                     f"[.//h3[@class='s-item__title s-item__title--has-tags']]//h3")
    if param not in current_item.text:
        raise Exception(f'Item "{param}" is not found in text:"{current_item.text}"')
    sleep(2)


@step('verify item price lower than {price}')
def verify_lower_price(context, price):
    item_price = context.driver.find_element(by=By.XPATH,
                                             value=f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']"
                                                   f"[.//div[@class='s-item__info clearfix']]//span[@class='s-item__price']")
    current_price = float(item_price.text.strip("$"))
    if current_price > float(price):
        warnings.warn(f"Item price is ${current_price} which higher than ${price}")
        raise Exception('Price too high!')


@step('verify item price higher than {price}')
def verify_higher_price(context, price):
    item_price = context.driver.find_element(by=By.XPATH,
                                             value=f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']"
                                                   f"[.//div[@class='s-item__info clearfix']]//span[@class='s-item__price']")
    current_price = float(item_price.text.strip("$"))
    if current_price < float(price):
        warnings.warn(f"Item price is ${current_price} which lower than ${price}")
        raise Exception('Price too low!')


@step('verify item price between {low_price} and {high_price}')
def verify_higher_price(context, low_price, high_price):
    item_price = context.driver.find_element(by=By.XPATH,
                                             value=f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']"
                                                   f"[.//div[@class='s-item__info clearfix']]//span[@class='s-item__price']")
    current_price = float(item_price.text.strip("$"))
    if current_price < float(low_price):
        warnings.warn(f"Item price is ${current_price} which lower than ${low_price}")
        raise Exception('Price too low!')
    elif current_price > float(high_price):
        warnings.warn(f"Item price is ${current_price} which higher than ${high_price}")
        raise Exception('Price too high!')


@step('verify item has "Free shipping"')
def verify_free_shipping(context):
    shipping = context.driver.find_element(by=By.XPATH,
                                           value=f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']"
                                                 f"[.//div[@class='s-item__info clearfix']]//span[@class='s-item__shipping s-item__logisticsCost']")
    assert shipping.text == "Free shipping", f"Shipping price is '{shipping.text}' and NOT FREE!"


@step('verify item shipping price lower than {price}')
def verify_free_shipping(context, price):
    shipping = context.driver.find_element(by=By.XPATH,
                                           value=f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']"
                                                 f"[.//div[@class='s-item__info clearfix']]//span[@class='s-item__shipping s-item__logisticsCost']")
    if shipping.text == "Free shipping":
        warnings.warn('No price. Free shipping')
    elif float(shipping.text[2:6]) > float(price):
        raise Exception(f"Shipping price is '{shipping.text}' and higher than expected!")


@step('verify item has "Free returns"')
def verify_free_returns(context):
    return_policy = context.driver.find_element(by=By.XPATH,
                                                value=f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']"
                                                      f"[.//div[@class='s-item__info clearfix']]//span[@class='s-item__free-returns s-item__freeReturnsNoFee']")
    assert return_policy.text == "Free returns", "Return not free!"


@step('verify item condition is "{condition}"')
def verify_free_returns(context, condition):
    try:
        item_condition = context.driver.find_element(by=By.XPATH,
                                                     value=f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']"
                                                           f"[.//div[@class='s-item__info clearfix']]//span[@class='SECONDARY_INFO']")
        assert item_condition.text == condition, f"Expected condition is '{condition}', but " \
                                                 f"Actual condition is '{item_condition.text}'"
    except NoSuchElementException:
        warnings.warn('Need to create test for second form')
        raise Exception('Second type of page was shown')


@step('verify item is sponsored')
def verify_free_returns(context):
    try:
        sponsored = context.driver.find_element(by=By.XPATH,
                                                value=f"//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']"
                                                      f"[.//div[@class='s-item__info clearfix']]//span[text()='Sponsored']")
        assert sponsored
    except Exception:
        raise Exception("Item isn't sponsored")


@step('choose "{category}" in search line')
def choose_cat_search_line(context, category):
    cat_button = context.driver.find_element(by=By.XPATH,
                                             value=f"//select")
    cat_button.click()
    sleep(2)
    cat_from_list = context.driver.find_element(by=By.XPATH,
                                                value=f"//select[@aria-label='Select a category for search']/option[text()=' Music']")
    cat_from_list.click()
    sleep(3)


@step('click pages menu "{page}"')
def click_daily_deals(context, page):
    daily_deals_link = context.driver.find_element(by=By.XPATH,
                                                   value=f"//a[@class='gh-p' and contains(text(), '{page}')]")
    daily_deals_link.click()
    sleep(2)


@step('Make sure you have been navigated to page "{page}"')
def validate_page(context, page):
    page_title = context.driver.find_element(by=By.XPATH,
                                             value=f"//div[@class='navigation-desktop']/h1/a[text()='{page}']")
    assert page_title.text == 'Deals'


@step('verify SPOTLIGHT DEAL percentage more than {percent} %')
def verify_discount_percent(context, percent):
    current_discount = context.driver.find_element(by=By.XPATH,
                                                   value=f"//div[./h2/*[text()='Spotlight Deal']]"
                                                         f"//span[@class='itemtile-price-bold']")
    discount = float(current_discount.text[:2])
    if float(percent) > discount:
        warnings.warn(f'Expected discount more than "{percent}" but current "{discount}"')
        raise Exception('Discount too low!')


@step('verify SPOTLIGHT DEAL percentage between {min_percent} and {max_percent} %')
def verify_discount_percent(context, min_percent, max_percent):
    current_discount = context.driver.find_element(by=By.XPATH,
                                                   value=f"//div[./h2/*[text()='Spotlight Deal']]"
                                                         f"//span[@class='itemtile-price-bold']")
    discount = float(current_discount.text[:2])
    if float(min_percent) > discount:
        warnings.warn(f'Expected discount more than "{min_percent}%" but current "{discount}%"')
        raise Exception('Discount too low!')
    elif float(max_percent) < discount:
        warnings.warn(f'Expected discount less than "{max_percent}%" but current "{discount}%"')
        raise Exception('Discount too high!')


@step('verify SPOTLIGHT DEAL is correct')
def verify_discount_percent(context):
    current_discount = context.driver.find_element(by=By.XPATH,
                                                   value=f"//div[./h2/*[text()='Spotlight Deal']]"
                                                         f"//span[@class='itemtile-price-bold']")
    discount = float(current_discount.text[:2])
    normal_price = context.driver.find_element(by=By.XPATH,
                                               value=f"//div[./h2/*[text()='Spotlight Deal']]"
                                                     f"//span[@class='first']")
    price = float(normal_price.text[1:])
    disc_price = context.driver.find_element(by=By.XPATH,
                                             value=f"//div[./h2/*[text()='Spotlight Deal']]"
                                                   f"//span[@class='itemtile-price-strikethrough']")
    current_price = float(disc_price.text[1:])
    calc_discount = round(float((1 - price / current_price) * 100))

    assert calc_discount == discount, f"Calculated discount is {calc_discount}% but provided discount is {discount}%"

    #


@step('verify FEATURED DEALS percentage more than {percent} %')
def verify_min_discount_percentage(context, percent):
    current_discount = context.driver.find_element(by=By.XPATH,
                                                   value=f"//div[@class='ebayui-dne-item-featured-card ebayui-dne-item-featured-card']"
                                                         f"//span[@class='itemtile-price-bold']")
    discount = float(current_discount.text[:2])
    if float(percent) > discount:
        warnings.warn(f'Expected discount more than "{percent}" but current "{discount}"')
        raise Exception('Discount too low!')


@step('verify FEATURED DEALS percentage between {min_percent} and {max_percent} %')
def verify_minmax_discount_percentage(context, min_percent, max_percent):
    current_discount = context.driver.find_element(by=By.XPATH,
                                                   value=f"//div[@class='ebayui-dne-item-featured-card ebayui-dne-item-featured-card']"
                                                         f"//span[@class='itemtile-price-bold']")
    discount = float(current_discount.text[:2])
    if float(min_percent) > discount:
        warnings.warn(f'Expected discount more than "{min_percent}%" but current "{discount}%"')
        raise Exception('Discount too low!')
    elif float(max_percent) < discount:
        warnings.warn(f'Expected discount less than "{max_percent}%" but current "{discount}%"')
        raise Exception('Discount too high!')


@step('verify FEATURED DEALS is correct')
def verify_correct_discount_percentage(context):
    current_discount = context.driver.find_element(by=By.XPATH,
                                                   value=f"//div[@class='ebayui-dne-item-featured-card ebayui-dne-item-featured-card']"
                                                         f"//span[@class='itemtile-price-bold']")
    discount = float(current_discount.text[:2])
    normal_price = context.driver.find_element(by=By.XPATH,
                                               value=f"//div[@class='ebayui-dne-item-featured-card ebayui-dne-item-featured-card']"
                                                     f"//span[@class='first']")
    price = float(normal_price.text[1:])
    disc_price = context.driver.find_element(by=By.XPATH,
                                             value=f"//div[@class='ebayui-dne-item-featured-card ebayui-dne-item-featured-card']"
                                                   f"//span[@class='itemtile-price-strikethrough']")
    current_price = float(disc_price.text[1:])
    calc_discount = round(float((1 - price / current_price) * 100))

    assert calc_discount == discount, f"Calculated discount is {calc_discount}% but provided discount is {discount}%"
