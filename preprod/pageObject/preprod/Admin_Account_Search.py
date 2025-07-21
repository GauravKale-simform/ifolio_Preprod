import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchAccount:
    SearchButtonTitle_xpath = (By.XPATH, "//div[contains(text(),'Advanced Search')]")
    First_account_xpath = (By.XPATH, "//td[normalize-space()='IFOLIO Team']")
    Search_Button_xpath = (By.XPATH, "//div[@class='sc-dcJsrY kvWFme']")
    Account_xpath = (By.XPATH,"//input[@id='name']")
    FirstName_xpath = (By.XPATH,"//input[@id='settings->firstname']")
    LastName_xpath = (By.XPATH,"//input[@id='settings->lastname']")

    Solution_xpath = (By.XPATH,"(//div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input'])[1]")
    Enterprise_xpath = (By.XPATH,"//li[@data-value='enterprise']")
    Educator_xpath = (By.XPATH,"//li[@data-value='educator']")
    Sports_xpath = (By.XPATH,"//li[@data-value='sports']")
    Pro_xpath = (By.XPATH,"//li[@data-value='pro']")

    Payment_xpath = (By.XPATH,"(//div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input'])[2]")
    Online_Accounts_xpath = (By.XPATH,"//li[@data-value='1']")
    B2B_xpath = (By.XPATH,"//li[@data-value='0']")

    Email_xpath = (By.XPATH,"//input[@id='settings->email']")

    SearchFinal_xpath = (By.XPATH,"//button[@type='submit']")
    Reset_xpath = (By.XPATH,"(//button[@type='button'])[5]")

    Loader_xpath = (By.XPATH,"//div[@role='progressbar']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def wait_for_first_account_to_display(self):
        self.wait.until(EC.visibility_of_element_located(SearchAccount.First_account_xpath))

    def click_on_search_button(self):
        self.driver.find_element(*SearchAccount.Search_Button_xpath).click()

    def enter_account_name(self,name):
        self.wait.until(EC.visibility_of_element_located(SearchAccount.SearchButtonTitle_xpath))
        self.driver.find_element(*SearchAccount.Account_xpath).send_keys(name)

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(SearchAccount.SearchFinal_xpath)).click()

    def enter_first_name(self,name):
        self.driver.find_element(*SearchAccount.FirstName_xpath).send_keys(name)

    def enter_last_name(self,name):
        self.driver.find_element(*SearchAccount.LastName_xpath).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*SearchAccount.Email_xpath).send_keys(email)

    def scroll(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def click_on_reset(self):
        self.wait.until(EC.visibility_of_element_located(SearchAccount.Reset_xpath))
        self.driver.find_element(*SearchAccount.Reset_xpath).click()

    def wait_for_progress_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(SearchAccount.Loader_xpath))




