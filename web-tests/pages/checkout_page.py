from selenium.webdriver.common.by import By


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
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE_INPUT).send_keys(zip_code)

    def continue_checkout(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_confirmation_message(self):
        return self.driver.find_element(*self.CONFIRMATION_HEADER).text
