from playwright.sync_api import expect

from pages.base_page import BasePage


class LogoutPage(BasePage):
    """
    Класс LogoutPage наследует от базового класса BasePage и представляет собой
    страницу выхода из системы. Содержит методы для выходв из системы.
    """
    url = "http://bi-tst-01:8082/login"

    def get_title(self): #TODO add to login test
        """
        Получение заголовка домашней страницы. Этот метод возвращает заголовок
        текущей страницы, который можно использовать для проверки того, что
        пользователь находится на правильной странице.
        """
        return self.title()

    def logout(self):
        """
        Выход из системы.
        """
        self.page.get_by_role("toolbar").get_by_role("button").first.click()
        self.page.locator("#q-portal--menu--4").get_by_role("button").nth(2).click()
        expect(self.page.get_by_role("heading")).to_contain_text("Авторизация")