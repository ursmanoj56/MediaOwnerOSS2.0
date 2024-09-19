from PageObjects.TenantLogin import TenantLogin
from Tests.BaseTest import BaseTest


class TestMyCampaignConfig(BaseTest):
    def login(self):
        self.tenantlogin = TenantLogin(self.driver)
        self.choosetemplate = self.tenantlogin.validate_loginFunction_withValid_credential("manohar", "admin@123")
        self.pageconfiguration = self.choosetemplate.verify_whether_configurationPage_is_displayed_click_configButton()
        self.mycampaignconfig = self.pageconfiguration.goto_Property_Mycampaign_config()

    def test_verify_default_enble_toggle_options_are_Checked_disable_in_Mycampaign(self):
        self.login()
        message = self.mycampaignconfig.verify_default_enble_toggle_options_are_Checked_disable_in_Mycampaign()
        message1 = self.mycampaignconfig.verfy_SearchBar_is_Checked()
        message2 = self.mycampaignconfig.verfy_Custamised_Table_is_Checked()
        message3 = self.mycampaignconfig.verify_FilterDropDown_is_disable()
        message4 = self.mycampaignconfig.verify_SearchBar_is_disable()
        message5 = self.mycampaignconfig.verify_CustamisedTable_is_disable()
        assert (message is True and message1 is True and message2 is True and message3 is True and message4 is True and message5 is True)

    def test_verify_Alldefault_enable_checked_elements_is_Displayed_in_Mycampaign(self):
        self.login()
        message = self.mycampaignconfig.verify_Alldefault_enable_checked_elements_is_Displayed_in_Mycampaign("surrendar_bigoutdoor","Test123")
        message1 = self.mycampaignconfig.verify_SearchBar_is_Displayed()
        message2 = self.mycampaignconfig.verify_CustamisedTable_is_Displayed()
        assert (message is True and message1 is True and message2 is True)

    def test_verify_Creative_option_when_configuration_disable(self):
        self.login()
        self.mycampaignconfig.verify_Creative_option_when_configuration_disable("surrendar_bigoutdoor","Test123")
        message = self.mycampaignconfig.creatives_is_displayed("LIVE")
        message1 = self.mycampaignconfig.creatives_is_displayed("APPROVED")
        assert ("Creatives" not in message and "Creatives" not in message1 )



    def test_verify_Creative_option_when_configuration_enable(self):
        self.login()
        self.mycampaignconfig.verify_Creative_option_when_configuration_disable("surrendar_bigoutdoor","Test123")
        message = self.mycampaignconfig.creatives_is_displayed("LIVE")
        message1 = self.mycampaignconfig.creatives_is_displayed("APPROVED")
        assert ("Creatives" in message and "Creatives" in message1 )

    def test_verify_DeliveryReport_option_when_configuration_disable(self):
        self.login()
        self.mycampaignconfig.verify_DeliveryReport_option_when_configuration_disable("surrendar_bigoutdoor", "Test123")
        message = self.mycampaignconfig.creatives_is_displayed("LIVE")
        assert ("Delivery Report" not in message)

    def test_verify_DeliveryReport_option_when_configuration_enable(self):
        self.login()
        self.mycampaignconfig.verify_DeliveryReport_option_when_configuration_disable("surrendar_bigoutdoor", "Test123")
        message = self.mycampaignconfig.creatives_is_displayed("LIVE")
        assert ("Delivery Report" in message)

    def test_verify_PaymentInvoice_option_when_configuration_disable(self):
        self.login()
        self.mycampaignconfig.verify_PaymentInvoice_option_when_configuration_disable("surrendar_bigoutdoor", "Test123")
        message = self.mycampaignconfig.creatives_is_displayed("LIVE")
        message1 = self.mycampaignconfig.creatives_is_displayed("APPROVED")
        assert ("Payment" not in message and " Payment" not in message1)

    def test_verify_PaymentInvoice_option_when_configuration_enable(self):
        self.login()
        self.mycampaignconfig.verify_PaymentInvoice_option_when_configuration_disable("surrendar_bigoutdoor", "Test123")
        message = self.mycampaignconfig.creatives_is_displayed("LIVE")
        message1 = self.mycampaignconfig.creatives_is_displayed("APPROVED")
        assert ("Payment" in message and "Payment" in message1)