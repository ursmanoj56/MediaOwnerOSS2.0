import pytest

from PageObjects.TenantLogin import TenantLogin
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtilities import get_data_from_excel


class TestTenantLogin(BaseTest):
    def test_loginButton_is_Displayed(self):
        self.tenantlogin =TenantLogin(self.driver)
        message =self.tenantlogin.loginButton_is_Displayed()
        assert message is True

    def test_validate_login_without_Credential(self):
        self.tenantlogin = TenantLogin(self.driver)
        message = self.tenantlogin.validate_login_without_Credential()
        assert message.__contains__("Please fill out this field")

    @pytest.mark.parametrize("username,password",get_data_from_excel(r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\TenantCreation.xlsx", "Sheet2"))
    def test_validateError_message_When_loginWith_invalid_credential(self, username, password):
        self.tenantlogin =TenantLogin(self.driver)
        self.tenantlogin.validateError_message_When_loginWith_invalid_credential(username, password)
        message= self.tenantlogin.warn_message()
        assert message.__contains__("Invalid username or password")

    def test_validate_loginFunction_withValid_credential(self):
        self.tenantlogin =TenantLogin(self.driver)
        choosetemplate = self.tenantlogin.validate_loginFunction_withValid_credential("manoj", "admin@123")
        message =choosetemplate.get_current_url()
        assert message.__contains__("http://164.52.223.30:8001/mytemplate/")


