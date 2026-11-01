from playwright.sync_api import expect


def test_login_navigation(login_page):

    login_page.navigation()

    expect(login_page.page).to_have_url(
        "https://the-internet.herokuapp.com/login"
    )

    expect(login_page.username).to_be_visible()
    expect(login_page.password).to_be_visible()