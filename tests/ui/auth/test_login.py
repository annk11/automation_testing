import allure

from data.data import UserData
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.severity('CRITICAL')
@allure.description('Проверка функциональности входа пользователя в систему.')
@allure.epic('UI-tests')
@allure.feature('Authorization')
@allure.story('Login Page')
class TestLoginPage:
    def test_login(self, page):
        login_page = LoginPage(page)
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

    assert "Тест завершен"
