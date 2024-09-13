from playwright.sync_api import Page

class AppointmentBookingPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_username(self, username):
        self.page.get_by_label("Username").fill(username)
        return self

    def fill_password(self, password):
        self.page.get_by_label("Password").fill(password)
        return self

    def select_facility(self, facility):
        self.page.get_by_label("Facility").select_option(facility)
        return self

    def check_apply_for_hospital_readmission(self):
        self.page.get_by_label("Apply for hospital readmission").check()
        return self

    def check_program(self, program):
        self.page.get_by_label(program).check()
        return self

    def select_visit_date(self, visit_date):
        self.page.locator("span").click()
        self.page.get_by_role("cell", name=visit_date).click()
        return self

    def fill_comment(self, comment):
        self.page.get_by_placeholder("Comment").fill(comment)
        return self

    def click_book_appointment(self):
        self.page.get_by_role("button", name="Book Appointment").click()
        return self