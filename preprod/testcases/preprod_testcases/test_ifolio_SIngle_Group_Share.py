from pageObject.preprod.ifolio_Single_Share import SingleShare
from pageObject.preprod.ifolio_Group_Share import GroupShare

class TestIfolio:
    def test_single_share(self, preprod_user_setup, preprod_test_data):
        self.driver = preprod_user_setup
        self.SS = SingleShare(self.driver)
        self.SS.click_on_share_button()
        self.SS.enter_name(preprod_test_data['Single_Share_Name'])
        self.SS.enter_company(preprod_test_data['Single_Share_Company'])
        self.SS.enter_email(preprod_test_data['Single_Share_Email'])
        self.SS.enter_message(preprod_test_data['Email_message'])
        self.SS.scroll(400)
        self.SS.click_on_send()
        self.SS.verify_success_message()

    def test_group_share(self,preprod_user_setup,preprod_test_data):
        self.driver = preprod_user_setup
        self.GS = GroupShare(self.driver)
        self.GS.click_on_share_button()
        self.GS.click_on_groupshare()
        self.GS.upload_list()
        self.GS.enter_campaign_name(preprod_test_data['Campaign_name'])
        self.GS.enter_message(preprod_test_data['Group_message'])
        self.GS.click_send_button()
        self.GS.verify_success_message()









