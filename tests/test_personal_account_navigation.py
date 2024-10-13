# test_personal_account.py
from selenium.webdriver.common.by import By
from locators import Locators

def test_navigate_to_personal_account(driver):
    driver.find_element(By.CSS_SELECTOR, Locators.PERSONAL_ACCOUNT_BUTTON).click()


