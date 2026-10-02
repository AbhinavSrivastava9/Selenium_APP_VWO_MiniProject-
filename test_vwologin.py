from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data import login_data
from login_page import LoginPage
import pytest
@pytest.mark.parametrize(
            "email,password",login_data
        )
def test_invalid_login(driver,email,password):
    login_page = LoginPage(driver)
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login()
    actual_message = login_page.get_error_message()
    expected_message = "Your email, password, IP address or location did not match"
    assert actual_message == expected_message


