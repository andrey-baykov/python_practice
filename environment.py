import os
import shutil

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.browser_mode = "regular"

    folder = './screenshots/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception:
            raise OSError(f"Can't delete {file_path}.")


def before_feature(context, feature):
    if "incognito" in feature.name:
        context.browser_mode = 'incognito'


def before_scenario(context, scenario):
    context.scenario_name = scenario.name
    context.filters = []

    if context.browser_mode == 'incognito':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                          chrome_options=chrome_options)
    else:
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def before_step(context, step):
    pass


def after_step(context, step):
    if step.status == 'failed':
        path = "./screenshots/" + context.scenario_name + "/"
        os.mkdir(path)
        context.driver.save_screenshot(path + step.name + ".png")


def after_scenario(context, scenario):
    context.driver.quit()


def after_feature(context, feature):
    pass


def after_all(context):
    pass
