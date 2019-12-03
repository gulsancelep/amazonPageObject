from amazon.amazonTest.POM.locators import MainPageLocators
from amazon.amazonTest.POM.actions.actionPage import Actions


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.Actions_Wait = Actions(driver)


class MainPage(BasePage):

    def is_amazon(self):
        assert "https://www.amazon.com/" in self.driver.current_url

    def click_nav_sign_in(self):
        self.Actions_Wait.click(MainPageLocators.NAV_SIGN_IN, "ID")

    def searching(self):
        self.Actions_Wait.input(MainPageLocators.SEARCHING, MainPageLocators.search_input)

    def searching_click(self):
        self.Actions_Wait.click(MainPageLocators.SEARCH_CLICK, "XPATH")
