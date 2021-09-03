from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Methods for working with webdriver."""
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://gmail.com/"

    def find_element(self, locator, time=10):
        """Find element."""
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """Find elements."""
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        """Load page ."""
        return self.browser.get(self.base_url)
