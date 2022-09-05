from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    pass


def before_feature(context, feature):
    pass

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def before_step(context, step):
    pass


def after_step(context, step):
    pass

def after_scenario(context, scenario):
    context.driver.quit()


def after_feature(context, feature):
    pass


def after_all(context):
    pass
