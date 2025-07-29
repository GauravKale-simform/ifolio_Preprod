import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UploadImage:
    IfolioStock_xapth = (By.XPATH,"//a[@href='/stock']")
    First_account_xpath = (By.XPATH, "//td[normalize-space()='IFOLIO Team']")
    Upload_Image_xpath = (By.XPATH,"(//input[@type='file'])[1]")
    Delete_Image_xpath = (By.XPATH,"(//div[@class='sc-hTUWRQ chBMJU'])[1]")
    Delete_Dialog_box_xpath = (By.XPATH,"//div[contains(text(),'Remove media')]")
    Ok_button_xpath = (By.XPATH,"//span[contains(text(),'Ok')]")
    Close_ToastMessage_xpath = (By.XPATH, "//button[@class='Toastify__close-button Toastify__close-button--success']")
    Loader_xpath = (By.XPATH, "//div[@role='progressbar']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click_on_templates(self):
        self.wait.until(EC.element_to_be_clickable(UploadImage.Close_ToastMessage_xpath)).click()
        self.wait.until(EC.visibility_of_element_located(UploadImage.First_account_xpath))
        self.wait.until(EC.element_to_be_clickable(UploadImage.IfolioStock_xapth)).click()
        self.wait.until(EC.invisibility_of_element_located(UploadImage.Loader_xpath))

    def upload_image(self):
        image_path = 'C://Users//gaurav//Downloads//simform_Google Search//10.jfif'
        self.driver.find_element(*UploadImage.Upload_Image_xpath).send_keys(image_path)
        self.wait.until(EC.invisibility_of_element_located(UploadImage.Loader_xpath))
        time.sleep(2)

    def wait_for_toast_message_to_disappear(self):
        self.wait.until(EC.element_to_be_clickable(UploadImage.Close_ToastMessage_xpath)).click()

    def delete_image(self):
        self.wait.until(EC.element_to_be_clickable(UploadImage.Delete_Image_xpath)).click()
        self.wait.until(EC.visibility_of_element_located(UploadImage.Delete_Dialog_box_xpath))
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(UploadImage.Ok_button_xpath)).click()
        self.wait.until(EC.invisibility_of_element_located(UploadImage.Close_ToastMessage_xpath))

