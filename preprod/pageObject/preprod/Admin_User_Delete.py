import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeleteUser:
    Search_Button_xpath = (By.XPATH, "//div[@class='sc-dcJsrY kvWFme']")
    SearchButtonTitle_xpath = (By.XPATH, "//div[contains(text(),'Advanced Search')]")
    Firstname_xpath = (By.XPATH, "//input[@id='firstname']")
    SearchFinal_xpath = (By.XPATH,"//button[@type='submit']")
    Reset_xpath = (By.XPATH,"(//button[@type='button'])[5]")

    Loader_xpath = (By.XPATH,"//div[@role='progressbar']")
    Select_user_xpath = (By.XPATH,'(//span[@class="MuiIconButton-label"])[6]') #//input[@aria-labelledby="enhanced-table-checkbox-0"]
    Delete_User_xpath = (By.XPATH,"//button[contains(text(),'Delete User')]")
    Ok_button_xpath = (By.XPATH, "//button[normalize-space()='Ok']")
    User_xpath = (By.XPATH, "//a[@href='/users']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click_on_search_button(self):
        self.wait.until(EC.presence_of_element_located(DeleteUser.Search_Button_xpath))
        time.sleep(1)
        search = self.wait.until(EC.element_to_be_clickable(DeleteUser.Search_Button_xpath))
        search.click()
        self.wait.until(EC.visibility_of_element_located(DeleteUser.SearchButtonTitle_xpath))

    def click_on_user(self):
        self.driver.find_element(*DeleteUser.User_xpath).click()

    def enter_first_name(self,name):
        self.driver.find_element(*DeleteUser.Firstname_xpath).send_keys(name)

    def click_final_search(self):
        self.driver.find_element(*DeleteUser.SearchFinal_xpath).click()

    def wait_for_progress_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(DeleteUser.Loader_xpath))

    def select_user(self):
        user_checkbox = self.wait.until(EC.element_to_be_clickable(DeleteUser.Select_user_xpath))
        user_checkbox.click()

    def terminate_search_opeartion(self):
        self.wait.until(EC.presence_of_element_located(DeleteUser.Search_Button_xpath))
        time.sleep(1)
        search = self.wait.until(EC.element_to_be_clickable(DeleteUser.Search_Button_xpath))
        search.click()

    def delete_user(self):
        self.driver.find_element(*DeleteUser.Delete_User_xpath).click()

    def click_ok_button(self):
        ok_button = self.wait.until(EC.element_to_be_clickable(DeleteUser.Ok_button_xpath))
        ok_button.click()
        time.sleep(3)

    def click_on_reset(self):
        self.driver.find_element(*DeleteUser.Reset_xpath).click()

    def scroll(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def perform_search_and_reset(self):
        self.click_final_search()
        self.scroll(-300)
        self.wait_for_progress_to_disappear()























