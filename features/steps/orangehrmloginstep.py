import time

from behave import *
from selenium import webdriver


@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()



@when('I open orange HRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(15)


@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element("xpath", "//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element("xpath", "//input[@placeholder='Password']").send_keys(pwd)


@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element('xpath', "//button[@type='submit']").click()


@then(u'User must successfully login to the dashboard page')
def step_impl(context):
    time.sleep(10)
    try:
        text = context.driver.find_element('xpath', "//span/h6[.='Dashboard']").text
    except:
        context.driver.close()
        assert False, "Test Failed"
        assert text == 'Dashboard'
    if text == 'Dashboard':
        context.driver.close()
        assert True,"Test Passed"
