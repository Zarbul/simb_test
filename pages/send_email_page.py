import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.base import BasePage


class SendLocators:
    """Locators for create and send email."""
    LOCATOR_WRITE_BUTTON = (By.XPATH, '//div[text()="Написать"]')
    LOCATOR_TO = (By.NAME, 'to')
    LOCATOR_TITLE = (By.NAME, 'subjectbox')
    LOCATOR_TEXT = (By.CSS_SELECTOR, 'div[aria-label="Тело письма"]')


class SendHelper(BasePage):
    """Create and send email."""
    def write_button(self):
        """Push button 'Write'."""
        button = self.find_element(SendLocators.LOCATOR_WRITE_BUTTON)
        button.click()

    def write_email(self, to_email, title, text):
        """Create and send email."""
        email_to = self.find_element(SendLocators.LOCATOR_TO)
        email_to.send_keys(to_email)

        topic_email = self.find_element(SendLocators.LOCATOR_TITLE)
        topic_email.send_keys(title)

        text_email = self.find_element(SendLocators.LOCATOR_TEXT)
        text_email.send_keys(text, Keys.CONTROL, Keys.ENTER)
