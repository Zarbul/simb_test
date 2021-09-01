from datetime import time
from random import randint

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="session")
def browser():
    gmail = 'mufasa13q13@gmail.com'
    password = 'MUFASA1!'
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=/tmp/chromium-gmail-' + str(randint(1, 200)))
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(f'--user-agent={USER_AGENT}')
    browser = webdriver.Chrome(options=options)
    browser.get(
        "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    time.sleep(randint(1, 15))
    browser.find_element_by_xpath("//input[@type='email']").click()
    browser.find_element_by_xpath("//input[@type='email']").send_keys(gmail)
    time.sleep(randint(1, 15))
    browser.find_element_by_xpath("//input[@type='email']").send_keys(Keys.RETURN)
    time.sleep(randint(1, 15))
    browser.find_element_by_xpath("//input[@type='password']").send_keys(password)
    time.sleep(randint(1, 15))
    browser.find_element_by_xpath("//input[@type='password']").send_keys(Keys.RETURN)
    time.sleep(15)
    print('logged in')


    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()