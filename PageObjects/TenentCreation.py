import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class TenantCreation(BasePage):
    NAME =(By.ID,"name")
    MO_ID =(By.ID, "mo_id")
    MO_EMAIL= (By.ID,"mo_email")
    DOMAIN_NAME =(By.ID,"domain_name")
    CREATE_BUTTON= (By.XPATH, "//button[text()='Create Tenant']")
    SUCESS_MESSAGE=(By.XPATH,"//h2[text()='Success!']")
    ERROR_MESSAGE =(By.XPATH,"//h2[text()='Error!']")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_current_URL(self):
        return self.get_current_url()

    def verify_TenantButton_is_displayed(self):
        return self.is_displayed(self.CREATE_BUTTON)

    def validate_ErrorMessage_TenantCreation_without_credentials(self):
        self.get_required_message(self.CREATE_BUTTON)
        time.sleep(5)
        return self.get_required_message(self.NAME)

    def tenantCreation_with_invalidData(self,Name,MoId,MoMail,DomainName):
        self.text_input(self.NAME,Name)
        self.text_input(self.MO_ID,MoId)
        self.text_input(self.MO_EMAIL,MoMail)
        self.text_input(self.DOMAIN_NAME,DomainName)
        self.click_button(self.CREATE_BUTTON)
        return self.get_required_message(self.NAME)

    def tenantCreation_with_invalidData_MOmail(self):
        return self.get_required_message(self.MO_ID)

    def tenantCreation_with_invalidData_MOid(self):
        return self.get_required_message(self.MO_EMAIL)

    def tenantCreation_with_invalidData_MOmail(self):
        return self.get_required_message(self.MO_ID)

    def tenantCreation_with_invalidData_DomainName(self):
        return self.get_required_message(self.DOMAIN_NAME)

    def tenantCreation_with_validData(self,Name,MoId,MoMail,DomainName):
        self.text_input(self.NAME,Name)
        self.text_input(self.MO_ID,MoId)
        self.text_input(self.MO_EMAIL,MoMail)
        self.text_input(self.DOMAIN_NAME,DomainName)
        self.click_button(self.CREATE_BUTTON)
        time.sleep(5)

    def tenantCreation_SuccessMessage(self):
        return self.get_text(self.SUCESS_MESSAGE)

    def tenantCreation_with_DuplicATEData(self):
        time.sleep(5)
        return self.get_text(self.ERROR_MESSAGE)





