from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        slug = item_name.lower().replace(" ", "-")
        add_id = f"add-to-cart-{slug}"
        remove_locator = (By.ID, f"remove-{slug}")

        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.INVENTORY_CONTAINER))
        wait.until(EC.presence_of_element_located((By.ID, add_id)))
        self.driver.execute_script(
            "var el = document.getElementById(arguments[0]);"
            "el.scrollIntoView({block: 'center'});"
            "el.click();",
            add_id,
        )
        wait.until(EC.presence_of_element_located(remove_locator))

    def go_to_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        WebDriverWait(self.driver, 15).until(EC.url_contains("cart.html"))

    def get_item_names(self):
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]

    def get_cart_badge_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0
