from selenium.webdriver.common.by import By


class Locaters:
    LOGIN = (By.XPATH, "(//button[@class='landing-login'])[2]")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")

