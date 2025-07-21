import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExportAccount:
    Export_button_xpath = (By.XPATH,"//button[normalize-space()='Export']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def export_account_details(self):
        export = self.wait.until(EC.element_to_be_clickable(ExportAccount.Export_button_xpath))
        export.click()
        time.sleep(10)



