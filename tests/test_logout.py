from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"

def test_login_and_logout(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(LOGIN_URL)

    email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
    email_input.send_keys("yana_kivachickaya_11_222@yandex.ru")

    password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
    password_input.send_keys("123456")

    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    login_button.click()

    wait.until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON))

    account_button = wait.until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
    account_button.click()

    logout_button = wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
    logout_button.click()

    wait.until(EC.url_to_be(LOGIN_URL))
    assert driver.current_url == LOGIN_URL






