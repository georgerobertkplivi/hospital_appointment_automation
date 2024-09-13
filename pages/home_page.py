from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self):
        self.page.goto("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        return self

    def login(self, username, password):
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
        if self.page.get_by_role("alert").is_visible():
            raise Exception("Login failed")
        return self

    def get_heading(self):
        return self.page.get_by_role("heading", name="We Care About Your Health")

    def get_make_appointment_link(self):
        return self.page.get_by_role("link", name="Make Appointment")