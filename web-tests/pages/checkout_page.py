from selenium.common.exceptions import ElementClickInterceptedException, WebDriverException
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

    def _click(self, locator):
        wait = WebDriverWait(self.driver, 20)
        button = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )
        wait.until(EC.element_to_be_clickable(locator))
        try:
            button.click()
        except (ElementClickInterceptedException, WebDriverException):
            self.driver.execute_script("arguments[0].click();", button)

    def fill_info(self, first_name, last_name, zip_code):
        wait = WebDriverWait(self.driver, 20)
        first = wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))
        first.send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE_INPUT).send_keys(zip_code)

    def continue_checkout(self):
        self._click(self.CONTINUE_BUTTON)
        WebDriverWait(self.driver, 20).until(EC.url_contains("checkout-step-two"))

    def finish_checkout(self):
        self._click(self.FINISH_BUTTON)
        WebDriverWait(self.driver, 20).until(EC.url_contains("checkout-complete"))

    def get_confirmation_message(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.CONFIRMATION_HEADER)
        ).text
