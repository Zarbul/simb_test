from selenium.webdriver.common.keys import Keys

from base.base import BasePage
from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")


class AuthHelper(BasePage):
    def enter_email(self, word):
        email_field = self.find_element(Locators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(word, Keys.RETURN)
        return email_field

    def enter_password(self, word):
        password_field = self.find_element(Locators.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(word, Keys.RETURN)
        return password_field
