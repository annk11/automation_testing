import allure
from playwright.sync_api import Page

from data.data import UserData
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


@allure.severity('CRITICAL')
@allure.description('Проверка функциональности выхода пользователя из системы.')
@allure.epic('Authorization')
@allure.feature('Logout')
@allure.story('Logout Page')
def test_logout(page: Page):
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)


    with allure.step("Открытие страницы входа"):
        login_page.open()

    with allure.step("Ввод логина и пароля"):
        login_page.login(UserData.username, UserData.password)

    with allure.step("Выбор домена"):
        login_page.set_realm()

    with allure.step("Проверка домашней страницы"):
        login_page.check_home_page()
        login_page.check_menu_availability()

    with allure.step("Выход из системы"):
        logout_page.logout()

    assert "Тест завершен"
