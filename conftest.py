import os

import pytest
from selenium import webdriver
from dotenv import load_dotenv


load_dotenv()


@pytest.fixture(scope="session")
def browser():
    LOGIN = str(os.getenv("LOGIN"))
    PASSWORD = str(os.getenv("PASSWORD"))

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(f'--user-agent={USER_AGENT}')
    browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()