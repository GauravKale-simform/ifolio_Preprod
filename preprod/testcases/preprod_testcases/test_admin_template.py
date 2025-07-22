from pageObject.preprod.Admin_Template import CreateTemplate

class TestCreateTemplate:
    def test_create_template(self,preprod_setup,preprod_account_test_data):
        self.driver = preprod_setup
        self.CT = CreateTemplate(self.driver)
        self.CT.wait_for_first_account_to_display()
        self.CT.click_on_templates()
        self.CT.create_new_ifolio()
        self.CT.select_ifolio(preprod_account_test_data['select_ifolio'])
        self.CT.click_on_continue()
        self.CT.rename_ifolio(preprod_account_test_data['rename_ifolio'])
        self.CT.back_to_admin()
        self.CT.verify_ifolio_in_admin_panel(preprod_account_test_data['rename_ifolio'])
        self.CT.delete_ifolio(preprod_account_test_data['rename_ifolio'])






