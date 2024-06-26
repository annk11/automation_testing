# from playwright.sync_api import Page
#
#
# def test_ok(page: Page) -> None:
#     page.goto("https://sso.passport.yandex.ru/push?uuid=7b848d25-6cfa-421e-a1d3-1a3dece6c8e6&retpath=https%3A%2F%2Fdzen.ru%2F%3Fyredirect%3Dtrue%26is_autologin_ya%3Dtrue")
#     page.goto("https://sso.dzen.ru/install?uuid=7b848d25-6cfa-421e-a1d3-1a3dece6c8e6")
#     page.goto("https://dzen.ru/?yredirect=true&is_autologin_ya=true")
#     page.goto("https://dzen.ru/?yredirect=true")
#     page.frame_locator("iframe[src=\"https\\:\\/\\/dzen\\.ru\\/\\?yredirect\\=true\"]").get_by_label("Запрос").click()
#     page.frame_locator("iframe[name=\"search_0\\.7984963459210119\"]").get_by_label("Запрос").fill("запрос")
#     with page.expect_popup() as page1_info:
#         page.frame_locator("iframe[name=\"search_0\\.7984963459210119\"]").get_by_role("button", name="Найти").click()
#     page1 = page1_info.value