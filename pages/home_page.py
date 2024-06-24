from playwright.sync_api import expect

from pages.base_page import BasePage


class HomePage(BasePage):
    url = 'http://bi-tst-01:8082/security/users'


    def check_ml_menu(self):  #TODO refactor
        self.page.get_by_role("toolbar").get_by_role("button").first.click()
        expect(self.page.locator("a").filter(has_text="Предиктивная аналитика"))

    def click_to_ml(self):
        self.page.get_by_role("toolbar").get_by_role("button").first.click()
        self.page.locator("a").filter(has_text="Предиктивная аналитика").click()