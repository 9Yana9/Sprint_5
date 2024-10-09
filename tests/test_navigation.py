import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators

class TestNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_navigate_to_personal_account(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        self.assertIn("Личный кабинет", driver.title)

    def test_navigate_to_constructor(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, Locators.LOGO_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, "a.constructor").click()
        self.assertIn("Конструктор", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()