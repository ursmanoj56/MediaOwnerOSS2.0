import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.CartPageConfiguration import CartPageConfiguration
from PageObjects.LandingPageConfiguration import LandingPageConfiguration
from PageObjects.MyCampaignConfig import MyCampaignConfig
from PageObjects.PropertyListConfiguration import PropertyListConfiguration


class PageConfiguration(BasePage):
    LANDINGPAGE_CONFIG_BUTTON=(By.XPATH,"//button[text()='Landing Page']")
    CART_CONFIG_BUTTON = (By.XPATH, "//button[text()='Cart']")
    MYORDER_CONFIG_BUTTON = (By.XPATH, "//button[text()='My Campaigns']")
    PROP_DETAILS_CONFIG_BUTTON = (By.XPATH, "//button[text()='Property details']")
    SEARCH_PAGE_CONFIG_BUTTON = (By.XPATH, "//button[text()='Search Page']")
    USER_REG_CONFIG_BUTTON = (By.XPATH, "//button[text()='User Registration']")
    TERM_COND_CONFIG_BUTTON = (By.XPATH, "//button[text()='Terms & conditions']")
    PRIVACY_POL_CONFIG_BUTTON = (By.XPATH, "//button[text()='Privacy Policy']")
    CONTACT_US_CONFIG_BUTTON = (By.XPATH, "//button[text()='Contact Us']")
    REPORT_CONFIG_BUTTON = (By.XPATH, "//button[text()='Reports']")
    NOTIFICATION_CONFIG_BUTTON = (By.XPATH, "//button[text()='Alert & Notification']")
    ASSERT_CONFIG_BUTTON = (By.XPATH, "//button[text()='Assets']")
    TECH_CONFIG_BUTTON = (By.XPATH, "//button[text()='Tech configuration']")
    SAVE_ALL_CONFIG_BUTTON = (By.ID, "save-all-config-btn")


    def __init__(self, driver):
        super().__init__(driver)

    def validate_configurationPage_URL(self):
        return self.get_current_url()

    def verify_all_configuration_buttons_displayed(self):
        time.sleep(2)
        self.refresh_page()
        return self.is_displayed(self.LANDINGPAGE_CONFIG_BUTTON)

    def verify_cartConfig_button_isDisplayed(self):
        return self.is_displayed(self.CART_CONFIG_BUTTON)

    def verify_Myorder_Config_button_isDisplayed(self):
        return self.is_displayed(self.MYORDER_CONFIG_BUTTON)

    def verify_Property_det_Config_button_isDisplayed(self):
        return self.is_displayed(self.PROP_DETAILS_CONFIG_BUTTON)

    def verify_SearchPagr_Config_button_isDisplayed(self):
        return self.is_displayed(self.SEARCH_PAGE_CONFIG_BUTTON)

    def verify_UserReg_Config_button_isDisplayed(self):
        return self.is_displayed(self.USER_REG_CONFIG_BUTTON)

    def verify_Terms_Cond_Config_button_isDisplayed(self):
        return self.is_displayed(self.TERM_COND_CONFIG_BUTTON)

    def verify_Privacy_Poly_Config_button_isDisplayed(self):
        return self.is_displayed(self.PRIVACY_POL_CONFIG_BUTTON)

    def verify_Contact_Us_Config_button_isDisplayed(self):
        return self.is_displayed(self.CONTACT_US_CONFIG_BUTTON)

    def verify_Report_Config_button_isDisplayed(self):
        return self.is_displayed(self.REPORT_CONFIG_BUTTON)

    def verify_Notify_Config_button_isDisplayed(self):
        return self.is_displayed(self.NOTIFICATION_CONFIG_BUTTON)

    def verify_Assert_Config_button_isDisplayed(self):
        return self.is_displayed(self.ASSERT_CONFIG_BUTTON)

    def verify_Tech_Config_button_isDisplayed(self):
        return self.is_displayed(self.TECH_CONFIG_BUTTON)

    def verify_save_all_configuration_button_is_displayed(self):
        time.sleep(2)
        self.refresh_page()
        return self.is_displayed(self.SAVE_ALL_CONFIG_BUTTON)

    def goto_landingpage_config(self):
        time.sleep(2)
        self.refresh_page()
        self.click_button(self.LANDINGPAGE_CONFIG_BUTTON)
        return LandingPageConfiguration(self.driver)

    def goto_Property_List_config(self):
        time.sleep(2)
        self.refresh_page()
        self.click_button(self.SEARCH_PAGE_CONFIG_BUTTON)
        return PropertyListConfiguration(self.driver)

    def goto_Property_Mycampaign_config(self):
        time.sleep(2)
        self.refresh_page()
        self.click_button(self.MYORDER_CONFIG_BUTTON)
        return MyCampaignConfig(self.driver)

    def goto_CartPAge_configuration(self):
        time.sleep(2)
        self.refresh_page()
        self.click_button(self.CART_CONFIG_BUTTON)
        return CartPageConfiguration(self.driver)



