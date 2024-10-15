from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_buns_section(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Булки']")))

    sauces_element = wait.until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_SAUCES))
    sauces_element.click()

    assert wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Соусы']")))

    buns_element = wait.until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUNS))
    buns_element.click()

    assert wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Булки']")))

def test_sauces_section(driver):
    wait = WebDriverWait(driver, 10)
    sauces_element = wait.until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_SAUCES))
    sauces_element.click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Соусы']")))

def test_fillings_section(driver):
    wait = WebDriverWait(driver, 10)
    fillings_element = wait.until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_FILLINGS))
    fillings_element.click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Начинки']")))




