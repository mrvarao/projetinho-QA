from selenium.webdriver.common.by import By


class CartPage:
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        return [el.text for el in self.driver.find_elements(*self.CART_ITEMS)]

    def proceed_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
