from PageObjects.TenantLogin import TenantLogin
from Tests.BaseTest import BaseTest


class TestChooseTemplate(BaseTest):
    def test_validate_Templates_displayed(self):
        self.tenantlogin = TenantLogin(self.driver)
        choosetemplate = self.tenantlogin.validate_loginFunction_withValid_credential("manoj", "admin@123")
        message =choosetemplate.validate_Templates_displayed()
        assert message is True

    def test_Verfy_whether_previewPage_is_displayed_click_Preview(self):
        self.tenantlogin = TenantLogin(self.driver)
        choosetemplate = self.tenantlogin.validate_loginFunction_withValid_credential("manoj", "admin@123")
        message =choosetemplate.Verfy_whether_previewPage_is_displayed_click_Preview()
        return message is True

    def test_verify_whether_configurationPage_is_displayed_click_configButton(self):
        self.tenantlogin = TenantLogin(self.driver)
        self.choosetemplate = self.tenantlogin.validate_loginFunction_withValid_credential("manoj", "admin@123")
        pageconfiguration = self.choosetemplate.verify_whether_configurationPage_is_displayed_click_configButton()
        message =pageconfiguration.validate_configurationPage_URL()
        assert message.__contains__("http://164.52.223.30:8001/form_io/")


