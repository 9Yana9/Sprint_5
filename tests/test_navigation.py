import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def login(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    wait = WebDriverWait(driver, 10)

    email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.EMAIL_INPUT)))
    email_input.send_keys("your_email@example.com")

    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.PASSWORD_INPUT)))
    password_input.send_keys("your_password")

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.LOGIN_BUTTON)))
    login_button.click()

@pytest.mark.usefixtures("driver")
def test_navigate_to_constructor(driver):
    login(driver)

    wait = WebDriverWait(driver, 10)
    constructor_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.CONSTRUCTOR_BUTTON))
    )
    constructor_button.click()

@pytest.mark.usefixtures("driver")
def test_navigate_via_logo(driver):
    login(driver)

    wait = WebDriverWait(driver, 20)
    logo = wait.until(
        EC.element_to_be_clickable((By.XPATH, Locators.LOGO_BUTTON))
    )
    logo.click()


