from playwright.sync_api import Page

class AppointmentHistoryPage:
    def __init__(self, page: Page):
        self.page = page

    def get_heading(self):
        return self.page.get_by_role("heading", name="History")

    def get_facility_hongkong(self):
        return self.page.get_by_text("Facility Hongkong CURA")

    def get_facility_seoul(self):
        return self.page.get_by_text("Facility Seoul CURA")