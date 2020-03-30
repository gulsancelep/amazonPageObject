from amazon.amazonTest.POM.locators import MainPageLocators
from amazon.amazonTest.POM.actions.actionPage import Actions


class LoginPage(Actions):

    def username_write(self):
        Actions.input(MainPageLocators.USERNAME, MainPageLocators.username)

    def password_write(self):
        Actions.input(MainPageLocators.PASSWORD, MainPageLocators.password)

    def continue_click(self):
        Actions.click(MainPageLocators.CONTINUE, "ID")

    def sign_in(self):
        Actions.click(MainPageLocators.SIGN_IN, "ID")
