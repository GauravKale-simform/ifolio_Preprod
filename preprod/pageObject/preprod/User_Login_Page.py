from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class User_Login:
    Email_xpath = (By.XPATH,"//input[@placeholder='Username']")
    Password_xpath = (By.XPATH,"//input[@placeholder='Password']")
    SigninButton_xpath = (By.XPATH,"//div[@class='sc-fznWqX iacghj']")
    EmailErrorMessage_xpath = (By.XPATH,"//div[contains(text(),'username field is required')]")
    ToastMessage_xpath = (By.XPATH, "//div[contains(@class, 'Toastify__toast-body')]")
    PasswordErrorMessage_xpath = (By.XPATH,"//div[contains(text(),'password field is required')]")
    ErrorMessage_xpath = (By.XPATH,"//div[contains(text(),'Invalid Login or Password')]")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,30)

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(User_Login.Email_xpath))
        self.driver.find_element(*User_Login.Email_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*User_Login.Password_xpath).send_keys(password)

    def click_on_signin_button(self):
        self.driver.find_element(*User_Login.SigninButton_xpath).click()

    def get_toast_message(self):
        try:
            toast_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(User_Login.ToastMessage_xpath))
            return toast_element.text
        except TimeoutException:
            return None















