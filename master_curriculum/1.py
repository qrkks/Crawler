from playwright.sync_api import Playwright, sync_playwright, expect
import re
from log.log_conifg import setup_logging
from decouple import config

logger = setup_logging(__name__)

logger.debug(config('test'))


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config('test'))
    page.locator("#kw").click()
    logger.debug(page.locator("#kw"))
    page.locator("#kw").fill("playwright")
    button = page.get_by_role("button", name="百度一下")
    input('输入完成后回车')
    button.click()

    # page.wait_for_event('click', target=page.get_by_role("button", name="百度一下"))
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="microsoft/playwright - GitHub").click()
    page1 = page1_info.value

    input('Ok?')
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
