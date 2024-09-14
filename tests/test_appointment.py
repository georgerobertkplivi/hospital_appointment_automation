import pytest

from pages.confirmation_page import ConfirmationPage
from pages.home_page import HomePage


@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def confirmation_page(page):
    return ConfirmationPage(page)


@pytest.mark.parametrize("username, password, expected_error_message", [
    ("", "", "Username and password are required"),
    ("John Doe", "", "Password is required"),
    ("", "ThisIsNotAPassword", "Username is required"),
    ("Invalid User", "ThisIsNotAPassword", "Invalid username or password"),
])
def test_invalid_login_credentials(home_page, username, password, expected_error_message):
    home_page.navigate_to().login(username, password)
    home_page.get_error_message().to_contain_text(expected_error_message)

def test_make_appointment(home_page, appointment_booking_page, confirmation_page):
    home_page.navigate_to().login("John Doe", "ThisIsNotAPassword").get_make_appointment_link().click()

    (appointment_booking_page.fill_username("John Doe").fill_password("ThisIsNotAPassword").
     select_facility("Hongkong CURA Healthcare Center").
     check_apply_for_hospital_readmission().
     check_program("Medicaid").select_visit_date("11/01/2024").
     fill_comment("Test Appointment").click_book_appointment())

    confirmation_page.get_heading().to_be_visible()
    confirmation_page.get_summary().to_contain_text("Please be informed that your appointment has been booked as following:")

def test_facility_selection_dropdown_populated(home_page):
    home_page.navigate_to()
    facilities = home_page.get_facility_selection_options()
    assert len(facilities) > 0, "Facility selection dropdown is empty"
    assert facilities[0] == "Select Facility", "Default option is not 'Select Facility'"

def test_facility_selection_dropdown_sorted(home_page):
    home_page.navigate_to()
    facilities = home_page.get_facility_selection_options()
    assert facilities == sorted(facilities), "Facility selection dropdown is not sorted alphabetically"

def test_facility_selection_default_option(home_page):
    home_page.navigate_to()
    default_option = home_page.get_facility_selection_default_option()
    assert default_option == "Select Facility", "Default option is not 'Select Facility'"

def test_facility_selection_invalid_option(home_page):
    home_page.navigate_to()
    home_page.select_facility("Invalid Facility")
    error_message = home_page.get_error_message()
    assert error_message, "Error message is not displayed for invalid facility selection"
    assert "Invalid facility selected" in error_message, "Error message is not correct"


def test_successful_login(home_page, dashboard_page):
    home_page.navigate_to().login("Valid User", "Valid Password")
    dashboard_page.wait_for_load()
    assert dashboard_page.is_loaded(), "Dashboard page is not loaded"
    assert dashboard_page.get_welcome_message() == "Welcome, Valid User", "Welcome message is not correct"

def test_unsuccessful_login_invalid_username(home_page):
    home_page.navigate_to().login("Invalid User", "Valid Password")
    error_message = home_page.get_error_message()
    assert error_message, "Error message is not displayed for invalid username"
    assert "Invalid username or password" in error_message, "Error message is not correct"

def test_unsuccessful_login_invalid_password(home_page):
    home_page.navigate_to().login("Valid User", "Invalid Password")
    error_message = home_page.get_error_message()
    assert error_message, "Error message is not displayed for invalid password"
    assert "Invalid username or password" in error_message, "Error message is not correct"

def test_unsuccessful_login_blank_username(home_page):
    home_page.navigate_to().login("", "Valid Password")
    error_message = home_page.get_error_message()
    assert error_message, "Error message is not displayed for blank username"
    assert "Username is required" in error_message, "Error message is not correct"

def test_unsuccessful_login_blank_password(home_page):
    home_page.navigate_to().login("Valid User", "")
    error_message = home_page.get_error_message()
    assert error_message, "Error message is not displayed for blank password"
    assert "Password is required" in error_message, "Error message is not correct"

def test_visit_date_selection(dashboard_page):
    dashboard_page.navigate_to()
    dashboard_page.select_visit_date("2022-01-01")
    assert dashboard_page.get_selected_visit_date() == "2022-01-01", "Selected visit date is not correct"

def test_visit_date_selection_invalid_date(dashboard_page):
    dashboard_page.navigate_to()
    dashboard_page.select_visit_date("Invalid Date")
    error_message = dashboard_page.get_error_message()
    assert error_message, "Error message is not displayed for invalid date"
    assert "Invalid date format" in error_message, "Error message is not correct"

def test_visit_date_selection_blank_date(dashboard_page):
    dashboard_page.navigate_to()
    dashboard_page.select_visit_date("")
    error_message = dashboard_page.get_error_message()
    assert error_message, "Error message is not displayed for blank date"
    assert "Visit date is required" in error_message, "Error message is not correct"

def test_program_selection(dashboard_page):
    dashboard_page.navigate_to()
    dashboard_page.select_program("Program 1")
    assert dashboard_page.get_selected_program() == "Program 1", "Selected program is not correct"

def test_program_selection_invalid_program(dashboard_page):
    dashboard_page.navigate_to()
    dashboard_page.select_program("Invalid Program")
    error_message = dashboard_page.get_error_message()
    assert error_message, "Error message is not displayed for invalid program"
    assert "Invalid program" in error_message, "Error message is not correct"

def test_program_selection_blank_program(dashboard_page):
    dashboard_page.navigate_to()
    dashboard_page.select_program("")
    error_message = dashboard_page.get_error_message()
    assert error_message, "Error message is not displayed for blank program"
    assert "Program is required" in error_message, "Error message is not correct"

def test_comment_field(dashboard_page):
    dashboard_page.navigate_to()
    dashboard_page.enter_comment("This is a test comment")
    assert dashboard_page.get_comment_text() == "This is a test comment", "Comment text is not correct"

def test_comment_field_max_length(dashboard_page):
    dashboard_page.navigate_to()
    long_comment = "a" * 256
    dashboard_page.enter_comment(long_comment)
    error_message = dashboard_page.get_error_message()
    assert error_message, "Error message is not displayed for long comment"
    assert "Comment is too long" in error_message, "Error message is not correct"

def test_book_appointment_button(dashboard_page):
    dashboard_page.navigate_to()
    dashboard_page.select_visit_date("2022-01-01")
    dashboard_page.select_program("Program 1")
    dashboard_page.enter_comment("This is a test comment")
    dashboard_page.click_book_appointment_button()
    assert dashboard_page.is_confirmation_page_displayed(), "Confirmation page is not displayed"


def test_confirmation_page_displayed(confirmation_page):
    confirmation_page.navigate_to()
    assert confirmation_page.is_confirmation_page_displayed(), "Confirmation page is not displayed"

def test_confirmation_page_details(confirmation_page):
    confirmation_page.navigate_to()
    assert confirmation_page.get_visit_date() == "2022-01-01", "Visit date is not correct"
    assert confirmation_page.get_program() == "Program 1", "Program is not correct"
    assert confirmation_page.get_comment() == "This is a test comment", "Comment is not correct"

def test_error_handling_invalid_request(dashboard_page):
    dashboard_page.navigate_to()
    dashboard_page.make_invalid_request()
    error_message = dashboard_page.get_error_message()
    assert error_message, "Error message is not displayed for invalid request"
    assert "Invalid request" in error_message, "Error message is not correct"

def test_error_handling_server_error(dashboard_page):
    dashboard_page.navigate_to()
    dashboard_page.simulate_server_error()
    error_message = dashboard_page.get_error_message()
    assert error_message, "Error message is not displayed for server error"
    assert "Server error" in error_message, "Error message is not correct"

