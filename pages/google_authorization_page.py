from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import BasePage


class Locators:
    LOCATOR_EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")


class AuthHelper(BasePage):
    def enter_email(self, email):
        email_field = self.find_element(Locators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email, Keys.RETURN)

    def enter_password(self, password):
        password_field = self.find_element(Locators.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password, Keys.RETURN)

