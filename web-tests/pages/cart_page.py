from selenium.common.exceptions import ElementClickInterceptedException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(self.CART_ITEMS)
        )
        return [el.text for el in self.driver.find_elements(*self.CART_ITEMS)]

    def proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 20)
        button = wait.until(EC.presence_of_element_located(self.CHECKOUT_BUTTON))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )
        wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        try:
            button.click()
        except (ElementClickInterceptedException, WebDriverException):
            self.driver.execute_script("arguments[0].click();", button)
        wait.until(EC.url_contains("checkout-step-one"))
