from selenium.common.exceptions import ElementClickInterceptedException, WebDriverException
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
        add_locator = (By.ID, f"add-to-cart-{slug}")
        remove_locator = (By.ID, f"remove-{slug}")

        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.INVENTORY_CONTAINER))
        button = wait.until(EC.presence_of_element_located(add_locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )
        wait.until(EC.element_to_be_clickable(add_locator))
        try:
            button.click()
        except (ElementClickInterceptedException, WebDriverException):
            self.driver.execute_script("arguments[0].click();", button)
        wait.until(EC.presence_of_element_located(remove_locator))

    def go_to_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        WebDriverWait(self.driver, 15).until(EC.url_contains("cart.html"))

    def get_item_names(self):
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]
