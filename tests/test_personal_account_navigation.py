import pytest
from locators import Locators

@pytest.mark.usefixtures("driver")
def test_navigate_to_personal_account(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

