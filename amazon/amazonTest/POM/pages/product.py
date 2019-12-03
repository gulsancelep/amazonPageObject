from amazon.amazonTest.POM.locators import MainPageLocators
from amazon.amazonTest.POM.actions.actionPage import Actions


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.Actions_Wait = Actions(driver)


class ProductPage(BasePage):

    def add_to_list(self):
        self.Actions_Wait.click(MainPageLocators.ADD_TO_LIST, "ID")

    def wish_list(self):
        self.Actions_Wait.click(MainPageLocators.WISH_LIST, "XPATH")

    def is_wish_list(self):
        actual = "1 item added to Wish List"
        self.assertEqual(self.Actions_Wait.is_checking(MainPageLocators.IS_WISH_LIST), actual)

    def view_list_show(self):
        self.Actions_Wait.click(MainPageLocators.VIEW_LIST, "ID")

    def wish_list_delete(self):
        self.Actions_Wait.click(MainPageLocators.WISH_LIST_DELETE, "XPATH")

    def is_wish_list_delete(self):
        actual = "Deleted"
        self.assertEqual(self.Actions_Wait.is_checking(MainPageLocators.IS_WISH_LIST_DELETE), actual)



