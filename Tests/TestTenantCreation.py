import pytest

from PageObjects.TenentCreation import TenantCreation
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtilities import get_data_from_excel


class TestTenantCreation(BaseTest):

    def test_validate_title(self):
        self.tenantcreat = TenantCreation(self.driver)
        message = self.tenantcreat.validate_current_URL()
        assert message.__contains__("http://164.52.223.30:8001/create-tenant/")

    def test_verify_TenantButton_is_displayed(self):
        self.tenantcreat = TenantCreation(self.driver)
        message = self.tenantcreat.verify_TenantButton_is_displayed()
        assert message is True

    def test_validate_TenantCreation_without_credentials(self):
        self.tenantcreat = TenantCreation(self.driver)
        message = self.tenantcreat.validate_ErrorMessage_TenantCreation_without_credentials()
        assert message.__contains__("Please fill out this field.")

    @pytest.mark.parametrize("Name,MoId,MoMail,DomainName",get_data_from_excel(r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\TenantCreation.xlsx", "Sheet1"))
    def test_tenantCreation_with_invalidData(self,Name,MoId,MoMail,DomainName):
        self.tenantcreat = TenantCreation(self.driver)
        message = self.tenantcreat.tenantCreation_with_invalidData(Name,MoId,MoMail,DomainName)
        message1=self.tenantcreat.tenantCreation_with_invalidData_MOid()
        message2 = self.tenantcreat.tenantCreation_with_invalidData_MOmail()
        message3 = self.tenantcreat.tenantCreation_with_invalidData_DomainName()
        assert (message.__contains__("Please fill out this field.") or message1.__contains__("Please fill out this field.") or message2.__contains__("Please fill out this field.") or message3.__contains__("Please fill out this field.") )

    def test_tenantCreation_with_validData(self):
        self.tenantcreat = TenantCreation(self.driver)
        self.tenantcreat.tenantCreation_with_validData('simha',654,'simha@gmail.com','usa')
        message =self.tenantcreat.tenantCreation_SuccessMessage()
        assert message.__contains__("Success!")

    def test_tenantCreation_with_DuplicATEData(self):
        self.tenantcreat = TenantCreation(self.driver)
        self.tenantcreat.tenantCreation_with_validData('simha', 654, 'simha@gmail.com', 'usa')
        message = self.tenantcreat.tenantCreation_with_DuplicATEData()
        assert message.__contains__("Error!")




