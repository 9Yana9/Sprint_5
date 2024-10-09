import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

    def test_successful_registration(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_NAME_FIELD).send_keys("Имя")
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_EMAIL_FIELD).send_keys("yana_kivachickaya_11_999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_PASSWORD_FIELD).send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_BUTTON).click()
        self.assertIn("Успешно зарегистрирован", driver.page_source)

    def test_registration_with_invalid_password(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_NAME_FIELD).send_keys("Имя")
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_EMAIL_FIELD).send_keys("yana_kivachickaya_11_999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_PASSWORD_FIELD).send_keys("123")
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_BUTTON).click()
        self.assertIn("Пароль должен содержать минимум 6 символов", driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

