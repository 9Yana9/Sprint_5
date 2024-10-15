import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

@pytest.mark.usefixtures("driver")
def test_login_via_main_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 10)
    main_login_button = wait.until(EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON))
    main_login_button.click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login_via_registration_form(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://stellarburgers.nomoreparties.site/register")
    login_button = wait.until(
        EC.element_to_be_clickable(Locators.LOGIN_LINK))
    login_button.click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login_via_password_recovery(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    login_link = wait.until(EC.element_to_be_clickable(Locators.LOGIN_LINK_2))
    login_link.click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
