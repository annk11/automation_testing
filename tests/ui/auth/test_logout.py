import allure
from playwright.sync_api import Page

from data.data import UserData
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


@allure.severity('CRITICAL')
@allure.description('Проверка функциональности выхода пользователя из системы.')
@allure.epic('UI tests')
@allure.feature('Authorization')
@allure.story('Logout Page')
class TestLogoutPage:
    def test_logout(self, page):
        login_page = LoginPage(page)
        logout_page = LogoutPage(page)
        home_page = HomePage(page)

        with allure.step("Открытие страницы входа"):
            login_page.open()

        with allure.step("Ввод логина и пароля"):
            login_page.login(UserData.username, UserData.password)

        with allure.step("Выбор домена"):
            login_page.set_realm()

        with allure.step("Проверка домашней страницы"):
            home_page.check_home_page()
            home_page.check_menu_availability()

        with allure.step("Выход из системы"):
            logout_page.logout()

    assert "Тест завершен"
