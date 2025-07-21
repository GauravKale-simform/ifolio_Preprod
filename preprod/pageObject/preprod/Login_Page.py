from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    Email_xpath = (By.XPATH,"//input[@id='email']")
    Password_xpath = (By.XPATH,"//input[@id='password']")
    SigninButton_xpath = (By.XPATH,"//button[@type='submit']")
    EmailErrorMessage_xpath = (By.XPATH,"//span[contains(text(),'Email is required.')]")
    ToastMessage_xpath = (By.XPATH, "//div[contains(@class, 'Toastify__toast-body')]")
    PasswordErrorMessage_xpath = (By.XPATH,"//span[contains(text(),'Password is required.')]")
    ErrorMessage_xpath = (By.XPATH,"//div[contains(text(),'Invalid Login or Password')]")

    def __init__(self,driver):
        self.driver = driver

    def enter_email(self,email):
        self.driver.find_element(*Login.Email_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*Login.Password_xpath).send_keys(password)

    def click_on_signin_button(self):
        self.driver.find_element(*Login.SigninButton_xpath).click()

    def get_toast_message(self):
        try:
            toast_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Login.ToastMessage_xpath))
            return toast_element.text
        except TimeoutException:
            return None












