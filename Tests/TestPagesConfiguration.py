from PageObjects.TenantLogin import TenantLogin
from Tests.BaseTest import BaseTest


class TestPagesConfiguration(BaseTest):

    def test_verify_all_configuration_buttons_displayed(self):
        self.tenantlogin = TenantLogin(self.driver)
        self.choosetemplate = self.tenantlogin.validate_loginFunction_withValid_credential("manoj", "admin@123")
        pageconfiguration = self.choosetemplate.verify_whether_configurationPage_is_displayed_click_configButton()
        message =pageconfiguration.verify_all_configuration_buttons_displayed()
        message1 = pageconfiguration.verify_cartConfig_button_isDisplayed()
        message2 = pageconfiguration.verify_Myorder_Config_button_isDisplayed()
        message3 = pageconfiguration.verify_Property_det_Config_button_isDisplayed()
        message4 = pageconfiguration.verify_SearchPagr_Config_button_isDisplayed()
        message5 = pageconfiguration.verify_UserReg_Config_button_isDisplayed()
        message6 = pageconfiguration.verify_Terms_Cond_Config_button_isDisplayed()
        message7 = pageconfiguration.verify_Privacy_Poly_Config_button_isDisplayed()
        message8 = pageconfiguration.verify_Contact_Us_Config_button_isDisplayed()
        message9 = pageconfiguration.verify_Report_Config_button_isDisplayed()
        message10 = pageconfiguration.verify_Notify_Config_button_isDisplayed()
        message11 = pageconfiguration.verify_Assert_Config_button_isDisplayed()
        message12 = pageconfiguration.verify_Tech_Config_button_isDisplayed()
        assert (message is True or message1 is True or message2 is True or message3 is True or message4 is True or message5 is True or message6 is True or message7 is True or message8 is True or message9 is True or message10 is True or message11 is True or message12 is True)

    def test_verify_save_all_configuration_button_is_displayed(self):
        self.tenantlogin = TenantLogin(self.driver)
        self.choosetemplate = self.tenantlogin.validate_loginFunction_withValid_credential("manoj", "admin@123")
        pageconfiguration = self.choosetemplate.verify_whether_configurationPage_is_displayed_click_configButton()
        message =pageconfiguration.verify_save_all_configuration_button_is_displayed()
        assert message is True