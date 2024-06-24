import allure
from playwright.sync_api import Page

from data.data import UserData
from pages.login_page import LoginPage


@allure.severity('CRITICAL')
@allure.description('Проверка функциональности входа пользователя в систему.')
@allure.epic('Authorization')
@allure.feature('Login')
@allure.story('Login Page')
class TestLoginPage:
    def test_login(self, page: Page):
        login_page = LoginPage(page)

        with allure.step("Открытие страницы входа"):
            login_page.open()

        with allure.step("Ввод логина и пароля"):
            login_page.login(UserData.username, UserData.password)

        with allure.step("Выбор домена"):
            login_page.set_realm()

        with allure.step("Проверка домашней страницы"):
            login_page.check_home_page()
            login_page.check_menu_availability()

    assert "Тест завершен"
