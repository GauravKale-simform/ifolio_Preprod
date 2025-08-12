import time
from operator import index

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Manager:
    First_account_xpath = (By.XPATH, "//td[normalize-space()='IFOLIO Team']")
    Search_Button_xpath = (By.XPATH, "//div[@class='sc-dcJsrY kvWFme']")
    Account_xpath = (By.XPATH, "//input[@id='name']")
    Loader_xpath = (By.XPATH, "//div[@role='progressbar']")

    Simform_team_xpath = (By.XPATH, "//td[normalize-space()='Simform Team']")
    Simform_Team_Icon_xpath = (By.XPATH,"(//img[@alt='avatar'])[2]")
    Owner_with_login_xpath = (By.XPATH,"//span[contains(text(),'Owner Log in')]")
    ToastMessage_xpath = (By.XPATH, "//div[contains(@class, 'Toastify__toast-body')]")
    Close_ToastMessage_xpath = (By.XPATH, "//button[@class='Toastify__close-button Toastify__close-button--success']")
    Close_Error_ToastMessage_xpath = (By.XPATH,"//button[@class='Toastify__close-button Toastify__close-button--error']")

    Campaigns_xpath = (By.XPATH,"//a[@href='/campaigns']")
    Campaign_Name_xpath = (By.XPATH,"//input[@id='step1-ChooseIfolio-input-campaignName']")

    Ifolio_Drop_Down_xpath = (By.XPATH,"//div[@id='step1-ChooseIfolio-select-Ifolio']")
    Select_ifolio_xpath = (By.XPATH,"//li[starts-with(@id, 'step1-ChooseIfolio-option-ifolio-')]")

    Schedule_Now_xpath = (By.XPATH,"//span[contains(text(),'Schedule Now')]")

    Text_Message_Radio_Button_xpath = (By.XPATH,"//input[@id='step2-DeliveryMethod-radio-MMS']") #already selected we have to deselect
    Text_Message_xpath = (By.XPATH,"//textarea[@id='step2-EditTextMessage-input-message']")
    Emial_Message_xpath = (By.XPATH,"//textarea[@id='step2-EditMessageForEmail-input-message']")

    Email_Drop_Down_xpath = (By.XPATH,"//div[@id='step2-emailPreview-select-emailFrom']")
    Select_Email_xpath = (By.XPATH,"//li[starts-with(@id, 'step2-emailPreview-option-emailFrom-')]")

    Upload_Banner_Image_xpath = (By.XPATH,'//div[@class="sc-cRmqLi sc-aNeao iCwTYA hBROBW"]//button')
    Upload_Avatar_Image_xpath = (By.XPATH, '//div[@class="sc-cRmqLi sc-aNeao jlnGTw lTxoR"]//button')
    Upload_Signature_Image_xpath = (By.XPATH,'//div[@class="sc-cRmqLi sc-aNeao jlnGTw lTxoX"]//button')
    Upload_Image_Save_Button_xpath = (By.XPATH,"(//span[contains(text(),'Save')])[2]")
    Email_Preview_xpath = (By.XPATH,"//div[contains(text(),'Email Preview')]")
    Note_xpath = (By.XPATH,"//span[contains(text(),'NOTE:')]")

    Email_Message_xpath = (By.XPATH,"//textarea[@id='step2-EditMessageForEmail-input-message']")

    # Banner_CheckBox_xpath = (By.XPATH,"//input[@id='step2-emailPreview-checkbox-banner']")
    # Avatar_CheckBox_xpath = (By.XPATH,"//input[@id='step2-emailPreview-checkbox-avatar']")
    # Signature_CheckBox_xpath = (By.XPATH,"//input[@id='step2-emailPreview-checkbox-signatureImage']")

    Next_step_xpath = (By.XPATH,"//span[contains(text(),'Next Step')]")

    Upload_List_xpath = (By.XPATH, "//input[@type='file']")
    Schedule_xpath = (By.XPATH,"(//span[contains(text(),'Schedule')])[2]")
    Campaign_Sent_xpath = (By.XPATH,"//div[contains(text(),'Campaign Sent')]")
    Ok_Button_xpath = (By.XPATH,"//span[contains(text(),'Ok')]")
    Campaign_Scheduler_xpath = (By.XPATH,"//div[contains(text(),'Campaign Scheduler')]")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def select_account(self,name):
        self.wait.until(EC.visibility_of_element_located(self.First_account_xpath))
        self.wait.until(EC.element_to_be_clickable(self.Search_Button_xpath)).click()
        self.driver.find_element(*Manager.Account_xpath).send_keys(name)

    def wait_for_progress_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(self.Loader_xpath))

    def owner_with_login(self):
        self.wait.until(EC.visibility_of_element_located(self.Simform_team_xpath))
        self.wait.until(EC.element_to_be_clickable(Manager.Simform_Team_Icon_xpath)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(Manager.Owner_with_login_xpath)).click()

    def close_toast_message(self):
        self.wait.until(EC.element_to_be_clickable(self.Close_ToastMessage_xpath)).click()

    def name_campaign(self,name):
        self.wait_for_progress_to_disappear()
        self.wait.until(EC.element_to_be_clickable(Manager.Campaigns_xpath)).click()
        time.sleep(2)
        self.driver.find_element(*Manager.Campaign_Name_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, "//body").click()

    def get_campaign_name(self):
        return self.driver.find_element(*Manager.Campaign_Name_xpath).get_attribute("value")

    def select_ifolio(self, index):
        self.wait.until(EC.element_to_be_clickable(Manager.Ifolio_Drop_Down_xpath)).click()
        specific_option_xpath = (By.XPATH, f"//li[@id='step1-ChooseIfolio-option-ifolio-{index}']")
        self.wait.until(EC.element_to_be_clickable(specific_option_xpath)).click()
        self.driver.find_element(*Manager.Schedule_xpath).click()

    def deselect_message(self):
        self.driver.find_element(*Manager.Text_Message_Radio_Button_xpath).click()

    def enter_message_email_field(self,message):
        message_box = self.driver.find_element(*Manager.Email_Message_xpath)
        message_box.click()
        message_box.send_keys(Keys.HOME)
        message_box.send_keys(Keys.END)
        message_box.send_keys(message)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", message_box)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", message_box)
        time.sleep(1)

    def select_email_address(self,index):
        self.wait.until(EC.element_to_be_clickable(Manager.Email_Drop_Down_xpath)).click()
        specific_option_xpath = (By.XPATH, f"//li[@id='step2-emailPreview-option-emailFrom-{index}']")
        self.wait.until(EC.element_to_be_clickable(specific_option_xpath)).click()

    def upload_banner_image(self,position):
        self.driver.find_element(*Manager.Upload_Banner_Image_xpath).click()
        time.sleep(1)
        image = f"(//div[@class='sc-jgyXzG kVozjW']//div[@type='image'])[{position}]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH,image))).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(Manager.Upload_Image_Save_Button_xpath)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(Manager.Note_xpath)).click()

    def upload_avatar_image(self,position):
        self.driver.find_element(*Manager.Upload_Avatar_Image_xpath).click()
        time.sleep(1)
        image = f"(//div[@class='sc-jgyXzG kVozjW']//div[@type='image'])[{position}]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH,image))).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(Manager.Upload_Image_Save_Button_xpath)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(Manager.Note_xpath)).click()

    def upload_signature_image(self,position):
        self.driver.find_element(*Manager.Upload_Signature_Image_xpath).click()
        time.sleep(1)
        self.wait_for_all_images_to_load()
        image = f"(//div[@class='sc-jgyXzG kVozjW']//div[@type='image'])[{position}]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH,image))).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(Manager.Upload_Image_Save_Button_xpath)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(Manager.Note_xpath)).click()

    def click_on_next_step(self):
        self.driver.find_element(*Manager.Next_step_xpath).click()

    def upload_contact_list(self):
        self.wait.until(EC.element_to_be_clickable(self.Close_Error_ToastMessage_xpath)).click()
        file_path = r'C://Users//gaurav//Desktop//iFOLIO//Automation//ifolio_preprod//utilities//Campaign_Sharing.xlsx'
        upload_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.Upload_List_xpath))
        self.driver.execute_script("arguments[0].style.display = 'block';", upload_input)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.Upload_List_xpath))
        upload_input.send_keys(file_path)

    def scroll(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def wait_for_all_images_to_load(self):
        self.wait.until(lambda d: d.execute_script("""return Array.from(document.images).every(img => img.complete && img.naturalHeight > 0);"""))

    def schedule_campaign(self):
        self.wait.until(EC.element_to_be_clickable(self.Close_ToastMessage_xpath)).click()
        self.wait.until(EC.element_to_be_clickable(self.Schedule_xpath)).click()
        self.wait.until(EC.visibility_of_element_located(self.Campaign_Sent_xpath))
        self.wait.until(EC.element_to_be_clickable(self.Ok_Button_xpath)).click()
        self.wait.until(EC.visibility_of_element_located(self.Campaign_Scheduler_xpath))





































