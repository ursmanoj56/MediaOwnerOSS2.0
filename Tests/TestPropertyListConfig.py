from PageObjects.TenantLogin import TenantLogin
from Tests.BaseTest import BaseTest


class TestPropertyListConfig(BaseTest):

    def login(self):
        """Reusable login method"""
        self.tenantlogin = TenantLogin(self. driver)
        self.choosetemplate = self.tenantlogin.validate_loginFunction_withValid_credential("manohar", "admin@123")
        self.pageconfiguration = self.choosetemplate.verify_whether_configurationPage_is_displayed_click_configButton()
        self.propertylistconfiguration = self.pageconfiguration.goto_Property_List_config()
    def searchPage(self):
        self.propertylistconfiguration.navigateToSearch_Page("manoj_vanigam", "Manoj@123", "test41","October", 2024,21,"October", 2024,25,"59d203e278d0675bdf1fff1a", "barcoo")

    def test_verify_default_enble_toggle_options_are_Checked_disable_in_PropertList(self):
        self.login()
        message = self.propertylistconfiguration.verify_default_enble_toggle_options_are_Checked_disable_in_PropertList()
        message1 = self.propertylistconfiguration.verfy_District_is_Checked()
        message2 = self.propertylistconfiguration.verfy_City_is_Checked()
        message3 = self.propertylistconfiguration.verfy_Broadtype_is_Checked()
        message4 = self.propertylistconfiguration.verify_Screen_is_Checked()
        message5 = self.propertylistconfiguration.verfy_DisplayImage_is_Checked()
        message6 = self.propertylistconfiguration.verfy_District_is_Disable()
        message7 = self.propertylistconfiguration.verfy_DisPlay_is_Disable()
        message8 = self.propertylistconfiguration.verfy_City_is_Disable()
        message9 = self.propertylistconfiguration.verfy_Broadtype_is_Disable()
        message10 = self.propertylistconfiguration.verfy_Screen_is_Disable()
        message11 = self.propertylistconfiguration.verfy_DisplayImage_is_Disable()
        assert (message is True and message1 is True  and message2 is True and message3 is True and message4 is True and message5 is True and message6 is True and message7 is True and message8 is True and message9 is True and message10 is True and message11 is True)

    def test_verify_Alldefault_enable_checked_elements_is_Displayed_propertyList(self):
        self.login()
        self.searchPage()
        message = self.propertylistconfiguration.verify_Alldefault_enable_checked_elements_is_Displayed_propertyList()
        message1 = self.propertylistconfiguration.verify_imageISDisplayed()
        message2 = self.propertylistconfiguration.verify_District_is_displayed()
        message3 = self.propertylistconfiguration.verify_Resolution_is_displayed()
        assert (message is True and message1 is True and message2 is True and message3 is True)

    def test_verify_Price_element_when_configuration_disable(self):
        self.login()
        self.propertylistconfiguration.verify_Price_element_when_configuration_disable()
        self.searchPage()
        message =self.propertylistconfiguration.validate_BillboardPrice()
        assert message is False

    def test_verify_Price_element_when_configuration_enable(self):
        self.login()
        self.propertylistconfiguration.verify_Price_element_when_configuration_disable()
        self.searchPage()
        message = self.propertylistconfiguration.validate_BillboardPrice()
        assert message is True

    def test_verify_View_More_when_configuration_disable(self):
        self.login()
        self.propertylistconfiguration.verify_View_More_when_configuration_disable()
        self.searchPage()
        message = self.propertylistconfiguration.validate_Billboard_View_More()
        assert message is False

    def test_verify_View_More_when_configuration_enable(self):
        self.login()
        self.propertylistconfiguration.verify_View_More_when_configuration_disable()
        self.searchPage()
        message = self.propertylistconfiguration.validate_Billboard_View_More()
        assert message is True

    def test_verify_Impresson_element_when_configuration_disable(self):
        self.login()
        self.propertylistconfiguration.verify_Impresson_element_when_configuration_disable()
        self.searchPage()
        message = self.propertylistconfiguration.validate_BillboardImpression()
        assert message is False

    def test_verify_Impresson_element_when_configuration_enable(self):
        self.login()
        self.propertylistconfiguration.verify_Impresson_element_when_configuration_disable()
        self.searchPage()
        message = self.propertylistconfiguration.validate_BillboardImpression()
        assert message is True

    def test_verify_Next_Availability_element_when_configuration_disable(self):
        self.login()
        self.propertylistconfiguration.verify_Next_Availability_element_when_configuration_disable()
        self.searchPage()
        message = self.propertylistconfiguration.validate_BillboardNextSlot()
        assert message is False

    def test_verify_Next_Availability_element_when_configuration_enable(self):
        self.login()
        self.propertylistconfiguration.verify_Next_Availability_element_when_configuration_disable()
        self.searchPage()
        message = self.propertylistconfiguration.validate_BillboardNextSlot()
        assert message is True

    def test_verify_AddtoCart_when_configuration_disable(self):
        self.login()
        self.propertylistconfiguration.verify_AddtoCart_when_configuration_disable()
        self.searchPage()
        message = self.propertylistconfiguration.validate_Billboard_AddtoCart()
        assert message is False

    def test_verify_AddtoCart_when_configuration_enable(self):
        self.login()
        self.propertylistconfiguration.verify_AddtoCart_when_configuration_disable()
        self.searchPage()
        message = self.propertylistconfiguration.validate_Billboard_AddtoCart()
        assert message is True




