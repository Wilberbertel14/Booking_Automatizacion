from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from lib.pages.home_page import HomePage
import time

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.wait = WebDriverWait(context.browser, 10)
    context.home_page = HomePage(context)

def after_all(context):
    context.browser.quit()

def before_feature(context, feature):
    context.url = "https://www.booking.com"