from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddUser:
    User_xpath = (By.XPATH,"//a[@href='/users']")
    Left_Add_User_xpath = (By.XPATH,"//button[normalize-space()='Add User']")

    It_Ace_Team_xpath = (By.XPATH, "//td[normalize-space()='IT Aces Team']")

    ContainerID_xpath = (By.XPATH,"//div[contains(text(),'Edit Information')]")

    Account_xpath = (By.XPATH,"(//input[@class='MuiInputBase-input MuiInput-input MuiAutocomplete-input MuiAutocomplete-inputFocused MuiInputBase-inputAdornedEnd'])[2]") #(//input[@type='text'])[10]
    Select_Account_xpath = (By.XPATH,"(//div[@role='presentation'])[3]//div//ul//li[@data-option-index=0]")
    Account_Clear_xpath = (By.XPATH,"(//button[@type='button'])[23]")

    FirstName_xpath = (By.XPATH,"(//input[@id='firstname'])[2]")
    LastName_xpath = (By.XPATH,"(//input[@id='lastname'])[2]")

    Email_xpath = (By.XPATH,"(//input[@id='email'])[2]")
    Phone_xpath = (By.XPATH,"(//input[@id='phone'])[2]")

    Address_City_xpath = (By.XPATH,"(//input[@class='MuiInputBase-input MuiInput-input MuiAutocomplete-input MuiAutocomplete-inputFocused MuiInputBase-inputAdornedEnd'])[3]") #(//input[@type='text'])[15]
    Select_Address_xpath = (By.XPATH,"(//div[@role='presentation'])[3]//div//ul//li[@data-option-index=0]")

    Job_Title_xpath = (By.XPATH,"(//input[@id='job_title'])[2]")
    SMS_Provider_xpath = (By.XPATH,"(//input[@id='sms_provider_phone'])")

    Manager_xpath = (By.XPATH,"(//input[@type='radio'])[2]")
    Admin_xpath = (By.XPATH,"(//input[@type='radio'])[3]")

    SaveButton_xpath = (By.XPATH,"(//button[@type='submit'])[2]")
    CancelButton_xpath = (By.XPATH,"(//button[@type='button'])[27]/span[contains(text(),'Cancel')]")

    First_User_xpath = (By.XPATH,"(//td[normalize-space()='admin'])[1]")
    Alert_xpath = (By.XPATH, "//div[@class='Toastify__toast-body']")

    ToastMessage_xpath = (By.XPATH, "//div[contains(@class, 'Toastify__toast-body')]")

    Loader_xpath = (By.XPATH,"//div[@role='progressbar']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,30)

    def click_on_user(self):
        Users = self.wait.until(EC.element_to_be_clickable(AddUser.User_xpath))
        Users.click()
        self.wait.until(EC.visibility_of_element_located(AddUser.First_User_xpath))

    def click_on_add_user(self):
        self.driver.find_element(*AddUser.Left_Add_User_xpath).click()
        self.wait.until(EC.visibility_of_element_located(AddUser.ContainerID_xpath))

    def select_account(self,account):
        self.driver.find_element(*AddUser.Account_xpath).send_keys(account)
        account = self.wait.until(EC.element_to_be_clickable(AddUser.Select_Account_xpath))
        account.click()

    def enter_first_name(self,name):
        self.driver.find_element(*AddUser.FirstName_xpath).send_keys(name)

    def enter_last_name(self,name):
        self.driver.find_element(*AddUser.LastName_xpath).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*AddUser.Email_xpath).send_keys(email)

    def enter_phone_number(self,number):
        self.driver.find_element(*AddUser.Phone_xpath).send_keys(number)

    def enter_address(self,address):
        self.driver.find_element(*AddUser.Address_City_xpath).send_keys(address)
        address = self.wait.until(EC.element_to_be_clickable(AddUser.Select_Address_xpath))
        address.click()

    def enter_job(self,job):
        self.driver.find_element(*AddUser.Job_Title_xpath).send_keys(job)

    def select_profile_role(self, role):
        role = role.lower()
        role_mapping = {"user": '//*[@id="dashboard-tabpanel-info"]/div/form/div/div[11]/div/label[1]/span[1]/span[1]',
                        "manager": '//*[@id="dashboard-tabpanel-info"]/div/form/div/div[11]/div/label[2]/span[1]/span[1]',
                        "admin": '//*[@id="dashboard-tabpanel-info"]/div/form/div/div[11]/div/label[3]/span[1]/span[1]'}
        role_xpath = role_mapping[role]
        radio_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, role_xpath)))
        radio_btn.click()

    def click_save_button(self):
        self.driver.find_element(*AddUser.SaveButton_xpath).click()

    def get_toast_message(self):
        try:
            toast_element = self.wait.until((EC.visibility_of_element_located(AddUser.ToastMessage_xpath)))
            return toast_element.text
        except TimeoutException:
            return None

    def wait_for_progress_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(AddUser.Loader_xpath))

















