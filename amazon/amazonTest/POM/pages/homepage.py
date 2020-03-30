from amazon.amazonTest.POM.locators import MainPageLocators
from amazon.amazonTest.POM.actions.actionPage import Actions


class MainPage(Actions):

    def is_amazon(self):
        assert "https://www.amazon.com/" in self.driver.current_url

    def click_nav_sign_in(self):
        Actions.click(MainPageLocators.NAV_SIGN_IN, "ID")

    def searching(self):
        Actions.input(MainPageLocators.SEARCHING, MainPageLocators.search_input)

    def searching_click(self):
        Actions.click(MainPageLocators.SEARCH_CLICK, "XPATH")
        Actions.click(MainPageLocators.NAV_SIGN_IN, "ID")

    def searching(self):
        Actions.input(MainPageLocators.SEARCHING, MainPageLocators.search_input)

    def searching_click(self):
        Actions.click(MainPageLocators.SEARCH_CLICK, "CLASS_NAME")
