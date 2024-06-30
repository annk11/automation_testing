import allure

from data.data import UserData
from pages.experiment_page import ExperimentPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.severity('CRITICAL')
@allure.description('Сквозной кейс для блока Предиктивной аналитики. Проверяет функциональность'
                    ' создания эксперимента, модели, запуска модели с определенными шагами. В кейсе'
                    ' используется классический алгоритм машинного обучения.')
@allure.epic('UI-tests')
@allure.feature('E2E')
@allure.story('E2E with ML algorithm')
class TestE2EMLAlgorithm:
    def test_e2e_ml(self, page):
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
            experiments_page.open_last_experiment()
            experiments_page.check_page_runs_of_experiments()

        with allure.step("Создание модели"):
            experiments_page.create_model()
            experiments_page.check_model_created()

        with allure.step("Создание шага Препроцессинг"):
            experiments_page.create_step('Препроцессинг')
            experiments_page.fill_preprocessing_step()

        with allure.step("Создание шага Параметры модели"):
            experiments_page.create_step('Параметры модели')
            experiments_page.fill_parameters_step()

        with allure.step("Создание шага Тренировка"):
            experiments_page.create_step('Тренировка')
            experiments_page.fill_training_step()

        with allure.step("Создание связей между шагами"):
            experiments_page.create_link()

        with allure.step("Запуск модели"):
            experiments_page.run_model()
            experiments_page.check_run_finished()
            experiments_page.change_run_description()

        with allure.step("Удаление запуска модели"):
            experiments_page.delete_run_model()

        with allure.step("Удаление эксперимента"):
            experiments_page.delete_experiment()

    assert "Тест завершен"
