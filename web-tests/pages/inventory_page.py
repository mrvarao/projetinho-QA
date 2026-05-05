from selenium.webdriver.common.by import By


class InventoryPage:
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        slug = item_name.lower().replace(" ", "-")
        button = self.driver.find_element(By.ID, f"add-to-cart-{slug}")
        button.click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    def get_item_names(self):
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]
