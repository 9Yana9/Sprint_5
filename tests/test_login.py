import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_login_via_main_button(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        personal_account_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.PERSONAL_ACCOUNT_BUTTON)))
        personal_account_button.click()
        main_login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.MAIN_LOGIN_BUTTON)))
        main_login_button.click()
        self.assertIn("Вход", driver.title)

    def test_login_via_personal_account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        personal_account_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.PERSONAL_ACCOUNT_BUTTON)))
        personal_account_button.click()

        self.assertIn("Вход", driver.title)

    def test_login_via_registration_form(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        personal_account_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.PERSONAL_ACCOUNT_BUTTON)))
        personal_account_button.click()
        register_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.REGISTER_LINK)))
        register_link.click()
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.LOGIN_BUTTON)))
        login_button.click()

        self.assertIn("Вход", driver.title)

    def test_login_via_password_recovery(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.LOGIN_LINK)))
        login_link.click()
        self.assertIn("Вход", driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


