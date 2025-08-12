import os
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SingleShare:
    ContinueEditing_xpath = (By.XPATH,"//div[contains(text(),'Continue editing')]")
    SharingButton_xpath = (By.XPATH,"//div[@data-helper='sharing-container']")
    Share_DialogBox_xpath = (By.XPATH,"//div[@class='sc-pdLXi cQeIQP']")
    Name_xpath = (By.XPATH,"//input[@class='sc-fzowVh iTmWaE'][1]")
    Company_xpath = (By.XPATH,"(//input[@class='sc-fzowVh iTmWaE'])[2]")
    PhoneNumber_xpath = (By.XPATH,"(//input[@class='sc-fzowVh iTmWaE'])[3]")
    Email_xpath = (By.XPATH,"(//input[@class='sc-fzowVh iTmWaE'])[4]")
    Message_xpath = (By.XPATH,"//textarea[@class='sc-plhlx bLAFyD']")
    SendButton_xpath = (By.XPATH,"//div[contains(text(),'Send')]")
    SuccessfulEmailShare_xpath = (By.XPATH,"//div[@class='sc-fzqPZZ cXxVvQ']")
    OkButton_xpath = (By.XPATH,"//div[@class='sc-fznWqX kSkVGe']")

    def __init__(self,driver):
        self.driver = driver
        self.screenshot_directory = "C://Users//gaurav//Desktop//iFOLIO//Automation//iFOLIO_auto//ScreenShots//Email_Single_Share"

    def click_on_share_button(self):
        share = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(SingleShare.SharingButton_xpath))
        share.click()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(SingleShare.Share_DialogBox_xpath))

    def enter_name(self,name):
        self.driver.find_element(*SingleShare.Name_xpath).send_keys(name)

    def enter_company(self,company):
        self.driver.find_element(*SingleShare.Company_xpath).send_keys(company)

    def enter_phone_number(self,number):
        self.driver.find_element(*SingleShare.PhoneNumber_xpath).send_keys(number)

    def enter_email(self,email):
        self.driver.find_element(*SingleShare.Email_xpath).send_keys(email)

    def enter_message(self, message):
        message_box = self.driver.find_element(*SingleShare.Message_xpath)
        message_box.click()
        message_box.send_keys(Keys.HOME)
        message_box.send_keys(Keys.ARROW_DOWN)
        message_box.send_keys(Keys.END)
        message_box.send_keys(Keys.ENTER)
        message_box.send_keys(message)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", message_box)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", message_box)
        time.sleep(2)
        screenshot_path = os.path.join(self.screenshot_directory, "SingleShare.png")
        self.driver.save_screenshot(screenshot_path)

    def click_on_send(self):
        self.driver.find_element(*SingleShare.SendButton_xpath).click()

    def scroll(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def verify_success_message(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(SingleShare.SuccessfulEmailShare_xpath))
        ok = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(SingleShare.OkButton_xpath))
        ok.click()






