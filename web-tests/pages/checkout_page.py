from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CONFIRMATION_HEADER = (By.CSS_SELECTOR, ".complete-header")

    def __init__(self, driver):
        self.driver = driver

    def fill_info(self, first_name, last_name, zip_code):
        wait = WebDriverWait(self.driver, 15)
        first = wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))
        first.send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE_INPUT).send_keys(zip_code)

    def continue_checkout(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()
        wait.until(EC.url_contains("checkout-step-two"))

    def finish_checkout(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()
        wait.until(EC.url_contains("checkout-complete"))

    def get_confirmation_message(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.CONFIRMATION_HEADER)
        ).text
