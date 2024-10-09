import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructorSections(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_buns_section(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        buns_element = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CONSTRUCTOR_BUNS)))
        driver.execute_script("arguments[0].click();", buns_element)
        self.assertIn("Булки", driver.page_source)

    def test_sauces_section(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        sauces_element = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CONSTRUCTOR_SAUCES)))
        driver.execute_script("arguments[0].click();", sauces_element)
        self.assertIn("Соусы", driver.page_source)

    def test_fillings_section(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        fillings_element = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CONSTRUCTOR_FILLINGS)))
        driver.execute_script("arguments[0].click();", fillings_element)
        self.assertIn("Начинки", driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



