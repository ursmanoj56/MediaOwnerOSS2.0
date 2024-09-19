from PageObjects.TenantLogin import TenantLogin
from Tests.BaseTest import BaseTest


class TestCartPageConfig(BaseTest):
    def login(self):
        self.tenantlogin = TenantLogin(self.driver)
        self.choosetemplate = self.tenantlogin.validate_loginFunction_withValid_credential("manohar", "admin@123")
        self.pageconfiguration = self.choosetemplate.verify_whether_configurationPage_is_displayed_click_configButton()
        self.cartpageconfig = self.pageconfiguration.goto_CartPAge_configuration()

    def test_verify_Impression_element_when_configuration_disable(self):
        self.login()
        self.cartpageconfig.verify_Impression_element_when_configuration_disable()




