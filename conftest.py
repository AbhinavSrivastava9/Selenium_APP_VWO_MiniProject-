import pytest 
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    yield driver
    driver.quit()

