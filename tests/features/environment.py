import os
import json

import allure
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from driver.driver import start_browser


load_dotenv()


def before_scenario(context, scenario):
    context.email = os.getenv("EMAIL")
    context.password = os.getenv("PASSWORD")
    context.base_url = os.getenv("URL")

    if not context.email or not context.password:
        raise RuntimeError(
            "EMAIL and PASSWORD must be configured in .env file"
        )

    context.is_api_test = "api" in scenario.tags

    if context.is_api_test:
        # API test
        context.playwright = sync_playwright().start()
        context.request = context.playwright.request.new_context()

    else:
        # UI test
        context.playwright, context.browser, context.page = start_browser()
        context.page.goto(context.base_url)


def after_step(context, step):

    if context.is_api_test:
        if hasattr(context, "response"):
            response = context.response

            curl = (
                f"curl -X {context.request_method} "
                f"'{context.request_url}'"
            )

            allure.attach(
                curl,
                name="cURL",
                attachment_type=allure.attachment_type.TEXT
            )

            try:
                response_body = json.dumps(
                    response.json(),
                    indent=2,
                    ensure_ascii=False
                )
            except Exception:
                response_body = response.text()

            allure.attach(
                response_body,
                name=f"Response - HTTP {response.status}",
                attachment_type=allure.attachment_type.JSON
            )

    else:
        allure.attach(
            context.page.screenshot(),
            name=f"Screenshot - {step.name}",
            attachment_type=allure.attachment_type.PNG
        )

def after_scenario(context, scenario):

    if context.is_api_test:
        context.request.dispose()
        context.playwright.stop()

    else:
        context.browser.close()
        context.playwright.stop()


def generate_curl(response):
    request = response.request

    curl = [
        f"curl -X {request.method}",
        f"'{request.url}'"
    ]

    for name, value in request.headers.items():
        curl.append(f"-H '{name}: {value}'")

    if request.post_data:
        try:
            body = json.loads(request.post_data)
            body = json.dumps(body, indent=2)
            curl.append(f"-d '{body}'")
        except json.JSONDecodeError:
            curl.append(f"-d '{request.post_data}'")

    return " \\\n  ".join(curl)