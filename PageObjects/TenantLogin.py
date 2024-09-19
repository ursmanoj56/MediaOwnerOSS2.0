from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.ChooseTemplate import ChooseTemplate


class TenantLogin(BasePage):
    USERNAME= (By.ID, "username")
    PASSWORD =(By.ID,"password")
    SUBMIT_LOGIN =(By.XPATH,"//button[text()='Login']")
    WARN_MESSAGE =(By.XPATH,"//div[@class='alert alert-danger']")

    def __init__(self, driver):
        super().__init__(driver)

    def loginButton_is_Displayed(self):
        return self.is_displayed(self.SUBMIT_LOGIN)

    def validate_login_without_Credential(self):
        self.click_button(self.SUBMIT_LOGIN)
        return self.get_required_message(self.USERNAME)

    def validateError_message_When_loginWith_invalid_credential(self,username,password):
        self.text_input(self.USERNAME,username)
        self.text_input(self.PASSWORD,password)
        self.click_button(self.SUBMIT_LOGIN)

    def validate_loginFunction_withValid_credential(self,username,password):
        self.text_input(self.USERNAME,username)
        self.text_input(self.PASSWORD,password)
        self.click_button(self.SUBMIT_LOGIN)
        return ChooseTemplate(self.driver)

       

    def warn_message(self):
        return self.get_text(self.WARN_MESSAGE)

    def validate_chooseTemplate_URL(self):
        return self.get_current_url()






