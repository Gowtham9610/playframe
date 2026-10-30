from playwright.sync_api import Page

def test_valid_login(login_page,page:Page):
    login_page.navigation()
