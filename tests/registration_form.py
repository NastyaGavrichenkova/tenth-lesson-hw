import os
from selene.support.shared import browser
from selene import be, have


def test_successful_registration():
    browser.open('/automation-practice-form')

    # WHEN
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')

    browser.element('#firstName').should(be.blank).type('leia')
    browser.element('#lastName').should(be.blank).type('organa')
    browser.element('#userEmail').should(be.blank).type('leia@gmail.com')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').should(be.blank).type('0123456789')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('May')
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').send_keys('1977')
    browser.element(f'.react-datepicker__day--0{25}').click()

    browser.element('#subjectsInput').should(be.blank).type('english').press_enter()
    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Reading')).click()
    # browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element("#uploadPicture").send_keys(os.path.abspath('resources/image_test.JPG'))

    browser.element('#currentAddress').should(be.blank).type('1 RIDGE AVE SUFFERN NY 10901-5807 USA')

    # browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()

    # browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Delhi')).click()

    browser.element('#submit').press_enter()

    # THEN
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'leia organa',
            'leia@gmail.com',
            'Female',
            '0123456789',
            '25 May 1977',
            'English',
            'Reading',
            'image_test.JPG',
            '1 RIDGE AVE SUFFERN NY 10901-5807 USA',
            'NCR',
            'Delhi'
        )
    )
