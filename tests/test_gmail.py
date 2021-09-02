import os
from time import sleep

import pytest
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

from pages.google_authorization_page import AuthHelper
from pages.find_emails_page import FindHelper
from pages.send_email_page import SendHelper

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')
EMAIL_TITLE = 'Тестовое задание. Каменев.'


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(20)
    selenium.set_page_load_timeout(20)
    return selenium


class TestGmail:

    @allure.feature('Test GMail.')
    @allure.story('Authorization in gmail.com, find and send email.')
    @allure.severity('blocker')
    def test_auth(self, selenium):
        """Authorization in gmail.com, find and send email."""
        gmail_page = AuthHelper(selenium)
        gmail_page.go_to_site()
        with allure.step('Делаем скриншот авторизации'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_auth',
                          attachment_type=AttachmentType.PNG)
        assert selenium.title == 'Gmail', 'Страница gmail.com не загрузилась.'
        gmail_page.enter_email(LOGIN)
        sleep(3)
        gmail_page.enter_password(PASSWORD)
        sleep(3)
        assert LOGIN in selenium.title, 'Авторизация не выполнена.'

        gmail_page = FindHelper(selenium)
        with allure.step('Делаем скриншот главной страницы'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_main_gmail',
                          attachment_type=AttachmentType.PNG)
        gmail_page.search_email(TO_EMAIL)
        emails = gmail_page.count_emails()
        with allure.step('Делаем скриншот найденых сообщений'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_sind_messages',
                          attachment_type=AttachmentType.PNG)
        assert isinstance(emails, int), 'Поиск сообщений не выполнен.'

        gmail_page = SendHelper(selenium)
        gmail_page.write_button()
        gmail_page.write_email(TO_EMAIL, EMAIL_TITLE, emails)
        with allure.step('Делаем скриншот отправленных сообщений'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_sind_messages',
                          attachment_type=AttachmentType.PNG)