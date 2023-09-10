from demoqa_tests.model.registration_page import RegistrationPage


def test_successful_registration():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_name('leia')
    registration_page.fill_last_name('organa')
    registration_page.fill_email('leia@gmail.com')
    registration_page.select_gender('Female')
    registration_page.fill_number('0123456789')

    registration_page.fill_date_of_birth('1977', 'May', '25')

    registration_page.select_subject('english')
    registration_page.select_hobby('Reading')

    registration_page.upload_picture('image_test.JPG')

    registration_page.fill_address('1 RIDGE AVE SUFFERN')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')

    registration_page.submit_form()

    # THEN
    registration_page.should_registration_user_with(
        'leia',
        'organa',
        'leia@gmail.com',
        'Female',
        '0123456789',
        '25 May,1977',
        'English',
        'Reading',
        'image_test.JPG',
        '1 RIDGE AVE SUFFERN',
        'NCR',
        'Delhi'
    )
