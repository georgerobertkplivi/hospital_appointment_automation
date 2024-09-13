import pytest
from playwright.sync_api import sync_playwright

from pages.appointment_booking_page import AppointmentBookingPage
from pages.appointment_history_page import AppointmentHistoryPage
from pages.confirmation_page import ConfirmationPage
from pages.home_page import HomePage


@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def appointment_booking_page(page):
    return AppointmentBookingPage(page)

@pytest.fixture
def confirmation_page(page):
    return ConfirmationPage(page)

@pytest.fixture
def appointment_history_page(page):
    return AppointmentHistoryPage(page)

@pytest.fixture
def playwright():
    with sync_playwright() as p:
        yield p