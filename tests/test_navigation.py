import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

BASE_URL = "https://stellarburgers.nomoreparties.site/"
LOGIN_URL = f"{BASE_URL}login"

def login(driver):
    driver.get(LOGIN_URL)
    wait = WebDriverWait(driver, 10)

    email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
    email_input.send_keys("your_email@example.com")

    password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
    password_input.send_keys("your_password")

    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    login_button.click()

    personal_account_button = wait.until(EC.presence_of_element_located(Locators.ACCOUNT_BUTTON))

    assert personal_account_button.is_displayed(), "Кнопка 'Личный Кабинет' не найдена на странице"

@pytest.mark.usefixtures("driver")
def test_navigate_to_constructor(driver):
    login(driver)

    wait = WebDriverWait(driver, 10)
    constructor_button = wait.until(
        EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
    )
    constructor_button.click()

    assert driver.current_url == BASE_URL

@pytest.mark.usefixtures("driver")
def test_navigate_via_logo(driver):
    driver.get(LOGIN_URL)
    wait = WebDriverWait(driver, 20)
    logo = wait.until(EC.element_to_be_clickable(Locators.LOGO_BUTTON))
    logo.click()

    wait.until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL



