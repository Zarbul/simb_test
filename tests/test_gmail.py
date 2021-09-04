import os
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

from pages.base import BasePage
from pages.google_authorization_page import AuthHelper
from pages.find_emails_page import FindEmailHelper
from pages.send_email_page import SendEmailHelper

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')
EMAIL_TITLE = os.getenv('EMAIL_TITLE')
SEND_TITLE = 'Тестовое задание. Каменев.'


class TestGmail:

    @allure.feature('Test GMail.')
    @allure.story('Authorization in gmail.com.')
    @allure.severity('blocker')
    def test_load_auth_page(self, browser):
        """Open Gmail.com page."""
        with allure.step("Open Gmail.com page."):
            gmail_page = BasePage(browser)
            gmail_page.go_to_site()
            assert browser.title == 'Gmail', 'Page Gmail.com not load.'

    @allure.feature('Test GMail.')
    @allure.story('Authorization in gmail.com.')
    @allure.severity('blocker')
    def test_auth(self, browser):
        """Authorization in Gmail.com."""
        with allure.step("Authorization in Gmail.com."):
            auth_page = AuthHelper(browser)
            auth_page.enter_email(LOGIN)
            auth_page.enter_password(PASSWORD)
            assert LOGIN in browser.title, 'Authorization failed.'

    @allure.feature('Test GMail.')
    @allure.story('Find and send email.')
    @allure.severity('normal')
    def test_find_emails(self, browser):
        """Search messages."""
        with allure.step("earch messages."):
            email_page = FindEmailHelper(browser)
            email_page.search_email()
            count_emails = email_page.count_emails()
            assert isinstance(count_emails, int), 'Emails not found.'

    @allure.feature('Test GMail.')
    @allure.story('Find and send email.')
    @allure.severity('critical')
    def test_send_email(self, browser):
        """Sending a message."""
        with allure.step("Sending a message."):
            send_page = SendEmailHelper(browser)
            count_emails = FindEmailHelper(browser).count_emails()
            send_page.click_on_write_button()
            send_page.write_email(TO_EMAIL, SEND_TITLE, count_emails)
            with allure.step('Get screenshot with send emails.'):
                allure.attach(browser.get_screenshot_as_png(),
                              name='screenshot_send_emails',
                              attachment_type=AttachmentType.PNG)
