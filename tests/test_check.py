from playwright.sync_api import Page

def test_checks(page:Page):
    page.goto("https://www.google.com/")
    page.locator("//*[@name='q']").fill("gowtham")
    print("test completed")

