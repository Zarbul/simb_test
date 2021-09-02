import os

from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from base.base import BasePage


load_dotenv()
EMAIL_TITLE = str(os.getenv("EMAIL_TITLE"))


class Locators:
    LOCATOR_SEARCH_EMAIL_TITLE = (By.XPATH, f'//span[@class="bqe"][text()="{EMAIL_TITLE}"]')


class FindHelper(BasePage):
    def search_email(self, word):
        search_email = self.find_element(Locators.LOCATOR_SEARCH_EMAIL_TITLE)
        return search_email

    def count_emails(self):
        search_emails = self.find_elements(Locators.LOCATOR_SEARCH_EMAIL_TITLE)
        count_emails = len(search_emails)
        return count_emails
