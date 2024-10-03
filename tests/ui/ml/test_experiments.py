import allure

from data.data import UserData
from pages.experiment_page import ExperimentPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.epic('UI')
@allure.feature('Предиктивная аналитика')
@allure.story('Эксперименты')
@allure.link("https://yt.omegafuture.ru/issue/OBI-51", name="OBI-51")
# @allure.testcase("https://yt.omegafuture.ru/issue/OBI-51", name="TC-001")
@allure.description('Проверка функциональности создания, редактирования и удаления ML-эксперимента.')
@allure.tag("Предиктивная аналитика", "БФС")
@allure.severity(allure.severity_level.CRITICAL)
class TestExperiments:
    @allure.title("Создание, редактирование, удаление эксперимента")
    def test_experiments(self, page):
        login_page = LoginPage(page)
        home_page = HomePage(page)
        experiments_page = ExperimentPage(page)

        with allure.step("Открытие страницы входа"):
            login_page.open()

        with allure.step("Ввод логина и пароля"):
            login_page.login(UserData.username, UserData.password)

        with allure.step("Выбор домена"):
            login_page.set_realm()

        with allure.step("Проверка домашней страницы"):
            home_page.check_home_page()
            home_page.check_menu_availability()

        with allure.step("Проверка доступности блока ML"):
            home_page.check_ml_menu()
            home_page.click_to_ml()

        with allure.step("Проверка меню блока ML"):
            experiments_page.check_ml_menu()
            experiments_page.check_experiment_page()

        with allure.step("Создание эксперимента"):
            experiments_page.create_experiment()
            experiments_page.check_experiment_created()

        with allure.step("Редактирование эксперимента"):
            experiments_page.update_last_experiment()

        with allure.step("Удаление эксперимента"):
            experiments_page.delete_last_experiment()
            experiments_page.check_experiment_deleted()

    assert "Тест завершен"