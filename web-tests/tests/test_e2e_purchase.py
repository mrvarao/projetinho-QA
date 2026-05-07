from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_complete_purchase(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    assert "/inventory" in driver.current_url, "login deveria redirecionar pra /inventory"

    inventory = InventoryPage(driver)
    assert inventory.get_cart_badge_count() == 0, "carrinho deveria comecar vazio"

    inventory.add_item_to_cart("Sauce Labs Backpack")
    assert inventory.get_cart_badge_count() == 1, "badge deveria mostrar 1 apos primeiro item"

    inventory.add_item_to_cart("Sauce Labs Bike Light")
    assert inventory.get_cart_badge_count() == 2, "badge deveria mostrar 2 apos segundo item"

    inventory.go_to_cart()
    assert "cart.html" in driver.current_url

    cart = CartPage(driver)
    items = cart.get_cart_items()
    assert len(items) == 2, f"esperado 2 itens no carrinho, recebi {len(items)}"
    assert "Sauce Labs Backpack" in items
    assert "Sauce Labs Bike Light" in items

    cart.proceed_to_checkout()
    assert "checkout-step-one" in driver.current_url

    checkout = CheckoutPage(driver)
    checkout.fill_info("Test", "User", "12345")
    checkout.continue_checkout()
    assert "checkout-step-two" in driver.current_url

    checkout.finish_checkout()
    assert "checkout-complete" in driver.current_url
    assert checkout.get_confirmation_message() == "Thank you for your order!"
