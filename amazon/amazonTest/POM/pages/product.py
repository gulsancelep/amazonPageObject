from amazon.amazonTest.POM.locators import MainPageLocators
from amazon.amazonTest.POM.actions.actionPage import Actions


class ProductPage(Actions):

    def add_to_list(self):
        Actions.click(MainPageLocators.ADD_TO_LIST, "ID")

    def wish_list(self):
        Actions.click(MainPageLocators.WISH_LIST, "XPATH")

    def is_wish_list(self):
        actual = "1 item added to Wish List"
        self.assertEqual(Actions.is_checking(MainPageLocators.IS_WISH_LIST), actual)

    def view_list_show(self):
        Actions.click(MainPageLocators.VIEW_LIST, "ID")

    def wish_list_delete(self):
        Actions.click(MainPageLocators.WISH_LIST_DELETE, "XPATH")

    def is_wish_list_delete(self):
        actual = "Deleted"
        self.assertEqual(Actions.is_checking(MainPageLocators.IS_WISH_LIST_DELETE), actual)



