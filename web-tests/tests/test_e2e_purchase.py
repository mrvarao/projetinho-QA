from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_complete_purchase(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    assert "/inventory" in driver.current_url

    inventory = InventoryPage(driver)
    inventory.add_item_to_cart("Sauce Labs Backpack")
    inventory.add_item_to_cart("Sauce Labs Bike Light")
    inventory.go_to_cart()

    cart = CartPage(driver)
    items = cart.get_cart_items()
    assert "Sauce Labs Backpack" in items
    assert "Sauce Labs Bike Light" in items

    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_info("Test", "User", "12345")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert checkout.get_confirmation_message() == "Thank you for your order!"
