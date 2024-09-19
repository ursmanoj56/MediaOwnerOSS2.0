import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class LandingPageConfiguration(BasePage):

    ADDRESS_TOGGLE=(By.ID,"address-0")
    LOGIN_TOGGLE =(By.ID,"login-0")
    LOGO_TOGGLE = (By.ID, "logo-0")
    CONTACT_FORM_TOGGLE = (By.ID, "contact form-0")
    CONTACT_EMAIL_TOGGLE = (By.ID, "contact email-0")
    FOOTER_TOGGLE = (By.ID, "footer-0")
    HEADLINE_TOGGLE = (By.ID, "headline-0")
    SUB_HEADLINE_TOGGLE = (By.ID, "sub headline-0")
    IMAGE_IN_LANDING_TOGGLE = (By.ID, "do you need an image in your landing page-0")
    FEATURE_PROPERTIES_TOGGLE = (By.ID, "featured properties-0")
    POPULAR_PROPERTIES_TOGGLE = (By.ID, "popular properties-0")
    CLIENT_WE_SERVED_TOGGLE = (By.ID, "clients we have served-0")
    TESTIMONIAL_TOGGLE = (By.ID, "clients testimonials-0")
    START_CAMPAIGN_TOGGLE = (By.ID, "start a campaign-0")
    SOCIAL_LINKS_TOGGLE = (By.ID, "social media links-0")
    TERMS_CONDITION_TOGGLE = (By.ID, "terms&conditions-0")
    PRIVACY_POLICY_TOGGLE = (By.ID, "privacy policy-0")
    ADD_IMAGE_CONTACT_TOGGLE = (By.ID, "add image for contact us-0")
    SAVE_ALL_CONFIGURATION = (By.ID,"save-all-config-btn")
    PREVIEW_BUTTON =(By.XPATH,"//div[text()='Preview']")

    LOGO=(By.XPATH,"//button[@class='landing-rectangle-parent']")
    HEADLINE =(By.XPATH,"//p[@class='landing-maximise']")
    LANDINGPAGE_IMAGE =(By.XPATH,"//img[@class='landing-mask-group-icon']")
    START_CAMPAIGN =(By.XPATH,"//button[@class='landing-rectangle-container']")
    LOGIN =(By.ID, "Login")
    EXPLORE =(By.XPATH, "//button[text()='Explore']")
    SUB_HEADLINE=(By.XPATH, "//h3[@class='landing-with-the-largest']")
    EXPLORE_PROPERTIES =(By.XPATH,"//div[@class='landing-explore-properties-header-parent']")
    ONE_MILLION_VIEWS_HEAD =(By.XPATH,"//h3[@class='landing-properties-with-1']")
    ONE_MILLION_IMAGE =(By.XPATH,"//div[@class='landing-featured-properties']")
    ONE_MILLION_IMAGE_LEFT_BUTTON = (By.XPATH, "//button[@class='landing-prevButton']")
    ONE_MILLION_IMAGE_RIGHT_BUTTON = (By.XPATH, "//button[@class='landing-nextButton']")
    ONE_MILLION_IMAGE_SCROLL_ICON =(By.XPATH,"//div[@class='landing-client-logos']")
    CLIENT_WE_SERVED=(By.XPATH,"//div[@class='landing-client-header']")
    CLIENT_WE_SAYS_HEADER=(By.XPATH,"//div[@class='landing-testimonial-content']")
    CLIENT_WE_SAYS = (By.XPATH, "//div[@class='landing-testimonial']")
    CLIENT_WE_SAYS_SCROLL=(By.XPATH,"//div[@class='landing-testimonial-content1']")
    CONTACT_US = (By.XPATH, "//div[@class='landing-questions-wrapper-wrapper']")
    FOOTER= (By.XPATH,"//section[@class='landing-group-section']")
    CONTACT_MAIL =(By.XPATH,"//div[@class='landing-contact-details']")
    ADDRESS = (By.XPATH,"//div[@class='landing-contact-details1']")
    SOCIAL_LINKS = (By.XPATH,"//div[@class='landing-social-icons']")
    TERMS_CONDITION = (By.XPATH, "(//a[@class='landing-terms-conditions'])[1]")
    PRIVACY_POLICY= (By.ID,"privacypolicy")

    CLOSE_POPUP= (By.XPATH, "//button[text()='Close']")
    SUCESS_MESSAGE =(By.XPATH,"//h2[text()='Success Message']")


    FILE_UPLOAD_LOCATOR = (By.CSS_SELECTOR, 'input[type="file"]')
    UPLOAD_BIG_LOGO = (By.CSS_SELECTOR, 'a.browse')
    UPLOADED_LOGO=(By.XPATH, "(//a[@ref='fileLink'])[1]")
    UPLOADED_LOGO1 = (By.XPATH, "(//a[@ref='fileLink'])[2]")
    UPLOADED_LOGO2 = (By.XPATH, "(//a[@ref='fileLink'])[3]")
    DELETE_BIG_LOGO = (By.XPATH, "(//i[@class='fa fa-remove'])[1]")
    UPLOAD_BIG_FEVICON = (By.XPATH, "(//a[@class='browse'])[4]")
    UPLOAD_PAGE_IMAGE = (By.XPATH, "(//a[@class='browse'])[6]")
    CLIENT_SERVED_LOGO1 = (By.XPATH, "(//a[@class='browse'])[7]")
    CLIENT_SERVED_NEXT =(By.XPATH, "(//button[@class='btn btn-primary'])[1]")
    CLIENT_WE_SERVED_SAVE =(By.XPATH,"//button[text()='Save']")
    CLIENT_WE_SERVED_CANCEL =(By.XPATH,"//button[text()='Cancel']")
    CLIENT_WE_SERVED_DELETE= (By.XPATH,"(//button[contains(@class,'removeRow')])[1]")
    UPLOADED_CLIENT_SERVED =(By.XPATH, "(//li[@class='list-group-item']/following::div[2])[1]")
    CLIENT_ICON_NEXT = (By.XPATH, "(//button[@class='btn btn-primary'])[2]")
    UPLOAD_CONTACTUS_IMAGE = (By.XPATH, "(//a[@class='browse'])[6]")
    INPUT_HEADLINE= (By.XPATH,"//input[@name='data[headline]']")
    INPUT_SUBHEADLINE =(By.XPATH,"//input[@name='data[sub headline]']")

    SAVE_ADD_CONTENT = (By.XPATH,"//button[@name='data[submit]']")
    ERROR_MESSAGE= (By.XPATH,"//div[@class='alert alert-danger']")
    CLIENT_SAYS_NEXT = (By.XPATH, "(//button[@class='btn btn-primary'])[3]")
    CLIENT_NAME =(By.XPATH,"//input[@name='data[testimonials][employeeInformation][0][fullname]']")
    CLIENT_DESIGNATION =(By.XPATH,"//input[@name='data[testimonials][employeeInformation][0][designation]']")
    CLIENT_COMPANY_NAME =(By.XPATH,"//input[@name='data[testimonials][employeeInformation][0][companyname]']")
    CLIENT_NAME1 = (By.XPATH, "//input[@name='data[testimonials][employeeInformation][1][fullname]']")
    CLIENT_DESIGNATION1 = (By.XPATH, "//input[@name='data[testimonials][employeeInformation][1][designation]']")
    CLIENT_COMPANY_NAME1 = (By.XPATH, "//input[@name='data[testimonials][employeeInformation][1][companyname]']")
    CLIENT_NAME2 = (By.XPATH, "//input[@name='data[testimonials][employeeInformation][2][fullname]']")
    CLIENT_DESIGNATION2 = (By.XPATH, "//input[@name='data[testimonials][employeeInformation][2][designation]']")
    CLIENT_COMPANY_NAME2 = (By.XPATH, "//input[@name='data[testimonials][employeeInformation][2][companyname]']")
    CLIENT_TEXT =(By.XPATH,"//div[@class='ql-editor ql-blank']/p[1]")
    CONTACT_HEADLINE =(By.XPATH,"//input[@name='data[Contactusform][Contactheadline]']")
    CONTACTUS_SUBHEADLINE =(By.XPATH,"//input[@name='data[Contactusform][contactsubHeadline]']")
    ADDRESS =(By.XPATH,"//input[@name='data[address]']")
    EMAIL =(By.XPATH,"//input[@name='data[email]']")
    FACEBOOKLINK = (By.XPATH,"//input[@name='data[SocialmediaLinks][facebookLink]']")
    TWITTERLINK = (By.XPATH,"//input[@name='data[SocialmediaLinks][twitterLink]']")
    INSTAGRAMLINK = (By.XPATH,"//input[@name='data[SocialmediaLinks][instagramLink]']")

    CLOSE_SUCCES_MESSAGE =(By.XPATH, "//button[text()='Close']")
    BACK_BUTTON=(By.XPATH,"//div[text()='Go back']")
    PUBLISH=(By.XPATH,"//div[text()='Publish']")










    def __init__(self, driver):
        super().__init__(driver)

    def verify_default_enble_toggle_options_are_Checked_disable(self):
        return self.is_checkbox_checked(self.LOGO_TOGGLE)

    def verify_logo_toggle_is_disable(self):
        return self.is_element_disabled(self.LOGO_TOGGLE)

    def verify_Headline_toggle_is_disable(self):
        return self.is_element_disabled(self.HEADLINE_TOGGLE)

    def verify_ImageIn_landing_toggle_is_disable(self):
        return self.is_element_disabled(self.IMAGE_IN_LANDING_TOGGLE)

    def verify_Startcampaign_toggle_is_disable(self):
        return self.is_element_disabled(self.START_CAMPAIGN_TOGGLE)

    def verify_Headline_toggle_is_checked(self):
        return self.is_checkbox_checked(self.HEADLINE_TOGGLE)

    def verify_ImageIn_landing_toggle_is_checked(self):
        return self.is_checkbox_checked(self.IMAGE_IN_LANDING_TOGGLE)

    def verify_Startcampaign_toggle_is_checked(self):
        return self.is_checkbox_checked(self.START_CAMPAIGN_TOGGLE)

    def verify_Alldefault_enable_checked_elements_is_Displayed(self):
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        return self.is_displayed(self.LOGO)

    def verify_Headline_elements_is_Displayed(self):
        return self.is_displayed(self.HEADLINE)

    def verify_LandingImage_element_is_Displayed(self):
        time.sleep(2)
        return self.is_displayed(self.LANDINGPAGE_IMAGE)

    def verify_StartCampaign_element_is_Displayed(self):
        self.scroll_into_view(self.START_CAMPAIGN)
        return self.is_displayed(self.START_CAMPAIGN)

    def verify_Save_configuration_button_works_properly(self):
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        return self.get_text(self.SUCESS_MESSAGE)

    def close_successMessage(self):
        self.click_button(self.CLOSE_POPUP)

    def verify_Login_element_when_configuration_disable(self):
        self.click_button(self.LOGIN_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        time.sleep(2)
        return self.is_displayed(self.LOGIN)


    def verify_Address_element_when_configuration_disable(self):
        self.click_button(self.ADDRESS_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        self.scroll_into_view(self.ADDRESS)
        time.sleep(2)
        return self.is_displayed(self.ADDRESS)

    def verify_Contact_form_element_when_configuration_disable(self):
        self.click_button(self.CONTACT_FORM_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        time.sleep(2)
        return self.is_displayed(self.CONTACT_US)

    def verify_Contact_email_element_when_configuration_disable(self):
        self.click_button(self.CONTACT_EMAIL_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        self.scroll_into_view(self.CONTACT_MAIL)
        time.sleep(2)
        return self.is_displayed(self.CONTACT_MAIL)

    def verify_Footer_element_when_configuration_disable(self):
        self.click_button(self.FOOTER_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        self.scroll_into_view(self.FOOTER)
        time.sleep(2)
        return self.is_displayed(self.FOOTER)

    def verify_SubHeadline_element_when_configuration_disable(self):
        self.click_button(self.SUB_HEADLINE_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        time.sleep(2)
        return self.is_displayed(self.SUB_HEADLINE)

    def verify_FeaturedProperties_element_when_configuration_disable(self):
        self.click_button(self.FEATURE_PROPERTIES_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        time.sleep(2)
        return self.is_displayed(self.EXPLORE_PROPERTIES)

    def verify_PopularProperties_element_when_configuration_disable(self):
        self.click_button(self.POPULAR_PROPERTIES_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        time.sleep(2)
        return self.is_displayed(self.ONE_MILLION_IMAGE)

    def is_PopularProperties_Head_displayed(self):
        return self.is_displayed(self.ONE_MILLION_VIEWS_HEAD)

    def is_PopularProperties_LeftButton_displayed(self):
        return self.is_displayed(self.ONE_MILLION_IMAGE_LEFT_BUTTON)

    def is_PopularProperties_RightButton_displayed(self):
        return self.is_displayed(self.ONE_MILLION_IMAGE_RIGHT_BUTTON)

    def is_PopularProperties_ScrollIcon_displayed(self):
        return self.is_displayed(self.ONE_MILLION_IMAGE_SCROLL_ICON)





    def verify_ClientWeServed_element_when_configuration_disable(self):
        self.click_button(self.CLIENT_WE_SERVED_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        time.sleep(2)
        return self.is_displayed(self.CLIENT_WE_SERVED)

    def verify_ClientTestinmonial_element_when_configuration_disable(self):
        self.click_button(self.TESTIMONIAL_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        time.sleep(2)
        return self.is_displayed(self.CLIENT_WE_SAYS_HEADER)

    def is_ClientTestinmonial_say_displayed(self):
        return self.is_displayed(self.CLIENT_WE_SAYS)

    def is_ClientTestinmonial_ScrollIcon_displayed(self):
        return self.is_displayed(self.CLIENT_WE_SAYS_SCROLL)



    def verify_SocialMedia_element_when_configuration_disable(self):
        self.click_button(self.SOCIAL_LINKS_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        time.sleep(2)
        return self.is_displayed(self.SOCIAL_LINKS)

    def verify_TermsCondi_element_when_configuration_disable(self):
        self.click_button(self.TERMS_CONDITION_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        time.sleep(2)
        return self.is_displayed(self.TERMS_CONDITION)

    def verify_Privacy_element_when_configuration_disable(self):
        self.click_button(self.PRIVACY_POLICY_TOGGLE)
        time.sleep(2)
        self.click_button(self.SAVE_ALL_CONFIGURATION)
        self.click_button(self.CLOSE_POPUP)
        self.refresh_page()
        self.click_button(self.PREVIEW_BUTTON)
        self.switch_to_frame(0)
        time.sleep(2)
        return self.is_displayed(self.PRIVACY_POLICY)

    def verify_to_uploadBrandLogo_invalid_formate_file(self,path,path1,path2):
       self.upload_image(self.UPLOAD_BIG_LOGO,self.FILE_UPLOAD_LOCATOR, path)
       self.upload_image(self.UPLOAD_BIG_LOGO,self.FILE_UPLOAD_LOCATOR,path1)
       self.upload_image(self.UPLOAD_BIG_LOGO,self.FILE_UPLOAD_LOCATOR,path2)

    def verify_logo_is_upoaded(self):
        return self.is_displayed(self.UPLOADED_LOGO)

    def verify_logo1_is_upoaded(self):
        return self.is_displayed(self.UPLOADED_LOGO1)

    def verify_logo2_is_upoaded(self):
        return self.is_displayed(self.UPLOADED_LOGO2)

    def delete_logo(self):
        self.click_button(self.DELETE_BIG_LOGO)

    def verify_to_uploadFeviconLogo_invalid_formate_file(self, path, path1):
        self.upload_image(self.UPLOAD_BIG_FEVICON, self.FILE_UPLOAD_LOCATOR, path)
        self.upload_image(self.UPLOAD_BIG_FEVICON, self.FILE_UPLOAD_LOCATOR, path1)
        time.sleep(5)

    def verify_fevicon_is_upoaded(self):
        return self.is_displayed(self.UPLOADED_LOGO)

    def verify_fevicon1_is_upoaded(self):
        return self.is_displayed(self.UPLOADED_LOGO1)

    def delete_fevicon(self):
        time.sleep(2)
        self.click_button(self.DELETE_BIG_LOGO)

    def verify_to_uplod_PageImage_invalid_formate_file(self, path):
        self.upload_image(self.UPLOAD_PAGE_IMAGE, self.FILE_UPLOAD_LOCATOR, path)
        time.sleep(5)

    def verify_PageImage_is_upoaded(self):
        return self.is_displayed(self.UPLOADED_LOGO)

    def delete_PageImage(self):
        time.sleep(2)
        self.click_button(self.DELETE_BIG_LOGO)

    def verify_to_uplod_ClientWeServed_invalid_formate_file(self, path,path1,path2):
        self.scroll_into_view(self.CLIENT_SERVED_NEXT)
        self.click_button(self.CLIENT_SERVED_NEXT)
        self.upload_image(self.CLIENT_SERVED_LOGO1, self.FILE_UPLOAD_LOCATOR, path)
        time.sleep(2)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.click_button(self.CLIENT_SERVED_NEXT)
        self.upload_image(self.CLIENT_SERVED_LOGO1, self.FILE_UPLOAD_LOCATOR, path1)
        time.sleep(2)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.click_button(self.CLIENT_SERVED_NEXT)
        self.upload_image(self.CLIENT_SERVED_LOGO1, self.FILE_UPLOAD_LOCATOR, path2)
        time.sleep(2)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)

    def verify_ClientWeServed_is_upoaded(self):
        return self.is_displayed(self.UPLOADED_CLIENT_SERVED)

    def delete_ClientWeServed(self):
        time.sleep(2)
        self.click_button(self.CLIENT_WE_SERVED_DELETE)

    def verify_to_uplod_ClientTestimonail_invalid_formate_file(self, path,path1,path2):
        self.scroll_into_view(self.CLIENT_ICON_NEXT)
        self.click_button(self.CLIENT_ICON_NEXT)
        self.upload_image(self.CLIENT_SERVED_LOGO1, self.FILE_UPLOAD_LOCATOR, path)
        time.sleep(2)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.click_button(self.CLIENT_SERVED_NEXT)
        self.upload_image(self.CLIENT_SERVED_LOGO1, self.FILE_UPLOAD_LOCATOR, path1)
        time.sleep(2)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.click_button(self.CLIENT_SERVED_NEXT)
        self.upload_image(self.CLIENT_SERVED_LOGO1, self.FILE_UPLOAD_LOCATOR, path2)
        time.sleep(2)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)

    def verify_ClientTestimonail_is_upoaded(self):
        return self.is_displayed(self.UPLOADED_CLIENT_SERVED)

    def delete_ClientTestimonail(self):
        time.sleep(2)
        self.click_button(self.CLIENT_WE_SERVED_DELETE)

    def verify_to_uplod_ContactUSImage_invalid_formate_file(self, path):
        self.scroll_into_view(self.UPLOAD_CONTACTUS_IMAGE)
        self.upload_image(self.UPLOAD_CONTACTUS_IMAGE, self.FILE_UPLOAD_LOCATOR, path)
        time.sleep(2)

    def verify_ContactUSImage_is_upoaded(self):
        return self.is_displayed(self.UPLOAD_BIG_LOGO)

    def delete_ContactUSImage(self):
        time.sleep(2)
        self.click_button(self.DELETE_BIG_LOGO)

    def verify_errorMessage_when_click_saveContent_withoutData(self):
        self.scroll_into_view(self.SAVE_ADD_CONTENT)
        self.click_button(self.SAVE_ADD_CONTENT)
        return self.is_displayed(self.ERROR_MESSAGE)

    def verify_sitePublish_with_validaData(self,brandlogo1,brandlogo2,brandlogo3,feviconlogo1,feviconlogo2,pageimage,headline,subheadline,clientlogo1,clientlogo2,clientlogo3,clienticon1,clienticon2,clienticon3,clientname1,
        clientdesignation1,clientcompany1,clienttext1,clientname2,clientdesignation2,clientcompany2,clienttext2,
        clientname3,clientdesignation3,clientcompany3,clienttext3,contactheadline,contactsubheadline,conatctimage,
                                           address,mail,facebook,twitter,instagram):
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, brandlogo1)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, brandlogo2)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, brandlogo3)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, feviconlogo1)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, feviconlogo2)
        self.scroll_into_view(self.UPLOAD_BIG_LOGO)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, pageimage)
        self.text_input(self.INPUT_HEADLINE,headline)
        self.text_input(self.INPUT_SUBHEADLINE, subheadline)
        self.scroll_into_view(self.CLIENT_SERVED_NEXT)
        self.click_button(self.CLIENT_SERVED_NEXT)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, clientlogo1)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.click_button(self.CLIENT_SERVED_NEXT)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, clientlogo2)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.click_button(self.CLIENT_SERVED_NEXT)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, clientlogo3)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.scroll_into_view(self.CLIENT_ICON_NEXT)
        self.click_button(self.CLIENT_ICON_NEXT)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, clienticon1)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.click_button(self.CLIENT_ICON_NEXT)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, clienticon2)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.click_button(self.CLIENT_ICON_NEXT)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, clienticon3)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.scroll_into_view(self.CLIENT_SAYS_NEXT)
        self.click_button(self.CLIENT_SAYS_NEXT)
        self.text_input(self.CLIENT_NAME,clientname1)
        self.text_input(self.CLIENT_DESIGNATION,clientdesignation1)
        self.text_input(self.CLIENT_COMPANY_NAME,clientcompany1)
        self.text_input(self.CLIENT_TEXT,clienttext1)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.scroll_into_view(self.CLIENT_SAYS_NEXT)
        self.click_button(self.CLIENT_SAYS_NEXT)
        self.text_input(self.CLIENT_NAME1, clientname2)
        self.text_input(self.CLIENT_DESIGNATION1, clientdesignation2)
        self.text_input(self.CLIENT_COMPANY_NAME1, clientcompany2)
        self.text_input(self.CLIENT_TEXT, clienttext2)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.scroll_into_view(self.CLIENT_SAYS_NEXT)
        self.click_button(self.CLIENT_SAYS_NEXT)
        self.text_input(self.CLIENT_NAME2, clientname3)
        self.text_input(self.CLIENT_DESIGNATION2, clientdesignation3)
        self.text_input(self.CLIENT_COMPANY_NAME2, clientcompany3)
        self.text_input(self.CLIENT_TEXT, clienttext3)
        self.click_button(self.CLIENT_WE_SERVED_SAVE)
        self.text_input(self.CONTACT_HEADLINE,contactheadline)
        self.text_input(self.CONTACTUS_SUBHEADLINE,contactsubheadline)
        self.upload_image(self.UPLOAD_BIG_LOGO, self.FILE_UPLOAD_LOCATOR, conatctimage)
        self.text_input(self.ADDRESS,address)
        self.text_input(self.EMAIL,mail)
        self.text_input(self.FACEBOOKLINK,facebook)
        self.text_input(self.TWITTERLINK,twitter)
        self.text_input(self.INSTAGRAMLINK,instagram)
        self.click_button(self.SAVE_ADD_CONTENT)
        time.sleep(2)
        self.click_button(self.CLOSE_SUCCES_MESSAGE)
        self.scroll_into_view(self.BACK_BUTTON)
        self.click_button(self.BACK_BUTTON)
        self.click_button(self.PUBLISH)
        time.sleep(30)
























