import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from locators import Locators

BASE_URL = "https://stellarburgers.nomoreparties.site"
LOGIN_URL = f"{BASE_URL}/login"
REGISTER_URL = f"{BASE_URL}/register"
FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_login_via_main_button(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    main_login_button = wait.until(EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON))
    main_login_button.click()
    assert driver.current_url == LOGIN_URL

def test_login_via_registration_form(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(REGISTER_URL)
    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_LINK))
    login_button.click()
    assert driver.current_url == LOGIN_URL

def test_login_via_password_recovery(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(FORGOT_PASSWORD_URL)
    login_link = wait.until(EC.element_to_be_clickable(Locators.LOGIN_LINK_2))
    login_link.click()
    assert driver.current_url == LOGIN_URL
