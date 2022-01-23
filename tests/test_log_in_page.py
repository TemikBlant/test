import pytest
from pages import MainPage
from pages import LogInPage


@pytest.mark.parametrize('email, password', [('2345dsd@mdsad.com', 'pass')])
def test_login_with_non_existent_email(go_login_stackoverflow, email, password):
    _ = go_login_stackoverflow
    LogInPage(_).login(email, password)
    assert LogInPage(_).get_email_error_message() == 'The email or password is incorrect.',\
        "Отсутствует сообщение о неверном email"


@pytest.mark.parametrize('email, password', [('fsdjlkad', 'pass'), ('123456', 'pass'),
                                             ('2132mail.ru@', 'pass')])
def test_login_with_invalid_email(go_login_stackoverflow, email, password):
    _ = go_login_stackoverflow
    LogInPage(_).login(email, password)
    assert LogInPage(_).get_email_error_message() == 'The email is not a valid email address.',\
        "Отсутствует сообщение о неверном email"
