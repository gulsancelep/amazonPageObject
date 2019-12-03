from amazon.amazonTest.POM.locators import MainPageLocators
from amazon.amazonTest.POM.actions.actionPage import Actions


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.Actions_Wait = Actions(driver)


class LoginPage(BasePage):

    def username_write(self):
        self.Actions_Wait.input(MainPageLocators.USERNAME, MainPageLocators.username)

    def password_write(self):
        self.Actions_Wait.input(MainPageLocators.PASSWORD, MainPageLocators.password)

    def continue_click(self):
        self.Actions_Wait.click(MainPageLocators.CONTINUE, "ID")

    def sign_in(self):
        self.Actions_Wait.click(MainPageLocators.SIGN_IN, "ID")



