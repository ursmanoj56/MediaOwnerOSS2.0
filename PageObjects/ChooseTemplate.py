from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.PageConfiguration import PageConfiguration


class ChooseTemplate(BasePage):
    TEMPLATE1 =(By.XPATH,"//img[@class='phone-image-icon']")
    CONFIGURE_BUTTON1 =(By.XPATH,"//div[contains(text(),'Configure')]")
    PREVIEW_BUTTON1=(By.XPATH,"//div[contains(text(),'Preview')]")
    PUBLISH_BUTTON1 =(By.XPATH,"//div[contains(text(),'Publish')]")
    EXPLORE_BUTTON =(By.XPATH,"//button[text()='Explore']")
    CONFIG_MODE_TEXT =(By.XPATH,"//div[@class='configuremodenav-your-in-now']")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_Templates_displayed(self):
        return self.is_displayed(self.TEMPLATE1)

    def Verfy_whether_previewPage_is_displayed_click_Preview(self):
        self.click_button(self.PREVIEW_BUTTON1)
        self.switch_to_frame(0)
        return  self.is_displayed(self.EXPLORE_BUTTON)

    def verify_whether_configurationPage_is_displayed_click_configButton(self):
        self.click_button(self.CONFIGURE_BUTTON1)
        return PageConfiguration(self.driver)






