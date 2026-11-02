from playwright.sync_api import Page
class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        #self.login_button = page.get_by_role("button",'type= submit')

    

    def navigation(self):
        self.page.goto("https://the-internet.herokuapp.com/logins")
    
    def login(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        #self.login_button.click()
        print("logged in successfully")

