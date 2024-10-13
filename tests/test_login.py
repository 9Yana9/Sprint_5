
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_login_via_main_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 10)
    personal_account_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.PERSONAL_ACCOUNT_BUTTON)))
    personal_account_button.click()
    main_login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.MAIN_LOGIN_BUTTON)))
    main_login_button.click()

def test_login_via_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 10)
    personal_account_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.PERSONAL_ACCOUNT_BUTTON)))
    personal_account_button.click()

def test_login_via_registration_form(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://stellarburgers.nomoreparties.site/register")
    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.LOGIN_BUTTON)))
    login_button.click()

def test_login_via_password_recovery(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.LOGIN_LINK)))
    login_link.click()
