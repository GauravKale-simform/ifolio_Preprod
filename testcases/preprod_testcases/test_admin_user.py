import datetime
from pageObject.preprod.Admin_User_Add import AddUser
from testcases.preprod_testcases.conftest import preprod_account_test_data
from pageObject.preprod.Admin_User_Search import UserSearch
from pageObject.preprod.Admin_User_Delete import DeleteUser

class TestAddUser:
    def test_add_user(self,preprod_setup,preprod_account_test_data):
        self.driver = preprod_setup
        self.AU = AddUser(self.driver)
        self.AU.click_on_user()
        self.AU.click_on_add_user()
        self.AU.select_account(preprod_account_test_data['select_Account'])
        self.AU.enter_first_name(preprod_account_test_data['user_First_Name'])
        self.AU.enter_last_name(preprod_account_test_data['user_Last_Name'])
        #addiging random email
        base_email = preprod_account_test_data['user_Email']
        username, domain = base_email.split('@')
        unique_id = datetime.datetime.now().strftime("%d%H%M%S")[-5:]
        unique_email = f"{username}+{unique_id}@{domain}"
        self.AU.enter_email(unique_email)

        self.AU.enter_phone_number(preprod_account_test_data['user_Phone'])
        self.AU.enter_address(preprod_account_test_data['user_Address'])
        self.AU.enter_job(preprod_account_test_data['user_Job'])
        self.AU.select_profile_role(preprod_account_test_data['user_Profile'])
        self.AU.click_save_button()
        self.AU.wait_for_progress_to_disappear()
        assert self.AU.get_toast_message() == 'New user created!'

    def test_search_user(self, preprod_setup, preprod_account_test_data):
        self.driver = preprod_setup
        self.SU = UserSearch(self.driver)
        self.SU.click_on_user()
        self.SU.click_on_search_button()
        roles = ["Super Admin", "Account Manager", "User"]
        for role in roles:
            self.SU.select_role(role)
            self.SU.click_final_search()
            self.SU.scroll(-300)
            self.SU.wait_for_progress_to_disappear()
            self.SU.click_on_reset()
            self.SU.wait_for_progress_to_disappear()
            self.SU.scroll(-00)
        self.SU.enter_account_name(preprod_account_test_data['select_Account'])
        self.SU.perform_search_and_reset()
        self.SU.enter_first_name(preprod_account_test_data['us_First_Name'])
        self.SU.perform_search_and_reset()
        self.SU.enter_last_name(preprod_account_test_data['us_Last_Name'])
        self.SU.perform_search_and_reset()
        self.SU.terminate_search_opeartion()

    def test_delete_user(self, preprod_setup, preprod_account_test_data):
        self.driver = preprod_setup
        # time.sleep(10)
        self.DU = DeleteUser(self.driver)
        self.DU.click_on_user()
        self.DU.click_on_search_button()
        self.DU.enter_first_name(preprod_account_test_data['user_First_Name'])
        self.DU.perform_search_and_reset()
        # time.sleep(10)
        self.DU.select_user()
        self.DU.terminate_search_opeartion()
        self.DU.delete_user()
        self.DU.click_ok_button()





















