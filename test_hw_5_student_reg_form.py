from selene import browser, have, by, be


def test_student_reg_form():
    browser.driver.execute_script('document.querySelector("#footer").remove()')
    browser.open('/automation-practice-form')
    # browser.execute_script('document.body.style.zoom="90%"')
    browser.element('.practice-form-wrapper').should(
        have.text('Student Registration Form')
    )

    browser.element('#firstName').set_value('Yuriy')
    browser.element('#lastName').set_value('Gladkov')
    browser.element('#userEmail').set_value('test@e.mail')
    # browser.element('#gender-radio-1').double_click()
    browser.element('[name=gender][value=Male]+label').click()
    # browser.element('[name=gender]').element(have.value('Male')).element('..').click()
    browser.element('#userNumber').set_value('14563214580')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').element_by(
        have.exact_text('July')
    ).click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option').element_by(
        have.exact_text('1980')
    ).click()
    browser.all('.react-datepicker__day').element_by(have.exact_text('15')).click()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#subjectsInput').type('Co').press_enter()
    browser.element('#uploadPicture').send_keys('D:/test.txt')
    browser.element('#currentAddress').type('Green forest str.')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Haryana')
    ).click()
    # browser.all('#state div').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('#city div').element_by(have.exact_text('Karnal')).click()
    browser.element('#submit').click()

    browser.element('.modal-content').should(be.visible)
    browser.element('#example-modal-sizes-title-lg').should(
        have.exact_text('Thanks for submitting the form')
    )
    browser.all('.table').all('td').should(
        have.exact_texts(
            ('Student Name', 'Yuriy Gladkov'),
            ('Student Email', 'test@e.mail'),
            ('Gender', 'Male'),
            ('Mobile', '1456321458'),
            ('Date of Birth', '15 July,1980'),
            ('Subjects', 'Computer Science'),
            ('Hobbies', 'Sports'),
            ('Picture', 'test.txt'),
            ('Address', 'Green forest str.'),
            ('State and City', 'Haryana Karnal'),
        )
    )

    browser.element("#closeLargeModal").click()
    browser.should(have.url("https://demoqa.com/automation-practice-form"))
