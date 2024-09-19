import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class MyCampaignConfig(BasePage):
    FILTER_DROPDOWN_TOGGLE =(By.ID,"dropdownstatuslist-2")
    SEARCH_BAR_TOGGLE =(By.ID,"searchInOrders-2")
    CUSTAMISE_TABLE_TOGGLE =(By.ID,"customiseTable-2")
    PREVIEW = (By.XPATH, "//div[text()='Preview']")
    FILTER = (By.ID ,"statusFilter")
    CUSTAMISE_TABLE =(By.ID ,"customizeBtn")
    SEARC_BAR = (By.XPATH ,"//div[@class='order-search-parent']")
    LOGIN = (By.XPATH ,"(//button[@class='landing-login'])[2]")
    USERNAME = (By.ID ,"username")
    PASSWORD = (By.ID, "password")
    LOGIN_AUTH_BUTTON = (By.ID ,"authButton")
    CRETIVES_TOGGLE =(By.ID, "creative-2")
    DELIVERY_REPORT_TOGGLE = (By.ID,"deliveryReport-2")
    PAYMENT_INVOICE_TOGGLE = (By.ID,"paymentInvoice-2")
    CRETIVES = (By.XPATH ,"(//div[@class='dropdown-content-myorder'])[1]")
    CRETIVES1 = (By.ID,"(//div[@class='dropdown-content-myorder']/a[text()=' Creatives'])[1]")
    DELIVERY_REPORT = (By.XPATH ,"(//div[@class='dropdown-content-myorder']/a[text()=' Delivery Report'])[1]")
    PAYMENT_INVOICE = (By.XPATH ,"(//div[@class='dropdown-content-myorder']/a[text()=' Payment Invoice'])[1]")

    SAVE_ALL_CONFIGURATION = (By.ID, "save-all-config-btn")
    CLOSE_POPUP = (By.XPATH, "//button[text()='Close']")
    SELECT_FILTER = (By.ID,"statusFilter")
    VIEW_OPTION =(By.XPATH ,"(//button[@class='view-button'])[1]")


    def __init__(self, driver):
        super().__init__(driver)

    def verify_default_enble_toggle_options_are_Checked_disable_in_Mycampaign(self):
        return self.is_checkbox_checked(self.FILTER_DROPDOWN_TOGGLE)

    def verfy_SearchBar_is_Checked(self):
        return self.is_checkbox_checked(self.SEARCH_BAR_TOGGLE)

    def verfy_Custamised_Table_is_Checked(self):
        return self.is_checkbox_checked(self.CUSTAMISE_TABLE_TOGGLE)

    def verify_FilterDropDown_is_disable(self):
        return self.is_element_disabled(self.FILTER_DROPDOWN_TOGGLE)

    def verify_SearchBar_is_disable(self):
        return self.is_element_disabled(self.SEARCH_BAR_TOGGLE)

    def verify_CustamisedTable_is_disable(self):
        return self.is_element_disabled(self.CUSTAMISE_TABLE_TOGGLE)

    def verify_Alldefault_enable_checked_elements_is_Displayed_in_Mycampaign(self,username,password):
        self.click_button(self.PREVIEW)
        self.switch_to_frame(0)
        self.click_button(self.LOGIN)
        self.text_input(self.USERNAME,username)
        self.text_input(self.PASSWORD,password)
        self.click_button(self.LOGIN_AUTH_BUTTON)
        time.sleep(2)
        return self.is_displayed(self.FILTER)

    def verify_SearchBar_is_Displayed(self):
        return self.is_displayed(self.SEARC_BAR)

    def verify_CustamisedTable_is_Displayed(self):
        time.sleep(2)
        return self.is_displayed(self.CUSTAMISE_TABLE)

    def verify_Creative_option_when_configuration_disable(self,username,password):
        self.click_button(self.CRETIVES_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW)
        self.switch_to_frame(0)
        self.click_button(self.LOGIN)
        self.text_input(self.USERNAME, username)
        self.text_input(self.PASSWORD, password)
        self.click_button(self.LOGIN_AUTH_BUTTON)
        time.sleep(2)

    def creatives_is_displayed(self,value):
        self.select_dropdown_option_by_value(self.SELECT_FILTER,value)
        self.move_to_element(self.VIEW_OPTION)
        return self.get_text(self.CRETIVES)

    def verify_DeliveryReport_option_when_configuration_disable(self, username, password):
        self.click_button(self.DELIVERY_REPORT_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW)
        self.switch_to_frame(0)
        self.click_button(self.LOGIN)
        self.text_input(self.USERNAME, username)
        self.text_input(self.PASSWORD, password)
        self.click_button(self.LOGIN_AUTH_BUTTON)
        time.sleep(2)


    def verify_PaymentInvoice_option_when_configuration_disable(self, username, password):
        self.click_button(self.PAYMENT_INVOICE_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW)
        self.switch_to_frame(0)
        self.click_button(self.LOGIN)
        self.text_input(self.USERNAME, username)
        self.text_input(self.PASSWORD, password)
        self.click_button(self.LOGIN_AUTH_BUTTON)
        time.sleep(2)













