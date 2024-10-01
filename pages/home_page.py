from playwright.sync_api import expect

from data.data import UserData
from pages.base_page import BasePage
from dotenv import load_dotenv
import os

load_dotenv()

class HomePage(BasePage):
    gateway_url = os.getenv('GATEWAY_URL')
    url = f'http://{gateway_url}/security/users'

    def check_home_page(self):
        """
        Проверяет доступность 'Домашней страницы'.
        """
        self.page.get_by_role("main")
        text = self.page.get_by_text("Пользователи").first
        expect(text).to_be_visible()

    def check_menu_availability(self):
        """
        Проверяет доступность меню и корректность имени пользователя.
        """
        self.page.get_by_role("toolbar").get_by_role("button").first.click()
        self.page.locator("#q-portal--menu--2").get_by_role("button").nth(1).click()
        expect(self.page.locator("#q-portal--dialog--3").get_by_text(UserData.username, exact=True)).to_be_visible()
        self.click_button_by_role(name="Отмена")

    def check_ml_menu(self):  #TODO refactor
        """
        Проверяет доступность меню Предиктивной аналитики.
        """
        self.page.get_by_role("toolbar").get_by_role("button").first.click()
        expect(self.page.locator("a").filter(has_text="Предиктивная аналитика"))

    def click_to_ml(self):
        """
        Переходит в раздел Предиктивной аналитики.
        """
        self.page.get_by_role("toolbar").get_by_role("button").first.click()
        self.page.locator("a").filter(has_text="Предиктивная аналитика").click()

    def click_to_access_groups(self):
        """
        Переходит на страницу Группы доступа.
        """
        self.page.locator("a").filter(has_text="Группы доступа").click()

