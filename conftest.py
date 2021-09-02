import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(f'--user-agent={USER_AGENT}')
    # browser = webdriver.Chrome(executable_path="./drivers/chromedriver", options=options)
    browser = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True},
        options=options
    )

    yield browser
    browser.quit()
