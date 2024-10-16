import pytest
from locators import Locators

LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"

@pytest.mark.usefixtures("driver")
def test_navigate_to_personal_account(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    assert driver.current_url == LOGIN_URL