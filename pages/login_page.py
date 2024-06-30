from playwright.sync_api import expect

from data.data import UserData
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Класс LoginPage наследует от базового класса BasePage и представляет собой
    страницу входа в систему. Содержит методы для входа в систему и проверку
    статуса входа.
    """
    url = "http://bi-tst-01:8082/login"

    def get_title(self): #TODO add to login test
        """
        Получение заголовка домашней страницы. Этот метод возвращает заголовок
        текущей страницы, который можно использовать для проверки того, что
        пользователь находится на правильной странице.
        """
        return self.title()

    def login(self, username, password):
        """
        Вход в систему с указанными именем пользователя и паролем.

        :param username: Имя пользователя для входа в систему.
        :param password: Пароль для входа в систему.
        """
        self.page.get_by_label("Логин").click()
        self.page.get_by_label("Логин").fill(username)
        self.page.get_by_label("Логин").press("Tab")
        self.page.get_by_label("Пароль").fill(password)
        self.click_button_by_role(name="Войти в систему")

    def set_realm(self): #TODO add realm parameter
        """
        Выбор домена для входа в систему.
        """
        self.page.get_by_text("arrow_drop_down").click()
        self.click_option_by_role(name='ML')
        self.click_button_by_role(name="Войти в домен")
