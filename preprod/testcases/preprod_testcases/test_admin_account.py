import pytest
from selenium.webdriver import ActionChains, Keys
from preprod.pageObject.preprod.Admin_Account_Search import SearchAccount
from preprod.pageObject.preprod.Admin_Account_Add import AddAccount
from preprod.pageObject.preprod.Admin_Account_Delete import DeleteAccount
from preprod.utilities import excel_reader

class TestAddAccount:
    @pytest.mark.parametrize("account_type", ["Enterprise","Educator","Sports","Pro"])
    def test_add_account(self,preprod_setup,account_type,preprod_account_test_data):
        self.driver = preprod_setup
        self.AA = AddAccount(self.driver)
        account_name = f"{preprod_account_test_data['account_name']} {account_type}"
        self.AA.wait_for_first_account_to_display()
        self.AA.click_on_add_account()
        self.AA.select_account_type(account_type)
        self.AA.enter_account_name(account_name)
        self.AA.enter_contact_firstname(preprod_account_test_data['first_name'])
        self.AA.enter_contact_lastname(preprod_account_test_data['last_name'])
        self.AA.enter_contact_email(preprod_account_test_data['email'])
        self.AA.enter_contact_phone(preprod_account_test_data['phone'])
        self.AA.enter_term_year(preprod_account_test_data['term'])
        self.AA.scroll(200)
        self.AA.enter_ifolio_owner_name(preprod_account_test_data['iFOLIO_owner_name'])
        self.AA.enter_ifolio_owner_email(preprod_account_test_data['iFOLIO_owner_email'])
        self.AA.enter_renewal_date(preprod_account_test_data['renewal_date'])
        self.AA.enter_number_of_managers(preprod_account_test_data['number_of_managers'])
        self.AA.enter_number_of_users(preprod_account_test_data['number_of_users'])
        self.AA.select_plan_type(preprod_account_test_data['plan_type'])
        self.AA.click_on_email_bank()
        self.AA.enter_account_email_bank_value(preprod_account_test_data['plan_type'],preprod_account_test_data['account_email_bank_value'])
        self.AA.enter_user_email_bank_value(preprod_account_test_data['plan_type'],preprod_account_test_data['user_email_bank_value'])
        self.AA.enter_overage_email_price(preprod_account_test_data['overage_email_price'])
        self.AA.click_text_bank()
        self.AA.enter_account_text_bank_value(preprod_account_test_data['plan_type'],preprod_account_test_data['account_text_bank_value'])
        self.AA.enter_user_text_bank_value(preprod_account_test_data['plan_type'],preprod_account_test_data['user_text_bank_value'])
        self.AA.enter_overage_email_price(preprod_account_test_data['plan_type'])
        self.AA.click_on_limits()
        site_limit_account = preprod_account_test_data['site_limit_per_account']
        site_limit_user = preprod_account_test_data['site_limit_per_user']
        contact_limit_account = preprod_account_test_data['contact_limit_per_account']
        contact_limit_user = preprod_account_test_data['contact_limit_per_user']
        media_size = preprod_account_test_data['media_library_org']
        upload_media_size = preprod_account_test_data['media_library_myupload']
        self.AA.enter_details_in_limits(site_limit_account, site_limit_user, contact_limit_account, contact_limit_user,media_size, upload_media_size)
        services = preprod_account_test_data['services'].split(",")
        self.AA.select_services(services)
        if account_type == "Pro":
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        else:
            self.AA.click_on_save_button()

    def test_search_account(self,preprod_setup,preprod_account_test_data):
        self.driver = preprod_setup
        self.SA = SearchAccount(self.driver)
        self.SA.click_on_search_button()
        self.SA.enter_account_name(preprod_account_test_data['search_Account_name'])
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        self.SA.wait_for_progress_to_disappear()
        self.SA.click_on_reset()
        self.SA.scroll(-300)
        self.SA.wait_for_progress_to_disappear()
        self.SA.enter_first_name(preprod_account_test_data['search_First_name'])
        self.SA.click_search_button()
        self.SA.scroll(-300)
        self.SA.wait_for_progress_to_disappear()
        self.SA.click_on_reset()
        self.SA.scroll(-300)
        self.SA.wait_for_progress_to_disappear()
        self.SA.enter_last_name(preprod_account_test_data['search_Last_name'])
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        self.SA.wait_for_progress_to_disappear()
        self.SA.click_on_reset()
        self.SA.scroll(-300)
        self.SA.wait_for_progress_to_disappear()
        self.SA.enter_email(preprod_account_test_data['search_Email'])
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        self.SA.wait_for_progress_to_disappear()
        self.SA.click_on_reset()
        self.SA.scroll(-300)
        self.SA.wait_for_progress_to_disappear()
        self.SA.click_on_search_button()

    # def test_export_accounts(self,beta_setup):
    #     self.driver = beta_setup
    #     self.EA = ExportAccount(self.driver)
    #     self.EA.export_account_details()

    def test_delete_account(self,preprod_setup,preprod_account_test_data):
        self.driver = preprod_setup
        self.SA = SearchAccount(self.driver)
        self.DA = DeleteAccount(self.driver)
        self.SA.click_on_search_button()
        self.DA.enter_email(preprod_account_test_data['delete_email'])
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        self.DA.wait_for_account_to_appear(preprod_account_test_data['delete_email'])
        self.DA.clicked_on_account_to_be_deleted()
        self.DA.close_dropdown_of_search()
        self.DA.click_on_delete_button()
        self.DA.verify_delete_dialog_box()
        self.DA.click_ok_button()
        self.DA.wait_for_progress_to_disappear()
        assert self.DA.get_toast_message() == 'Accounts are deleted.'









