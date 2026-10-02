class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
    def click(self,locator):
        element = self.driver.find_element(*locator)
        element.click()

    def password_text(self,locator,password):
        element = self.driver.find_element(*locator)
        element.send_keys(password)
    def email_text(self,locator,email):
        element = self.driver.find_element(*locator)
        element.send_keys(email)