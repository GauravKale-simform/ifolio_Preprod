import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddAccount:
    First_account_xpath = (By.XPATH,"//td[normalize-space()='IFOLIO Team']")
    Add_Account_xpath = (By.XPATH, "//button[normalize-space()='Add Account']")
    ContainerId_xpath = (By.XPATH, "//div[@role='dialog']")
    Account_Type_Dropdown_xpath = (By.XPATH, "(//div[@class='MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-fullWidth MuiInput-fullWidth MuiInputBase-formControl MuiInput-formControl'])[7]")  # Ensure correct XPath
    AccountName_xpath = (By.XPATH, "(//input[@id='name'])[2]")
    ContactFirstName_xpath = (By.XPATH, "//input[@id='firstname']")
    ContactLastName_xpath = (By.XPATH,"//input[@id='lastname']")
    ContactEmail_xpath = (By.XPATH,"//input[@id='email']")
    ContactPhone_xpath = (By.XPATH, "//input[@id='phone']")
    TermYear_xpath = (By.XPATH, "//input[@id='term']")
    ifolioOwnerName_xpath = (By.XPATH, "//input[@id='owner_name']")
    ifolioOwnerEmail_xpath = (By.XPATH, "//input[@id='owner_email']")
    Renewal_date_xpath = (By.XPATH,"//input[@id='exp_year']")
    NumberofManagers_xpath = (By.XPATH,"//input[@id='number_of_admins']")
    NumberofUsers_xpath = (By.XPATH,"//input[@id='number_of_users']")

    MessagingServiceID_xpath = (By.XPATH,"//input[@id='twilio_messaging_service_id']")
    CheckButton_xpath = (By.XPATH,"//span[contains(text(),'Check')]")

    Left_Email_Bank = (By.XPATH, "//a[@href='/accounts#section2']")
    AccountEmailBankPerMonth_xpath = (By.XPATH,"//input[@id='account_email_bank_per_month']")
    UserEmailBankPerMonth_xpath = (By.XPATH,"//input[@id='user_email_bank_per_month']")
    OverageEmailPrice_xpath = (By.XPATH,"//input[@id='overage_email_price']")
    AccountEmailBankPerYear_xpath = (By.XPATH, "//input[@id='account_email_bank_per_year']")
    UserEmailBankPerYear_xpath = (By.XPATH, "//input[@id='user_email_bank_per_year']")

    Left_Text_Bank = (By.XPATH,"//a[@href='/accounts#section3']")
    AccountTextBankPerMonth_xpath = (By.XPATH,"//input[@id='account_text_bank_per_month']")
    UserTextBankPerMonth_xpath = (By.XPATH,"//input[@id='user_text_bank_per_month']")
    OverageTextPrice_xpath = (By.XPATH,"//input[@id='overage_text_price']")
    AccountTextBankPerYear_xpath = (By.XPATH, "//input[@id='account_text_bank_per_year']")
    UserTextBankPerYear_xpath = (By.XPATH, "//input[@id='user_text_bank_per_year']")

    Left_Limits = (By.XPATH,"//a[@href='/accounts#section4']")
    SiteLimitPerAccount_xpath = (By.XPATH,"//input[@id='ifolio_limit']")
    SiteLimitPerUser_xpath = (By.XPATH,"//input[@id='ifolio_per_user_limit']")
    ContactLimitForAccount_xpath = (By.XPATH,"//input[@id='contact_limit_per_account']")
    ContactLimitForUsers_xpath = (By.XPATH,"//input[@id='contact_limit_per_user']")
    MediaSize_xpath = (By.XPATH,"//input[@id='media_library_size_limit_per_account']")
    UploadMediaSize_xpath = (By.XPATH,"//input[@id='media_library_size_limit_per_user']")

    AnimatedChartsCheckBox_xpath = (By.XPATH,"//input[@name='has_animated_charts']")
    SubAccountsCheckBox_xpath = (By.XPATH,"//input[@name='has_subaccounts']")
    ManagerAnalyticsCheckBox_xpath = (By.XPATH,"//input[@name='has_manager_analytics']")
    IconLibraryCheckBox_xpath = (By.XPATH,"//input[@name='has_icon_library']")
    LinkPersonalizationCheckBox_xpath = (By.XPATH,"//input[@name='can_personilize_link']")
    UserAnalyticsCheckBox_xpath = (By.XPATH,"//input[@name='has_user_analytics']")
    MediaStockLibraryCheckBox_xpath = (By.XPATH,"//input[@name='has_ifolio_stock_library']")
    CustomURLCheckBox_xpath = (By.XPATH,"//input[@name='has_custom_urls']")
    TwoWayMessagingCheckBox_xpath = (By.XPATH,"//input[@name='has_two_way_messaging']")
    MediaOrgLibraryCheckBox_xpath = (By.XPATH,"//input[@name='has_org_media_library']")
    GroupShareCheckBox_xpath = (By.XPATH,"//input[@name='has_group_sharing']")
    EmailSignButtonCheckBox_xpath = (By.XPATH,"//input[@name='has_email_signature_buttons']")
    CustomTemplates_xpath = (By.XPATH,"//input[@name='has_custom_templates']")
    CampaignAppCheckBox_xpath = (By.XPATH,"//input[@name='has_campaign_app']")
    NavBarCreatorCheckBox_xpath = (By.XPATH,"//input[@name='navbar_creator']")
    HideShareButtonCheckBox_xpath = (By.XPATH,"//input[@name='hide_sharing']")
    HidePoweredByIfolioCheckBox_xpath = (By.XPATH,"//input[@name='hide_powered_by_ifolio']")
    EnableRedirects_xpath = (By.XPATH,"//input[@name='is_redirects_enabled']")

    Loader_xpath = (By.XPATH,"//div[@role='progressbar']")

    UploadImage_xpath = (By.XPATH,"//img[@class='sc-fulCBj wnlqA']")
    ToastMessage_xpath = (By.XPATH, "//div[contains(@class, 'Toastify__toast-body')]")

    CloseAddAddountWindow_xpath = (By.XPATH,"//div[@class='sc-bVVIoq jIJVCe']")

    SaveButton_xpath = (By.XPATH,"(//button[@type='submit'])[2]")
    CancelButton_xpath = (By.XPATH,"(//button[@type='button'])[17]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def wait_for_first_account_to_display(self):
        self.wait.until(EC.visibility_of_element_located(AddAccount.First_account_xpath))

    def click_on_add_account(self):
        add_account = self.wait.until(EC.element_to_be_clickable(AddAccount.Add_Account_xpath))
        add_account.click()

    def select_account_type(self, account_type):
        self.wait.until(EC.visibility_of_element_located(AddAccount.ContainerId_xpath))
        time.sleep(1)
        Account_Option_xpath = f"//li[normalize-space()='{account_type}']"
        dropdown = self.wait.until(EC.element_to_be_clickable(AddAccount.Account_Type_Dropdown_xpath))
        self.driver.execute_script("arguments[0].scrollIntoView();", dropdown)
        self.wait.until(EC.element_to_be_clickable(dropdown))
        dropdown.click()
        option_xpath = (By.XPATH, Account_Option_xpath)
        option = self.wait.until(EC.visibility_of_element_located(option_xpath))
        self.driver.execute_script("arguments[0].scrollIntoView();", option)
        option.click()

    def enter_account_name(self,name):
        account_name = self.wait.until(EC.visibility_of_element_located(AddAccount.AccountName_xpath))
        account_name.send_keys(name)

    def enter_contact_firstname(self,fname):
        self.driver.find_element(*AddAccount.ContactFirstName_xpath).send_keys(fname)

    def enter_contact_lastname(self,lname):
        self.driver.find_element(*AddAccount.ContactLastName_xpath).send_keys(lname)

    def enter_contact_email(self,email):
        self.driver.find_element(*AddAccount.ContactEmail_xpath).send_keys(email)

    def enter_contact_phone(self,phone):
        self.driver.find_element(*AddAccount.ContactPhone_xpath).send_keys(phone)

    def enter_term_year(self,year):
        self.driver.find_element(*AddAccount.TermYear_xpath).send_keys(year)

    def enter_ifolio_owner_name(self,name):
        self.driver.find_element(*AddAccount.ifolioOwnerName_xpath).send_keys(name)

    def enter_ifolio_owner_email(self,email):
        self.driver.find_element(*AddAccount.ifolioOwnerEmail_xpath).send_keys(email)

    def enter_renewal_date(self,date):
        self.driver.find_element(*AddAccount.Renewal_date_xpath).send_keys(date)

    def enter_number_of_managers(self,mnumber):
        self.driver.find_element(*AddAccount.NumberofManagers_xpath).send_keys(mnumber)

    def enter_number_of_users(self,number):
        self.driver.find_element(*AddAccount.NumberofUsers_xpath).send_keys(number)

    def select_plan_type(self, plan_type):
        plan_xpath = (By.XPATH, f"(//input[@name='plan_is_annual'])[{'1' if plan_type.lower() == 'annual' else '2'}]")
        self.driver.find_element(*plan_xpath).click()

    def click_on_email_bank(self):
        self.driver.find_element(*AddAccount.Left_Email_Bank).click()

    def enter_account_email_bank_value(self, plan_type, value):
        if plan_type.lower() == 'annual':
            email_bank_xpath = AddAccount.AccountEmailBankPerYear_xpath
        else:
            email_bank_xpath = AddAccount.AccountEmailBankPerMonth_xpath
        email_bank_field = self.driver.find_element(*email_bank_xpath)
        email_bank_field.clear()
        email_bank_field.send_keys(value)

    def enter_user_email_bank_value(self,plan_type,value):
        if plan_type.lower() == 'annual':
            email_bank_xpath = AddAccount.UserEmailBankPerYear_xpath
        else:
            email_bank_xpath = AddAccount.UserEmailBankPerMonth_xpath
        email_bank_field = self.driver.find_element(*email_bank_xpath)
        email_bank_field.clear()
        email_bank_field.send_keys(value)

    def enter_overage_email_price(self,price):
        self.driver.find_element(*AddAccount.OverageEmailPrice_xpath).send_keys(price)

    def click_text_bank(self):
        self.driver.find_element(*AddAccount.Left_Text_Bank).click()

    def enter_account_text_bank_value(self,plan_type,value):
        if plan_type.lower() == 'annual':
            email_bank_xpath = AddAccount.AccountTextBankPerYear_xpath
        else:
            email_bank_xpath = AddAccount.AccountTextBankPerMonth_xpath
        email_bank_field = self.driver.find_element(*email_bank_xpath)
        email_bank_field.clear()
        email_bank_field.send_keys(value)

    def enter_user_text_bank_value(self,plan_type,value):
        if plan_type.lower() == 'annual':
            email_bank_xpath = AddAccount.UserTextBankPerYear_xpath
        else:
            email_bank_xpath = AddAccount.UserTextBankPerMonth_xpath
        email_bank_field = self.driver.find_element(*email_bank_xpath)
        email_bank_field.clear()
        email_bank_field.send_keys(value)

    def click_on_limits(self):
        self.driver.find_element(*AddAccount.Left_Limits).click()

    def enter_details_in_limits(self, site_limit_account, site_limit_user, contact_limit_account, contact_limit_user,media_size, upload_media_size):
        self.driver.find_element(*AddAccount.SiteLimitPerAccount_xpath).send_keys(site_limit_account)
        self.driver.find_element(*AddAccount.SiteLimitPerUser_xpath).send_keys(site_limit_user)
        self.driver.find_element(*AddAccount.ContactLimitForAccount_xpath).send_keys(contact_limit_account)
        self.driver.find_element(*AddAccount.ContactLimitForUsers_xpath).send_keys(contact_limit_user)
        self.driver.find_element(*AddAccount.MediaSize_xpath).send_keys(media_size)
        self.driver.find_element(*AddAccount.UploadMediaSize_xpath).send_keys(upload_media_size)

    def select_services(self, services):
        service_mapping = {"AnimatedCharts": self.AnimatedChartsCheckBox_xpath,"SubAccounts": self.SubAccountsCheckBox_xpath,
            "ManagerAnalytics": self.ManagerAnalyticsCheckBox_xpath,"IconLibrary": self.IconLibraryCheckBox_xpath,
            "LinkPersonalization": self.LinkPersonalizationCheckBox_xpath,"UserAnalytics": self.UserAnalyticsCheckBox_xpath,
            "MediaStockLibrary": self.MediaStockLibraryCheckBox_xpath,"CustomURL": self.CustomURLCheckBox_xpath,
            "TwoWayMessaging": self.TwoWayMessagingCheckBox_xpath,"MediaOrgLibrary": self.MediaOrgLibraryCheckBox_xpath,
            "GroupShare": self.GroupShareCheckBox_xpath,"EmailSignButton": self.EmailSignButtonCheckBox_xpath,
            "CustomTemplates": self.CustomTemplates_xpath,"CampaignApp": self.CampaignAppCheckBox_xpath,
            "NavBarCreator": self.NavBarCreatorCheckBox_xpath,"HideShareButton": self.HideShareButtonCheckBox_xpath,
            "HidePoweredByIfolio": self.HidePoweredByIfolioCheckBox_xpath,"EnableRedirects": self.EnableRedirects_xpath}
        for service in services:
            checkbox_xpath = service_mapping.get(service)
            if checkbox_xpath:
                checkbox = self.driver.find_element(*checkbox_xpath)
                if not checkbox.is_selected():
                    checkbox.click()

    def scroll(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def click_on_save_button(self):
        self.driver.find_element(*AddAccount.SaveButton_xpath).click()
        time.sleep(3)

    def wait_for_toast_message_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(AddAccount.ToastMessage_xpath))





