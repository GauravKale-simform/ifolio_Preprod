import os
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GroupShare:
    SharingButton_xpath = (By.XPATH,"//div[@data-helper='sharing-container']")
    Group_ShareButton_xpath = (By.XPATH, "//div[@class='sc-qOiPt ljTWv']")
    Share_DialogBox_xpath = (By.XPATH, "//div[@class='sc-pdLXi cQeIQP']")
    Group_Share_DialogBox_xpath = (By.XPATH,"//div[@class='sc-pdLXi cQeIQP']")
    Campaign_Name_xpath = (By.XPATH,"(//input[@class='sc-fzowVh iTmWaE'])[1]")
    Upload_List_xpath = (By.XPATH,"//input[@type='file']")
    Message_xpath = (By.XPATH, "//textarea[@class='sc-plhlx bLAFyD']")
    Check_Image_xpath = (By.XPATH,"//div[@class='sc-pQfhO flsVnQ']")
    SendButton_xpath = (By.XPATH,"//div[contains(text(),'Send')]")
    SuccessfulEmailShare_xpath = (By.XPATH,"//div[@class='sc-fzqPZZ cXxVvQ']")
    OkButton_xpath = (By.XPATH,"//div[@class='sc-fznWqX kSkVGe']")

    def __init__(self,driver):
        self.driver = driver
        self.screenshot_directory = "C://Users//gaurav//Desktop//iFOLIO//Automation//iFOLIO_auto//ScreenShots//Email_Group_Share"

    def click_on_share_button(self):
        share = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(GroupShare.SharingButton_xpath))
        share.click()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(GroupShare.Share_DialogBox_xpath))

    def click_on_groupshare(self):
        groupshare = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(GroupShare.Group_ShareButton_xpath))
        groupshare.click()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(GroupShare.Group_Share_DialogBox_xpath))

    def upload_list(self):
        file_path = r'C://Users//gaurav//Desktop//iFOLIO//Automation//ifolio_preprod//utilities//groupshare.xlsx'
        # file_path = os.path.abspath("utilities/groupshare.xlsx")
        upload_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.Upload_List_xpath))
        self.driver.execute_script("arguments[0].style.display = 'block';", upload_input)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.Upload_List_xpath))
        upload_input.send_keys(file_path)

    # def upload_list(self):
    #     file_path = "/utilities/groupshare.xlsx"
    #     upload_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(GroupShare.Upload_List_xpath)        )
    #     self.driver.execute_script("arguments[0].style.display = 'block';", upload_input)
    #     time.sleep(2)
    #     upload_input.send_keys(file_path)

    def enter_message(self, message):
        message_box = self.driver.find_element(*GroupShare.Message_xpath)
        message_box.click()
        message_box.send_keys(Keys.HOME)
        message_box.send_keys(Keys.ARROW_DOWN)
        message_box.send_keys(Keys.END)
        message_box.send_keys(Keys.ENTER)
        message_box.send_keys(message)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", message_box)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", message_box)
        time.sleep(2)
        screenshot_path = os.path.join(self.screenshot_directory, "GroupShare.png")
        self.driver.save_screenshot(screenshot_path)

    def enter_campaign_name(self,name):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(GroupShare.Campaign_Name_xpath))
        self.driver.find_element(*GroupShare.Campaign_Name_xpath).send_keys(name)

    def click_send_button(self):
        self.driver.find_element(*GroupShare.SendButton_xpath).click()

    def verify_success_message(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(GroupShare.SuccessfulEmailShare_xpath))
        ok = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(GroupShare.OkButton_xpath))
        ok.click()





