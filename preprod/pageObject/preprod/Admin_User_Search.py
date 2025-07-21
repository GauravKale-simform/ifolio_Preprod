import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserSearch:
    Search_Button_xpath = (By.XPATH, "//div[@class='sc-dcJsrY kvWFme']")
    Role_xapth = (By.XPATH,"//div[@id='mui-component-select-role_name']")
    Role_Dialog_box_xpath = (By.XPATH,"(//ul[@tabindex='-1'])[2]")
    Account_xpath = (By.XPATH,'(//input[@type="text"])[1]')
    Select_account_xpath = (By.XPATH,"(//div[@role='presentation'])[2]//div//ul//li[@data-option-index=0]")
    Firstname_xpath = (By.XPATH,"//input[@id='firstname']")
    Lastname_xpath = (By.XPATH,"//input[@id='lastname']")
    Email_xpath = (By.XPATH,"//input[@id='email']")
    Phone_xpath = (By.XPATH,"//input[@id='phone']")
    City_xapth = (By.XPATH,"//input[@id='city_name']")
    State_xpath = (By.XPATH,"//input[@id='state_name']")
    JobTitle_xpath = (By.XPATH,"//input[@id='job_title']")
    SearchButtonTitle_xpath = (By.XPATH, "//div[contains(text(),'Advanced Search')]")
    User_xpath = (By.XPATH, "//a[@href='/users']")

    SearchFinal_xpath = (By.XPATH,"//button[@type='submit']")
    Reset_xpath = (By.XPATH,"(//button[@type='button'])[5]")

    Loader_xpath = (By.XPATH,"//div[@role='progressbar']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click_on_user(self):
        self.driver.find_element(*UserSearch.User_xpath).click()

    def click_on_search_button(self):
        self.wait.until(EC.presence_of_element_located(UserSearch.Search_Button_xpath))
        time.sleep(1)
        search = self.wait.until(EC.element_to_be_clickable(UserSearch.Search_Button_xpath))
        search.click()
        self.wait.until(EC.visibility_of_element_located(UserSearch.SearchButtonTitle_xpath))

    def select_role(self,role_type):
        self.driver.find_element(*UserSearch.Role_xapth).click()
        self.wait.until(visibility_of_element_located(UserSearch.Role_Dialog_box_xpath))
        role_option = (By.XPATH, f"//li[normalize-space()='{role_type}']")
        element = self.wait.until(EC.element_to_be_clickable(role_option))
        element.click()

    def enter_account_name(self,name):
        self.driver.find_element(*UserSearch.Account_xpath).send_keys(name)
        account = self.wait.until(EC.element_to_be_clickable(UserSearch.Select_account_xpath))
        account.click()

    def enter_first_name(self,name):
        self.driver.find_element(*UserSearch.Firstname_xpath).send_keys(name)

    def enter_last_name(self,name):
        self.driver.find_element(*UserSearch.Lastname_xpath).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*UserSearch.Email_xpath).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(*UserSearch.Phone_xpath).send_keys(phone)

    def enter_city(self,city):
        self.driver.find_element(*UserSearch.Phone_xpath).send_keys(city)

    def enter_job_title(self,job):
        self.driver.find_element(*UserSearch.JobTitle_xpath).send_keys(job)

    def click_final_search(self):
        self.driver.find_element(*UserSearch.SearchFinal_xpath).click()

    def click_on_reset(self):
        self.driver.find_element(*UserSearch.Reset_xpath).click()

    def wait_for_progress_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(UserSearch.Loader_xpath))

    def scroll(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def terminate_search_opeartion(self):
        self.wait.until(EC.presence_of_element_located(UserSearch.Search_Button_xpath))
        time.sleep(1)
        search = self.wait.until(EC.element_to_be_clickable(UserSearch.Search_Button_xpath))
        search.click()

    def perform_search_and_reset(self):
        self.click_final_search()
        self.scroll(-300)
        self.wait_for_progress_to_disappear()
        self.click_on_reset()
        self.wait_for_progress_to_disappear()
        self.scroll(-300)


    #this is for email search functionality but as of now email,phone,city,state,job title search are not working on BETA.
    # self.SU.enter_email('lastname@first.com')
    # self.SU.click_final_search()
    # self.SU.scroll(-300)
    # time.sleep(10)
    # self.SU.wait_for_progress_to_disappear()
    # self.SU.click_on_reset()
























