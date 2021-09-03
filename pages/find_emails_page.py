import os

from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from .base import BasePage


load_dotenv()
EMAIL_TITLE = str(os.getenv("EMAIL_TITLE"))


class Locators:
    LOCATOR_SEARCH_EMAIL_TITLE = (By.XPATH, f'//span[@class="bqe"][text()="{EMAIL_TITLE}"]')


class FindEmailHelper(BasePage):
    def search_email(self):
        self.find_element(Locators.LOCATOR_SEARCH_EMAIL_TITLE)

    def count_emails(self):
        search_emails = self.find_elements(Locators.LOCATOR_SEARCH_EMAIL_TITLE)
        count_emails = int(len(search_emails) / 2)
        return count_emails
