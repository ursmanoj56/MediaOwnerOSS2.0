import os

import pytest

from PageObjects.ChooseTemplate import ChooseTemplate
from PageObjects.TenantLogin import TenantLogin
from Tests.BaseTest import BaseTest
from Tests.TestData import TestData


class TestLandingPageConfiguration(BaseTest):

    def login(self):
        """Reusable login method"""
        self.tenantlogin = TenantLogin(self.driver)
        self.choosetemplate = self.tenantlogin.validate_loginFunction_withValid_credential("kailash", "admin@123")
        self.pageconfiguration = self.choosetemplate.verify_whether_configurationPage_is_displayed_click_configButton()
        self.landpageconfiguration = self.pageconfiguration.goto_landingpage_config()

    def test_verify_all_default_enble_toggle_option(self):
        self.login()
        message =self.landpageconfiguration.verify_default_enble_toggle_options_are_Checked_disable()
        message1 = self.landpageconfiguration.verify_Headline_toggle_is_checked()
        message2 = self.landpageconfiguration.verify_ImageIn_landing_toggle_is_checked()
        message3 = self.landpageconfiguration.verify_Startcampaign_toggle_is_checked()
        message4 = self.landpageconfiguration.verify_logo_toggle_is_disable()
        message5 = self.landpageconfiguration.verify_ImageIn_landing_toggle_is_disable()
        message6 = self.landpageconfiguration.verify_Headline_toggle_is_disable()
        message7 = self.landpageconfiguration.verify_Startcampaign_toggle_is_disable()
        assert (message is True and message1 is True and message2 is True and message3 is True and message4 is True and message5 is True and message6 is True and message7 is True)

    def test_verify_Alldefault_enable_checked_elements_is_Displayed(self):
        self.login()
        message = self.landpageconfiguration.verify_Alldefault_enable_checked_elements_is_Displayed()
        message1 = self.landpageconfiguration.verify_Headline_elements_is_Displayed()
        message2 = self.landpageconfiguration.verify_LandingImage_element_is_Displayed()
        message3 = self.landpageconfiguration.verify_StartCampaign_element_is_Displayed()

        assert (message is True and message1 is True and message2 is True and message3 is True )

    def test_verify_Save_configuration_button_works_properly(self):
        self.login()
        message = self.landpageconfiguration.verify_Save_configuration_button_works_properly()
        self.landpageconfiguration.close_successMessage()
        assert  message.__contains__("Success Message")


    def test_verify_Login_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_Login_element_when_configuration_disable()
        assert message is False

    def test_verify_Login_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_Login_element_when_configuration_disable()
        assert message is True

    def test_verify_Address_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_Address_element_when_configuration_disable()
        assert message is False

    def test_verify_Address_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_Address_element_when_configuration_disable()
        assert message is True

    def test_verify_Contact_form_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_Contact_form_element_when_configuration_disable()
        assert message is False

    def test_verify_Contact_form_element_when_configurationn_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_Contact_form_element_when_configuration_disable()
        assert message is True

    def test_verify_Contact_email_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_Contact_email_element_when_configuration_disable()
        assert message is False

    def test_verify_Contact_email_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_Contact_email_element_when_configuration_disable()
        assert message is True

    def test_verify_Footer_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_Footer_element_when_configuration_disable()
        assert message is False

    def test_verify_Footer_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_Footer_element_when_configuration_disable()
        assert message is True

    def test_verify_SubHeadline_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_SubHeadline_element_when_configuration_disable()
        assert message is False

    def test_verify_SubHeadline_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_SubHeadline_element_when_configuration_disable()
        assert message is True

    def test_verify_FeaturedProperties_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_FeaturedProperties_element_when_configuration_disable()
        assert message is False

    def test_verify_FeaturedProperties_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_FeaturedProperties_element_when_configuration_disable()
        assert message is True

    def test_verify_ClientWeServed_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_ClientWeServed_element_when_configuration_disable()
        assert message is False

    def test_verify_ClientWeServed_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_ClientWeServed_element_when_configuration_disable()
        assert message is True

    def test_verify_SocialMedia_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_SocialMedia_element_when_configuration_disable()
        assert message is False

    def test_verify_SocialMedia_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_SocialMedia_element_when_configuration_disable()
        assert message is True

    def test_verify_TermsCondi_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_TermsCondi_element_when_configuration_disable()
        assert message is False

    def test_verify_TermsCondi_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_TermsCondi_element_when_configuration_disable()
        assert message is True

    def test_verify_Privacy_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_Privacy_element_when_configuration_disable()
        assert message is False

    def test_verify_Privacy_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_Privacy_element_when_configuration_disable()
        assert message is True

    def test_verify_ClientTestinmonial_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_ClientTestinmonial_element_when_configuration_disable()
        message1 = self.landpageconfiguration.is_ClientTestinmonial_say_displayed()
        message2 = self.landpageconfiguration.is_ClientTestinmonial_ScrollIcon_displayed()
        assert (message is False and message1 is False and message2 is False)

    def test_verify_ClientTestinmonial_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_ClientTestinmonial_element_when_configuration_disable()
        message1 = self.landpageconfiguration.is_ClientTestinmonial_say_displayed()
        message2 = self.landpageconfiguration.is_ClientTestinmonial_ScrollIcon_displayed()
        assert (message is True and message1 is True and message2 is True)

    def test_verify_PopularProperties_element_when_configuration_disable(self):
        self.login()
        message = self.landpageconfiguration.verify_PopularProperties_element_when_configuration_disable()
        message1 = self.landpageconfiguration.is_PopularProperties_Head_displayed()
        message2 = self.landpageconfiguration.is_PopularProperties_LeftButton_displayed()
        message3 = self.landpageconfiguration.is_PopularProperties_RightButton_displayed()
        message4 = self.landpageconfiguration.is_PopularProperties_ScrollIcon_displayed()
        assert (message is False and message1 is False and message2 is False and message3 is False and message4 is False)

    def test_verify_PopularProperties_element_when_configuration_enable(self):
        self.login()
        message = self.landpageconfiguration.verify_PopularProperties_element_when_configuration_disable()
        message1 = self.landpageconfiguration.is_PopularProperties_Head_displayed()
        message2 = self.landpageconfiguration.is_PopularProperties_LeftButton_displayed()
        message3 = self.landpageconfiguration.is_PopularProperties_RightButton_displayed()
        message4 = self.landpageconfiguration.is_PopularProperties_ScrollIcon_displayed()
        assert (message is True and message1 is True and message2 is True and message3 is True and message4 is True)

    def test_verify_to_uploadBrandLogo_valid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uploadBrandLogo_invalid_formate_file(r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Logo.svg",r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Logo1.svg",r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\logo2.eps")
        message =self.landpageconfiguration.verify_logo_is_upoaded()
        message1 = self.landpageconfiguration.verify_logo1_is_upoaded()
        message2 = self.landpageconfiguration.verify_logo2_is_upoaded()
        assert (message is True and message1 is True and message2 is True)

    def test_verify_to_uploadBrandLogo_Invalid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uploadBrandLogo_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Tenant Creation.pdf",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\invoice.txt",
             r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\TenantCreation.xlsx")
        message = self.landpageconfiguration.verify_logo_is_upoaded()
        message1 = self.landpageconfiguration.verify_logo1_is_upoaded()
        message2 = self.landpageconfiguration.verify_logo2_is_upoaded()
        assert (message is False and message1 is False and message2 is False)

    def test_Verify_logoIS_displayed_when_deleteled(self):
        self.login()
        self.landpageconfiguration.verify_to_uploadBrandLogo_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Tenant Creation.pdf",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\invoice.txt",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\TenantCreation.xlsx")
        self.landpageconfiguration.delete_logo()
        self.landpageconfiguration.delete_logo()
        self.landpageconfiguration.delete_logo()

    def test_verify_to_uploadFeviconLogo_invalid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uploadFeviconLogo_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Tenant Creation.pdf",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\invoice.txt")

        message = self.landpageconfiguration.verify_fevicon_is_upoaded()
        message1 = self.landpageconfiguration.verify_fevicon1_is_upoaded()
        assert (message is False and message1 is False)

    def test_verify_to_uploadFeviconLogo_valid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uploadFeviconLogo_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\fevlogo.ico",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\fevlogo1.ico")

        message = self.landpageconfiguration.verify_fevicon_is_upoaded()
        message1 = self.landpageconfiguration.verify_fevicon1_is_upoaded()
        assert (message is True and message1 is True)

    def test_verify_deleteButton_in_uploadFeviconLogo(self):
        self.login()
        self.landpageconfiguration.verify_to_uploadFeviconLogo_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\fevlogo.ico",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\fevlogo1.ico")

        self.landpageconfiguration.delete_fevicon()
        self.landpageconfiguration.delete_fevicon()


    def test_verify_to_uplod_PageImage_invalid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_PageImage_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\fevlogo.ico")

        message = self.landpageconfiguration.verify_PageImage_is_upoaded()
        assert message is False

    def test_verify_to_uplod_PageImage_valid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_PageImage_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\landingImage.png")

        message = self.landpageconfiguration.verify_PageImage_is_upoaded()
        assert message is True

    def test_verify_deleteButton_in_uploadPageImage(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_PageImage_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\landingImage.png")
        self.landpageconfiguration.delete_PageImage()

    def test_verify_to_uplod_ClientWeServed_valid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_ClientWeServed_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Logo.svg",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Logo1.svg",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\logo2.eps")

        message = self.landpageconfiguration.verify_ClientWeServed_is_upoaded()
        assert message is True

    def test_verify_to_uplod_ClientWeServed_invalid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_ClientWeServed_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Tenant Creation.pdf",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\invoice.txt",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\TenantCreation.xlsx")
        message = self.landpageconfiguration.verify_ClientWeServed_is_upoaded()
        assert message is False

    def test_verify_deleteButton_in_uploadClientWeServed(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_ClientWeServed_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Logo.svg",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Logo1.svg",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\logo2.eps")
        self.landpageconfiguration.delete_ClientWeServed()

    def test_verify_to_uplod_ClientTestimonail_valid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_ClientTestimonail_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Logo.svg",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Logo1.svg",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\logo2.eps")

        message = self.landpageconfiguration.verify_ClientTestimonail_is_upoaded()
        assert message is True

    def test_verify_to_uplod_ClientTestimonail_Invalid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_ClientWeServed_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Tenant Creation.pdf",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\invoice.txt",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\TenantCreation.xlsx")
        message = self.landpageconfiguration.verify_ClientTestimonail_is_upoaded()
        assert message is False

    def test_verify_deleteButton_in_uploadClientTestimonail(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_ClientWeServed_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Logo.svg",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\Logo1.svg",
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\logo2.eps")
        self.landpageconfiguration.delete_ClientTestimonail()

    def test_verify_to_uplod_ContactUSImage_invalid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_ContactUSImage_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\fevlogo.ico")

        message = self.landpageconfiguration.verify_ContactUSImage_is_upoaded()
        assert message is False

    def test_verify_to_uplod_ContactUSImage_valid_formate_file(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_ContactUSImage_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\landingImage.png")

        message = self.landpageconfiguration.verify_ContactUSImage_is_upoaded()
        assert message is True

    def test_verify_deleteButton_in_uploadContactUSImage(self):
        self.login()
        self.landpageconfiguration.verify_to_uplod_ContactUSImage_invalid_formate_file(
            r"C:\Users\HP\PycharmProjects\BUILDER-OSS2.0\TestFiles\landingImage.png")
        self.landpageconfiguration.delete_ContactUSImage()

    def test_verify_errorMessage_when_click_saveContent_withoutData(self):
        self.login()
        message =self.landpageconfiguration.verify_errorMessage_when_click_saveContent_withoutData()
        assert message is True




    def test_verify_sitePublish_with_validaData(self):

     self.login()
     self.landpageconfiguration.verify_sitePublish_with_validaData(
        TestData.brandlogo1,TestData.brandlogo2, TestData.brandlogo3, TestData.feviconlogo1, TestData.feviconlogo2, TestData.pageimage, TestData.headline, TestData.subheadline,
        TestData.clientlogo1, TestData.clientlogo2, TestData.clientlogo3, TestData.clienticon1, TestData.clienticon2, TestData.clienticon3, TestData.clientname1,
        TestData.clientdesignation1, TestData.clientcompany1, TestData.clienttext1, TestData.clientname2, TestData.clientdesignation2, TestData.clientcompany2,
        TestData.clienttext2, TestData.clientname3, TestData.clientdesignation3, TestData.clientcompany3, TestData.clienttext3, TestData.contactheadline,
        TestData.contactsubheadline,
        TestData.conatctimage, TestData.address, TestData.mail, TestData.facebook, TestData.twitter, TestData.instagram
    )
















