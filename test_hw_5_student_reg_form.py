from selene import browser, have, by


def test_student_reg_form():

    browser.open('/automation-practice-form')
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    browser.element('#firstName').set_value('First Name')
    browser.element('#lastName').set_value('Last Name')
    browser.element('#userEmail').set_value('test@e.mail')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').set_value('+1456321458')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').element_by(have.exact_text('July')).click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option').element_by(have.exact_text('1980')).click()
    browser.all('.react-datepicker__day').element_by(have.exact_text('15')).click()
    browser.element('#subjectsInput').type('Computer Sciense').press_tab()
    browser.element('#hobbies-checkbox-1').click()


    ...

