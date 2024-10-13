from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_buns_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 10)
    buns_element = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CONSTRUCTOR_BUNS)))
    driver.execute_script("arguments[0].click();", buns_element)
    assert "Булки" in driver.page_source

def test_sauces_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 10)
    sauces_element = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CONSTRUCTOR_SAUCES)))
    driver.execute_script("arguments[0].click();", sauces_element)
    assert "Соусы" in driver.page_source

def test_fillings_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 10)
    fillings_element = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CONSTRUCTOR_FILLINGS)))
    driver.execute_script("arguments[0].click();", fillings_element)
    assert "Начинки" in driver.page_source




