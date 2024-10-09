import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators


class TestLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_logout(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_EMAIL_FIELD).send_keys("test_testov1999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_PASSWORD_FIELD).send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_BUTTON).click()

        driver.find_element(By.CSS_SELECTOR, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, Locators.LOGOUT_BUTTON).click()
        self.assertIn("Вход", driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

