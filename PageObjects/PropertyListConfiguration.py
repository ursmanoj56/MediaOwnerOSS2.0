import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class PropertyListConfiguration(BasePage):
    PROPERTY_CARD_DETAILS =(By.XPATH,"//button[text()='Property card details']")
    DISPLAY_NAME_TOGGLE =(By.ID, "display name-4-Property card details")
    DISTRICT_TOGGLE =(By.ID,"district & state-4-Property card details")
    CITY_TOGGLE = (By.ID, "city-4-Property card details")
    BROADTYPE_TOGGLE = (By.ID, "board type (Classic/Digital)-4-Property card details")
    SCREEN_TYPE_TOGGLE =(By.ID, "screen type-4-Property card details")
    RESOLUTION_TOGGLE= (By.ID, "resolution/size-4-Property card details")
    POTENTIAL_VIEWS_TOGGLE = (By.ID ,"show potential views-4-Property card details")
    PRICE_TOGGLE = (By.ID,"price/month-4-Property card details")
    VIEW_MORE_TOGGLE= (By.ID,"view more-4-Property card details")
    DISPLAY_IMAGE_TOGGLE = (By.ID,"DisplayImage-4-Property card details")
    ADD_CART_TOGGLE= (By.ID,"AddToCart-4-Property card details")
    NEXT_AVALIBILITY_TOGGLE = (By.ID,"Next Availability-4-Property card details")
    EXPLORE =(By.XPATH,"//button[text()='Explore']")
    LOGIN_BUTTON = (By.XPATH ,"(//button[@class='landing-login'])[2]")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_AUTH_BUTTON = (By.ID, "authButton")
    CREATE_CAMPAIGN = (By.XPATH, "//a[text()='Start New Campaign']")
    CAMPAIGN_NAME = (By.ID, "name")
    CLICK_CALENDER1 = (By.ID, "calendarIcon")
    NEXT_MONTH = (By.XPATH, "//pre[@class='create-right']")
    CURRENT_MONTH = (By.XPATH, "//p[@class='create-display']")
    SELECT_DATE = (By.XPATH, "//div[text()='{day}']")
    CLICK_CALENDER2 = (By.ID, "calendarIcon1")
    NEXT_MONTH2 = (By.XPATH, "//pre[@class='create-right1']")
    CURRENT_MONTH2 = (By.XPATH, "//p[@class='create-display1']")
    SELECT_DATE2 = (By.XPATH, "(//div[text()='{day}'])[2]")
    SELECT_STATE = (By.ID, "states_dropdown")
    SELECT_DISTRICTS = (By.ID, "Districts")


    NEXT_BUTTON = (By.XPATH, "//b[text()='Next']")
    BILLBOARD_IMAGE = (By.XPATH, "(//img[@class='images-list'])[1]")
    BILLBOARD_NAME = (By.XPATH, "(//b[@class='listview-sunnybank-outbound8'])[1]")
    BILLBOARD_STATE = (By.XPATH, "(//div[@class='listview-queensland5'])[1]")
    BILLBOARD_PRICE = (By.XPATH, "(//div[@class='listview-aud-50005'])[1]")
    BILLBOARD_RESOLUTION = (By.XPATH, "(//div[@class='listview-x608'])[1]")
    BILLBOARD_NEXT_SLOT = (By.XPATH, "(//div[@class='listview-nov-2024'])[1]")
    BILLBOARD_IMPRESSION = (By.XPATH, "(//div[@class='listview-availability-value'])[1]")
    VIEW_MORE = (By.XPATH ,"(//button[text()='Preview '])[1]")
    ADD_TO_CART = (By.XPATH, "(//button[text()='Add to Cart'])[1]")
    PREVIEW=(By.XPATH,"//div[text()='Preview']")
    SAVE_ALL_CONFIGURATION = (By.ID, "save-all-config-btn")
    CLOSE_POPUP = (By.XPATH, "//button[text()='Close']")



    def __init__(self, driver):
        super().__init__(driver)

    def verify_default_enble_toggle_options_are_Checked_disable_in_PropertList(self):
        self.click_button(self.PROPERTY_CARD_DETAILS)
        return self.is_checkbox_checked(self.DISPLAY_NAME_TOGGLE)

    def verfy_District_is_Checked(self):
        return self.is_checkbox_checked(self.DISTRICT_TOGGLE)

    def verfy_City_is_Checked(self):
        return self.is_checkbox_checked(self.CITY_TOGGLE)

    def verfy_Broadtype_is_Checked(self):
        return self.is_checkbox_checked(self.BROADTYPE_TOGGLE)

    def verify_Screen_is_Checked(self):
        return self.is_checkbox_checked(self.SCREEN_TYPE_TOGGLE)

    def verfy_DisplayImage_is_Checked(self):
        return self.is_checkbox_checked(self.DISPLAY_IMAGE_TOGGLE)

    def verfy_District_is_Disable(self):
        return self.is_element_disabled(self.DISTRICT_TOGGLE)

    def verfy_DisPlay_is_Disable(self):
        return self.is_element_disabled(self.DISPLAY_NAME_TOGGLE)

    def verfy_City_is_Disable(self):
        return self.is_element_disabled(self.CITY_TOGGLE)

    def verfy_Broadtype_is_Disable(self):
        return self.is_element_disabled(self.BROADTYPE_TOGGLE)

    def verfy_Screen_is_Disable(self):
        return self.is_element_disabled(self.SCREEN_TYPE_TOGGLE)

    def verfy_DisplayImage_is_Disable(self):
        return self.is_element_disabled(self.DISPLAY_IMAGE_TOGGLE)

    def open_date_picker(self):
        self.click_button(self.CLICK_CALENDER1)
        time.sleep(3)

    def get_current_month_year(self):
        month_year_text = self.get_text(self.CURRENT_MONTH)
        return month_year_text

    def navigate_to_month(self, target_month, target_year):
        month_mapping = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }
        reverse_month_mapping = {v: k for k, v in month_mapping.items()}

        target_year = int(target_year)
        target_month_num = month_mapping[target_month]

        while True:
            current_month_year = self.get_current_month_year()
            current_month_str, current_year_str = current_month_year.split()
            current_year = int(current_year_str)
            current_month = month_mapping[current_month_str]

            if current_year == target_year and current_month == target_month_num:
                break
            elif current_year > target_year or (current_year == target_year and current_month > target_month_num):
                self.click_button(self.NEXT_MONTH)
            else:
                self.click_button(self.NEXT_MONTH)

    def select_date(self, day):
        xpath = self.SELECT_DATE[1].format(day=day)  # Format the XPATH string
        date_locator1 = (self.SELECT_DATE[0], xpath)  # Recreate the tuple with the formatted XPATH
        self.click_button(date_locator1)

    def open_date_picker2(self):
        self.click_button(self.CLICK_CALENDER2)
        time.sleep(3)

    def get_current_month_year2(self):
        month_year_text = self.get_text(self.CURRENT_MONTH2)
        return month_year_text

    def navigate_to_month2(self, target_month, target_year):
        month_mapping = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }
        reverse_month_mapping = {v: k for k, v in month_mapping.items()}

        target_year = int(target_year)
        target_month_num = month_mapping[target_month]

        while True:
            current_month_year = self.get_current_month_year2()
            current_month_str, current_year_str = current_month_year.split()
            current_year = int(current_year_str)
            current_month = month_mapping[current_month_str]

            if current_year == target_year and current_month == target_month_num:
                break
            elif current_year > target_year or (current_year == target_year and current_month > target_month_num):
                self.click_button(self.NEXT_MONTH2)
            else:
                self.click_button(self.NEXT_MONTH2)

    def select_date2(self, day):
        xpath = self.SELECT_DATE2[1].format(day=day)  # Format the XPATH string
        date_locator1 = (self.SELECT_DATE2[0], xpath)  # Recreate the tuple with the formatted XPATH
        self.click_button(date_locator1)

    def navigateToSearch_Page(self,name, password,campaignName,month1, year1,date1,month2,year2, date2,state,district):
        self.click_button(self.PREVIEW)
        self.switch_to_frame(0)
        self.click_button(self.LOGIN_BUTTON)
        time.sleep(1)
        self.text_input(self.USERNAME,name)
        self.text_input(self.PASSWORD,password)
        self.click_button(self.LOGIN_AUTH_BUTTON)
        time.sleep(2)
        self.click_button(self.CREATE_CAMPAIGN)
        time.sleep(2)
        self.text_input(self.CAMPAIGN_NAME,campaignName)
        self.open_date_picker()
        self.navigate_to_month(month1, year1)
        self.select_date(date1)
        self.open_date_picker2()
        self.navigate_to_month2(month2,year2)
        self.select_date2(date2)
        self.select_state(state,district)

    def select_state(self,value,value2):
        self.click_button(self.SELECT_STATE)
        time.sleep(2)
        self.select_dropdown_option_by_value(self.SELECT_STATE,value)
        time.sleep(2)
        self.click_button(self.SELECT_DISTRICTS)
        time.sleep(5)
        self.select_dropdown_option_by_value(self.SELECT_DISTRICTS, value2)
        time.sleep(1)
        self.click_button(self.NEXT_BUTTON)
        time.sleep(4)


    def verify_Alldefault_enable_checked_elements_is_Displayed_propertyList(self):
        self.move_to_element(self.BILLBOARD_NAME)
        return self.is_displayed(self.BILLBOARD_NAME)

    def verify_imageISDisplayed(self):
        return self.is_displayed(self.BILLBOARD_IMAGE)

    def verify_District_is_displayed(self):
        return self.is_displayed(self.BILLBOARD_STATE)

    def verify_Resolution_is_displayed(self):
        return self.is_displayed(self.BILLBOARD_RESOLUTION)

    def verify_Price_element_when_configuration_disable(self):
        self.click_button(self.PROPERTY_CARD_DETAILS)
        self.click_button(self.PRICE_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        time.sleep(2)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()

    def validate_BillboardPrice(self):
        self.scroll_to_bottom()
        return self.is_displayed(self.BILLBOARD_PRICE)

    def verify_View_More_when_configuration_disable(self):
        self.click_button(self.PROPERTY_CARD_DETAILS)
        self.click_button(self.VIEW_MORE_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        time.sleep(2)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()

    def validate_Billboard_View_More(self):
        self.scroll_to_bottom()
        self.move_to_element(self.BILLBOARD_NAME)
        return self.is_displayed(self.VIEW_MORE)

    def verify_Impresson_element_when_configuration_disable(self):
        self.click_button(self.PROPERTY_CARD_DETAILS)
        self.click_button(self.POTENTIAL_VIEWS_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        time.sleep(2)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()

    def validate_BillboardImpression(self):
        self.scroll_to_bottom()
        return self.is_displayed(self.BILLBOARD_IMPRESSION)

    def verify_Next_Availability_element_when_configuration_disable(self):
        self.click_button(self.PROPERTY_CARD_DETAILS)
        self.click_button(self.NEXT_AVALIBILITY_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        time.sleep(2)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()

    def validate_BillboardNextSlot(self):
        self.scroll_to_bottom()
        return self.is_displayed(self.BILLBOARD_NEXT_SLOT)

    def verify_AddtoCart_when_configuration_disable(self):
        self.click_button(self.PROPERTY_CARD_DETAILS)
        self.click_button(self.ADD_CART_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        time.sleep(2)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()

    def validate_Billboard_AddtoCart(self):
        self.scroll_to_bottom()
        self.move_to_element(self.BILLBOARD_NAME)
        return self.is_displayed(self.ADD_TO_CART)




