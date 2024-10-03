import allure

from data.data import UserData
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


@allure.epic('UI')
@allure.feature('Авторизация')
@allure.story('Выход из системы')
@allure.link("https://yt.omegafuture.ru/issue/OBI-1973", name="OBI-1973")
@allure.testcase("https://yt.omegafuture.ru/issue/OBI-1973", name="TC-001")
@allure.description('Проверка функциональности выхода пользователя из системы.')
@allure.tag("Авторизация", "БФС")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogoutPage:
    @allure.title("Выход из системы")
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
