from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        slug = item_name.lower().replace(" ", "-")
        remove_locator = (By.ID, f"remove-{slug}")
        self.driver.find_element(By.ID, f"add-to-cart-{slug}").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(remove_locator))

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        WebDriverWait(self.driver, 15).until(EC.url_contains("cart.html"))

    def get_item_names(self):
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]
