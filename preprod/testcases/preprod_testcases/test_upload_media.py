from preprod.pageObject.preprod.Admin_Upload_Image import UploadImage
from preprod.testcases.preprod_testcases.conftest import preprod_test_data

class TestUploadImage:
    def test_upload_image(self,preprod_setup,preprod_test_data):
        self.driver = preprod_setup
        self.UI = UploadImage(self.driver)
        self.UI.click_on_templates()
        self.UI.upload_image()
        self.UI.wait_for_toast_message_to_disappear()
        self.UI.delete_image()







