import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeleteAccount:
    SearchButtonTitle_xpath = (By.XPATH, "//div[contains(text(),'Advanced Search')]")
    First_account_xpath = (By.XPATH, "//td[normalize-space()='IFOLIO Team']")
    Search_Button_xpath = (By.XPATH, "//div[@class='sc-dcJsrY kvWFme']")
    Email_xpath = (By.XPATH,"//input[@id='settings->email']")
    Checkbox_xpath = (By.XPATH,"//thead/tr[1]/th[1]/span[1]/span[1]/input[1]")
    Main_Menu_xpath = (By.XPATH,"//div[contains(text(),'MENU')]")
    Delete_button_xpath = (By.XPATH,"(//button[normalize-space()='Delete'])[1]")
    Delete_button_dialog_xpath = (By.XPATH,"//div[normalize-space()='Delete Accounts']")
    Ok_button_xpath = (By.XPATH,"//button[normalize-space()='Ok']")
    Accounted_selected_xpath = (By.XPATH,"//tr[@class='MuiTableRow-root jss97 jss99 MuiTableRow-hover Mui-selected']")

    ToastMessage_xpath = (By.XPATH, "//div[contains(@class, 'Toastify__toast-body')]")
    Loader_xpath = (By.XPATH, "//div[@role='progressbar']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def close_dropdown_of_search(self):
        self.driver.find_element(*DeleteAccount.Search_Button_xpath).click()
        self.wait.until(EC.visibility_of_element_located(DeleteAccount.Main_Menu_xpath))

    def enter_email(self,name):
        self.wait.until(EC.visibility_of_element_located(DeleteAccount.SearchButtonTitle_xpath))
        self.driver.find_element(*DeleteAccount.Email_xpath).send_keys(name)

    def wait_for_account_to_appear(self, account_name):
        account_xpath = f"//td[contains(text(), '{account_name}')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, account_xpath)))

    def clicked_on_account_to_be_deleted(self):
        self.driver.find_element(*DeleteAccount.Checkbox_xpath).click()

    def click_on_delete_button(self):
        self.driver.find_element(*DeleteAccount.Delete_button_xpath).click()

    def verify_delete_dialog_box(self):
        self.wait.until(EC.visibility_of_element_located(DeleteAccount.Delete_button_dialog_xpath))

    def click_ok_button(self):
        ok_button = self.wait.until(EC.element_to_be_clickable(DeleteAccount.Ok_button_xpath))
        ok_button.click()
        time.sleep(3)

    def get_toast_message(self):
        try:
            toast_element = self.wait.until((EC.visibility_of_element_located(DeleteAccount.ToastMessage_xpath)))
            return toast_element.text
        except TimeoutException:
            return None

    def wait_for_progress_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(DeleteAccount.Loader_xpath))







