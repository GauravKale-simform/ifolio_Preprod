import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateTemplate:
    First_account_xpath = (By.XPATH, "//td[normalize-space()='IFOLIO Team']")
    Template_xpath = (By.XPATH,"//a[@href='/templates']")
    Loader_xpath = (By.XPATH, "//div[@role='progressbar']")
    CreateNew_Button_xpath = (By.XPATH,"//span[contains(text(),'Create new')]")
    Swipe_next_xpath = (By.XPATH, "//div[@class='swiper-button-next']")
    Swipe_previous_xpath = (By.XPATH, "//div[@class='swiper-button-prev']")
    Select_ifolio_xpath = (By.XPATH,"//div[div[text()='Automation']]//img") #this will be dynamic
    Continue_button_xpath = (By.XPATH, "//div[contains(text(), 'Continue')]")
    Name_of_ifolio = (By.XPATH, "//input[@maxlength='255']")
    BackToAdmin_xpath = (By.XPATH,"//div[contains(text(), 'Back to admin')]")
    TemplateName_xpath = (By.XPATH,"//input[@value='Automation']") #this will be dynamic
    Delete_confirmation_dialog_xpath = (By.XPATH,"//div[@class='sc-krNlru gpPELw']")
    Ok_Button_xpath = (By.XPATH,"//span[contains(text(),'Ok')]")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click_on_templates(self):
        self.wait.until(EC.visibility_of_element_located(CreateTemplate.First_account_xpath))
        Templates = self.wait.until(EC.element_to_be_clickable(CreateTemplate.Template_xpath))
        Templates.click()
        self.wait.until(EC.invisibility_of_element_located(CreateTemplate.Loader_xpath))

    def create_new_ifolio(self):
        Create_Button = self.wait.until(EC.element_to_be_clickable(CreateTemplate.CreateNew_Button_xpath))
        Create_Button.click()

    def select_ifolio(self, name):#Demo 1, New Template, Site, Digital Business Card, Event --> those are available on first page
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        ifolio_xpath = f"//div[div[text()='{name}']]//img[@alt='template']"
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, ifolio_xpath)))
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_continue(self):
        Continue_button = self.wait.until(EC.element_to_be_clickable(CreateTemplate.Continue_button_xpath))
        Continue_button.click()
        self.wait.until(EC.invisibility_of_element_located(CreateTemplate.Loader_xpath))
        time.sleep(3)

    def rename_ifolio(self,name):
        input_field = self.wait.until(EC.element_to_be_clickable(CreateTemplate.Name_of_ifolio))
        input_field.send_keys(Keys.CONTROL + "a")
        input_field.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        input_field.send_keys(name)

    def back_to_admin(self):
        admin_panel = self.wait.until(EC.element_to_be_clickable(CreateTemplate.BackToAdmin_xpath))
        admin_panel.click()

    def verify_ifolio_in_admin_panel(self,name):
        TemplateName_xpath = f"//input[@value='{name}']"
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,TemplateName_xpath)))

    def delete_ifolio(self,name):
        xpath = f"//input[contains(@value,'{name}')]/ancestor::div[4]//div[contains(@class,'sc-eBHhsj')]//span[contains(text(),'Delete')]"
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
        element.click()
        self.wait.until(EC.visibility_of_element_located(CreateTemplate.Delete_confirmation_dialog_xpath))
        ok = self.wait.until(EC.element_to_be_clickable(CreateTemplate.Ok_Button_xpath))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ok)
        ok.click()
        self.wait.until(EC.invisibility_of_element_located(CreateTemplate.Loader_xpath))
        time.sleep(2)

















