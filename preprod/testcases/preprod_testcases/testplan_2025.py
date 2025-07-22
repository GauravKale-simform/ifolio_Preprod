import time
from datetime import datetime
from testcases.preprod_testcases.conftest import preprod_test_data

class Testplan2025:
    def test_name_campaign(self,preprod_setup,preprod_test_data,manager_flow):
        self.driver = preprod_setup
        self.MG = manager_flow
        today = datetime.now().strftime("%d_%B")
        campaign_name = f"Auto_Test_{today}"
        self.MG.name_campaign(campaign_name)
        saved_name = self.MG.get_campaign_name().strip()
        assert campaign_name == saved_name
        self.MG.select_ifolio(index=4)
        self.MG.deselect_message()
        self.MG.enter_message_email_field('This is Preprod Campaign automation')
        self.MG.scroll(300)
        self.MG.select_email_address(index=4)
        self.MG.upload_banner_image(4)
        self.MG.upload_avatar_image(5)
        self.MG.upload_signature_image(6)
        self.MG.scroll(200)
        self.MG.click_on_next_step()
        self.MG.upload_contact_list()
        self.MG.scroll(200)


