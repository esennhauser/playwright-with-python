from behave import given, when, then

from pages.login_page import LoginPage
from pages.products_page import ProductPage


@given("A customer is logged on the Saucedemo platform")
def step_customer_is_logged_in(context):
    login_page = LoginPage(context.page)

    login_page.fill_credentials(
        "standard_user",
        "secret_sauce"
    )

    login_page.click_login()

    login_page.verify_dashboard()


@given("The customer is on the products page")
def step_customer_is_on_products_page(context):
    product_page = ProductPage(context.page)

    product_page.verify_products_page()


@when('The customer adds "{product_name}" to the cart')
def step_customer_adds_product_to_cart(context, product_name):
    product_page = ProductPage(context.page)

    context.product_name = product_name

    product_page.add_product_to_cart(product_name)


@when("The customer clicks on the cart button")
def step_customer_clicks_cart(context):
    product_page = ProductPage(context.page)

    product_page.click_cart()


@then("The customer can see the product previously selected")
def step_customer_sees_selected_product(context):
    product_page = ProductPage(context.page)

    product_page.verify_product_in_cart(
        context.product_name
    )
