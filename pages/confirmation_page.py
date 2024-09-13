from playwright.sync_api import Page

class ConfirmationPage:
    def __init__(self, page: Page):
        self.page = page

    def get_heading(self):
        return self.page.get_by_role("heading", name="Appointment Confirmation")

    def get_summary(self):
        return self.page.locator("#summary")

    def get_facility(self):
        return self.page.locator("#facility")

    def get_hospital_readmission(self):
        return self.page.locator("#hospital_readmission")

    def get_program(self):
        return self.page.locator("#program")

    def get_visit_date(self):
        return self.page.locator("#visit_date")

    def get_comment(self):
        return self.page.locator("#comment")