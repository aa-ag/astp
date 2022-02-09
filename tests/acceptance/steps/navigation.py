from behave import *
from selenium import webdriver

# reads from navigation feature
use_step_matcher('re')


@given('I am on the homepage')
def step_implementation(context):
    browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    browser.get('http://127.0.0.1:5000')