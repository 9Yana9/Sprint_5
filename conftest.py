import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()