from pageObject.preprod.Admin_Template import CreateTemplate
from testcases.preprod_testcases.conftest import beta_test_data

class TestCreateTemplate:
    def test_create_template(self,beta_setup,beta_test_data):
        self.driver = beta_setup
        self.CT = CreateTemplate(self.driver)
        self.CT.click_on_templates()
        self.CT.create_new_ifolio()
        self.CT.select_ifolio(beta_test_data['select_ifolio'])
        self.CT.click_on_continue()
        self.CT.rename_ifolio(beta_test_data['rename_ifolio'])
        self.CT.back_to_admin()
        self.CT.verify_ifolio_in_admin_panel(beta_test_data['rename_ifolio'])
        self.CT.delete_ifolio(beta_test_data['rename_ifolio'])






