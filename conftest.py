from playwright.sync_api import Page
from pages.login_page import LoginPage
import pytest

@pytest.fixture()
def login_page(page:Page):
    return LoginPage(page)
