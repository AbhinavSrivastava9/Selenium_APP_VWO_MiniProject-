from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basepage import BasePage

class LoginPage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
    
    email_locator = (By.ID,"login-username")
    password_locator = (By.ID,"login-password")
    login_locator = (By.ID,"js-login-btn")

    def enter_email(self,email):
        self.email_text(self.email_locator,email)

    def enter_password(self,password):
        self.password_text(self.password_locator,password)

    def click_login(self):
        self.click(self.login_locator)

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 10)

        error_message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "js-notification-box-msg")
        )
    )

        return error_message.text
