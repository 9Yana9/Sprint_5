# test_login_logout.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_login_and_logout(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.EMAIL_INPUT)))
    email_input.send_keys("your_email@example.com")

    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.PASSWORD_INPUT)))
    password_input.send_keys("your_password")

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.LOGIN_BUTTON)))
    login_button.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, Locators.ACCOUNT_BUTTON)))

    account_button = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.ACCOUNT_BUTTON)))
    account_button.click()

    logout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.LOGOUT_BUTTON)))
    logout_button.click()





