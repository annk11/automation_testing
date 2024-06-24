import pytest


@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {
            "width": 1366,
            "height": 768,
        }
    }

# @pytest.fixture(scope='class')
# def browser():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(channel="chrome", headless=False)
#         context = browser.new_context(ignore_https_errors=True)
#         page = context.new_page()
#         yield page
#         page.close()
#         browser.close()
