import os

from selene import have, command, be
from selene.support.shared import browser

from demoqa_tests import tests


class RegistrationPage():

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').click().send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def select_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    def select_hobby(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()

    def upload_picture(self, image):
        browser.element("#uploadPicture").set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f'resources/{image}')
            )
        )

    def fill_address(self, street):
        browser.element('#currentAddress').should(be.blank).type(street)

    def select_state(self, name):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(name)).click()

    def select_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(name)).click()

    def submit_form(self):
        browser.element('#submit').press_enter()

    def should_registration_user_with(self, name, last_name, email, gender, number,
                                      date_of_birth, subject, hobby, image_name,
                                      address, state, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f'{name} {last_name}',
                             email,
                             gender,
                             number,
                             date_of_birth,
                             subject,
                             hobby,
                             image_name,
                             address,
                             f'{state} {city}'
                             )
        )
