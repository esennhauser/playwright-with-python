from behave import when, then


@when("The client requests the products endpoint")
def step_request_products(context):
    url = "https://dummyjson.com/products"
    method = "GET"

    context.request_method = method
    context.request_url = url

    context.response = context.request.get(url)


@then("The response status should be 200")
def step_verify_status(context):
    assert context.response.status == 200


@then("The response should contain products")
def step_verify_products(context):
    body = context.response.json()

    assert "products" in body
    assert isinstance(body["products"], list)
    assert len(body["products"]) > 0

    product = body["products"][0]

    assert "id" in product
    assert "title" in product
    assert "price" in product