import pytest
from selenium.webdriver.common.by import By
from locators import Locators

@pytest.mark.usefixtures("driver")
class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_NAME_FIELD).send_keys("Имя")
        driver.find_element(By.XPATH, Locators.REGISTER_EMAIL_FIELD).send_keys("yana_kivachickaya_11_999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_PASSWORD_FIELD).send_keys("123456")
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()

    def test_registration_with_invalid_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_NAME_FIELD).send_keys("Имя")
        driver.find_element(By.XPATH, Locators.REGISTER_EMAIL_FIELD).send_keys("yana_kivachickaya_11_999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_PASSWORD_FIELD).send_keys("123")
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()

        error_message = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p").text
        assert error_message == "Некорректный пароль"


