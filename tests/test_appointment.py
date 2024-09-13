def test_make_appointment(home_page, appointment_booking_page, confirmation_page):
    home_page.navigate_to().login("John Doe", "ThisIsNotAPassword").get_make_appointment_link().click()

    (appointment_booking_page.fill_username("John Doe").fill_password("ThisIsNotAPassword").
     select_facility("Hongkong CURA Healthcare Center").
     check_apply_for_hospital_readmission().
     check_program("Medicaid").select_visit_date("11").
     fill_comment("Test Appointment").click_book_appointment())

    confirmation_page.get_heading().to_be_visible()
    confirmation_page.get_summary().to_contain_text("Please be informed that your appointment has been booked as following:")