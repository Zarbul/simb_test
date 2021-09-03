from selenium.webdriver.common.by import By

from .base import BasePage


class SendLocators:
    """Locators for create and send email."""
    LOCATOR_WRITE_BUTTON = (By.XPATH, '//div[text()="Написать"]')
    LOCATOR_TO = (By.NAME, 'to')
    LOCATOR_TITLE = (By.NAME, 'subjectbox')
    LOCATOR_TEXT = (By.CSS_SELECTOR, 'div[aria-label="Тело письма"]')
    LOCATOR_SEND_BUTTON = (By.XPATH, '//div[text()="Отправить"]')


class SendEmailHelper(BasePage):
    """Create and send email."""
    def click_on_write_button(self):
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
        text_email.send_keys(text)

        send_button = self.find_element(SendLocators.LOCATOR_SEND_BUTTON)
        send_button.click()
