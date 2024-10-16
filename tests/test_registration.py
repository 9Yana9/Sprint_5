import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

# Вынесенные переменные для URL
REGISTER_URL = "https://stellarburgers.nomoreparties.site/register"
LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"

@pytest.mark.usefixtures("driver")
class TestRegistration:

    def test_successful_registration(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(REGISTER_URL)
        driver.find_element(*Locators.REGISTER_NAME_FIELD).send_keys("Имя")
        driver.find_element(*Locators.REGISTER_EMAIL_FIELD).send_keys("yana_kivachickaya_11_222@yandex.ru")
        driver.find_element(*Locators.REGISTER_PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        wait.until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_registration_with_invalid_password(self, driver):
        driver.get(REGISTER_URL)
        driver.find_element(*Locators.REGISTER_NAME_FIELD).send_keys("Имя")
        driver.find_element(*Locators.REGISTER_EMAIL_FIELD).send_keys("yana_kivachickaya_11_888@yandex.ru")
        driver.find_element(*Locators.REGISTER_PASSWORD_FIELD).send_keys("123")  # Некорректный пароль
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        error_message = driver.find_element(*Locators.ERROR_MESSAGE).text
        assert error_message == "Некорректный пароль"