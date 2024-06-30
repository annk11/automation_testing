import allure

from data.data import UserData
from pages.access_groups_page import AccessGroupsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.severity('NORMAL')
@allure.description('Сквозной кейс для блока Предиктивной аналитики. Проверяет функциональность'
                    ' создания группы доступа для ML-инженеров и добавляет туда шаблон и эксперимент.')
@allure.epic('ML')
@allure.feature('E2E')
@allure.story('Access groups for ML experiment/pattern')
class TestE2EAccessGroups:
    def test_e2e_access_groups(self, page) -> None:
        login_page = LoginPage(page)
        home_page = HomePage(page)
        access_groups_page = AccessGroupsPage(page)

        with allure.step("Открытие страницы входа"):
            login_page.open()

        with allure.step("Ввод логина и пароля"):
            login_page.login(UserData.username, UserData.password)

        with allure.step("Выбор домена"):
            login_page.set_realm()

        with allure.step("Проверка домашней страницы"):
            home_page.check_home_page()
            home_page.check_menu_availability()

        with allure.step("Создание группы доступа"):
            home_page.click_to_access_groups()
            access_groups_page.create_access_group()
            access_groups_page.check_access_group()

        with allure.step("Редактирование группы доступа"):
            access_groups_page.update_access_group()
            access_groups_page.check_access_group()

        with allure.step("Добавление пользователя в группу доступа"):
            access_groups_page.add_user_in_access_group()

        with allure.step("Добавление ML-шаблона в группу доступа"):
            access_groups_page.access_groups_settings()
            access_groups_page.add_pattern_in_access_group()
            access_groups_page.check_pattern_in_access_group()

        with allure.step("Добавление ML-эксперимента в группу доступа"):
            access_groups_page.access_groups_settings()
            access_groups_page.add_experiment_in_access_group()
            access_groups_page.check_experiment_in_access_group()

        with allure.step("Добавление ML-эксперимента в группу доступа"):
            access_groups_page.delete_access_group()

    assert "Тест завершен"