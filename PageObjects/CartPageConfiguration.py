import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class CartPageConfiguration(BasePage):

    QUICK_SUMMERY = (By.XPATH , "//button[text()='Quick Summary']")
    IMPRESSION_TOGGLE =(By.ID ,"impressions-1-Quick Summary")
    REACH_TOGGLE = (By.ID ,"reach-1-Quick Summary")
    AVERAGE_FREQUENCY_TOGGLE = (By.ID ,"average frequency-1-Quick Summary")
    REPORTS_IN_CART = (By.XPATH , "//button[text()='Show report in cart page?']")
    DELIVERY_REPORT_TOGGLE = (By.ID ,"play log-1-show report in cart page?")
    PROOF_OF_PLAY_TOGGLE = (By.ID , "proof of play-1-show report in cart page?")
    POST_CAMPIAGN_REPORT_TOGGLE = (By.ID ,"post campaign report-1-show report in cart page?")
    IMPRESSION = (By.XPATH ,"//div[@class='cartfilled-impressions-parent']")
    REACH = (By.XPATH ,"//div[@class='cartfilled-metrics-labels']")
    AVERAGE_FREQUENCY = (By.XPATH, "//div[@class='cartfilled-metrics-values']")
    PROOF_OF_PLAY = (By.XPATH ,"//div[@class='cartfilled-proof-of-play']")
    POST_CAMPAIGN_REPORT = (By.XPATH ,"//div[@class='cartfilled-pcr-post-campaign']")
    DELIVERY_REPORT = (By.XPATH ,"//div[@class='cartfilled-delivery-report']")
    USER_ICON = (By.XPATH , "//div[@class='user-icon']")
    CART_PAGE = (By.XPATH ,"//div[@id='dropdownMenu']/a[3]")
    SAVE_ALL_CONFIGURATION = (By.ID, "save-all-config-btn")
    CLOSE_POPUP = (By.XPATH, "//button[text()='Close']")

    PREVIEW = (By.XPATH, "//div[text()='Preview']")
    LOGIN = (By.XPATH, "(//button[@class='landing-login'])[2]")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_AUTH_BUTTON = (By.ID, "authButton")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_Impression_element_when_configuration_disable(self,username,password):
        self.click_button(self.QUICK_SUMMERY)
        self.click_button(self.IMPRESSION_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.loginSite(username, password)
        return self.is_displayed(self.IMPRESSION)


    def loginSite(self,username,password):
        self.click_button(self.PREVIEW)
        self.switch_to_frame(0)
        self.click_button(self.LOGIN)
        self.text_input(self.USERNAME, username)
        self.text_input(self.PASSWORD, password)
        self.click_button(self.LOGIN_AUTH_BUTTON)
        time.sleep(2)
        self.click_button(self.USER_ICON)
        self.click_button(self.CART_PAGE)


