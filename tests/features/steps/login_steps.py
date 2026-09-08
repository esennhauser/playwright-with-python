from behave import given, when, then

from pages.login_page import LoginPage


@given("The customer is at the login page")
def step_customer_at_login_page(context):
    context.login_page = LoginPage(context.page)


@when("The customer fills in his email and password")
def step_customer_fills_credentials(context):
    context.login_page.fill_credentials(
        context.email,
        context.password
    )


@when("The customer clicks on the Log In button")
def step_click_log_in(context):
    context.login_page.click_login()


@then("The customer can see the products page")
def step_dashboard_visible(context):
    context.login_page.verify_dashboard()
    