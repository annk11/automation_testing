import re
import time
from playwright.sync_api import expect

from pages.base_page import BasePage
from data.data import DataGenerator
from dotenv import load_dotenv
import os

load_dotenv()

class ExperimentPage(BasePage):
    gateway_url = os.getenv('GATEWAY_URL')
    url = f'http://{gateway_url}/ml/experiments'

    def check_ml_menu(self):
        expect(self.page.get_by_role("complementary").locator("a").filter(has_text="Эксперименты")).to_be_visible()
        expect(self.page.locator("a").filter(has_text="Модели")).to_be_visible()
        expect(self.page.get_by_text("hubКонструктор нейросетей")).to_be_visible()
        expect(self.page.locator("a").filter(has_text="Классические алгоритмы")).to_be_visible()

    def check_experiment_page(self):
        expect(self.page.get_by_role("main")).to_contain_text("Эксперименты")
        expect(self.page.get_by_role("main")).to_contain_text("Список всех ваших экспериментов")

    def create_experiment(self):
        self.page.locator(".q-page-sticky > div > .q-btn").click()
        self.page.get_by_label("Наименование").fill(DataGenerator.name)
        self.page.locator("div").filter(has_text=re.compile(r"^Источник данныхarrow_drop_down$")).nth(1).click()
        self.page.get_by_text("ML-хранилище_ml_resultml_result").click()
        self.page.get_by_text("public").click()
        self.page.get_by_label("Описание").fill(DataGenerator.description)
        self.page.get_by_role("button", name="Создать").click()

    def check_experiment_created(self):
        expect(self.page.get_by_text("Эксперимент сохранен успешно")).to_be_visible()
        expect(self.page.locator("section")).to_contain_text(DataGenerator.name)

    def open_last_experiment(self):
        self.page.locator("div:last-child > .index_wrapper_M6fL4 > .index_panel_svWK0 > .q-btn").click()
        self.page.get_by_text("Открыть эксперимент").click()

    def update_last_experiment(self):
        self.page.locator("div:last-child > .index_wrapper_M6fL4 > .index_panel_svWK0 > .q-btn").click()
        self.page.get_by_text("Редактировать").click()
        self.page.get_by_label("Наименование").fill(DataGenerator.name)
        self.page.get_by_label("Описание").fill(DataGenerator.description)
        self.page.get_by_role("button", name="Сохранить").click()

    def delete_last_experiment(self):
        self.page.locator("div:last-child > .index_wrapper_M6fL4 > .index_panel_svWK0 > .q-btn").click()
        self.page.get_by_text("Удалить").click()
        self.page.get_by_role("button", name="Удалить").click()

    def check_experiment_deleted(self):
        expect(self.page.get_by_role("alert").nth(1)).to_contain_text("Эксперимент успешно удален")

    def check_page_runs_of_experiments(self):
        expect(self.page.get_by_role("main")).to_contain_text("Полный список запусков по всем моделям "
                                                              "эксперимента")

    def create_model(self):
        self.page.get_by_role("main").locator("button").nth(2).click()
        expect(self.page.get_by_text("Добавить модель")).to_be_visible()
        self.page.get_by_label("Наименование", exact=True).click()
        self.page.get_by_label("Наименование", exact=True).fill(DataGenerator.name)
        self.page.get_by_label("Описание", exact=True).click()
        self.page.get_by_label("Описание", exact=True).fill(DataGenerator.description)
        self.page.get_by_role("button", name="Создать").click()

    def check_model_created(self):
        expect(self.page.get_by_role("main")).to_contain_text(DataGenerator.name)
        expect(self.page.get_by_role("main")).to_contain_text("Создан")
        expect(self.page.get_by_role("main")).to_contain_text("1")
        expect(self.page.get_by_role("main")).to_contain_text("Добавить шаг")

    def create_step(self, step_type: str):
        self.page.get_by_role("button", name="Добавить шаг").click()
        self.page.get_by_text(step_type).click()

    def fill_preprocessing_step(self):  #TODO refactor: add NEXT button
        self.page.get_by_role("button",
                              name="Препроцессинг Источник данных Нет данных Объект источника данных "
                                   "Нет данных").click()
        self.page.locator(".index_wrapper_YHBfX > button:nth-child(2)").first.click()
        self.page.get_by_label("Описание").click()
        self.page.get_by_label("Описание").fill(DataGenerator.description)
        self.page.get_by_text("2Набор данных").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Источник данныхarrow_drop_down$")).nth(1).click()
        self.page.get_by_text("ETL-хранилище_ml_demo").click()
        self.page.get_by_text("public").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Объект источника$")).first.click()
        self.page.get_by_role("option", name="attrition", exact=True).locator("div").nth(2).click()
        expect(self.page.locator("form")).to_contain_text("Количество столбцов:")
        self.page.get_by_text("3Выбор признаков").click()
        self.page.get_by_role("button", name="Добавить поле").click()
        self.page.locator(".q-field__native").first.click()
        self.page.get_by_role("option", name="age", exact=True).locator("div").nth(2).click()
        self.page.get_by_role("button", name="Настройка").click()
        self.page.get_by_text("Стандартизация").click()
        self.page.get_by_role("button", name="Применить настройки").click()
        self.page.get_by_role("button", name="Добавить поле").click()
        self.page.locator(".q-field__native").first.click()
        self.page.get_by_role("option", name="attrition").locator("div").nth(2).click()
        self.page.get_by_role("row", name="attrition attrition int8").get_by_role("checkbox").click()
        self.page.get_by_role("button", name="Сохранить").click()

    def fill_parameters_step(self):  #TODO refactor: add NEXT button
        self.page.get_by_role("button", name="Параметры модели Нет данных").click()
        self.page.locator(".index_wrapper_YHBfX > button").first.click()
        self.page.get_by_label("Описание").click()
        self.page.get_by_label("Описание").fill(DataGenerator.description)
        self.page.get_by_text("2Параметры", exact=True).click()
        self.page.locator(".q-field__native").first.click()
        self.page.get_by_role("option", name="Классификация").locator("div").nth(2).click()
        self.page.locator(
            "div:nth-child(2) > .AppSelect_wrap_SkwRi > .q-field > .q-field__inner > "
            ".q-field__control > .q-field__control-container > .q-field__native").click()
        self.page.get_by_text("Классический ML-алгоритм").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Алгоритм$")).first.click()
        self.page.get_by_role("option", name="Логистическая регрессия").locator("div").nth(1).click()
        self.page.get_by_role("button", name="Сохранить").click()

    def fill_training_step(self):  #TODO refactor: add NEXT button
        self.page.get_by_role("button", name="Тренировка Нет данных").click()
        self.page.locator(".index_wrapper_YHBfX > button").first.click()
        self.page.get_by_label("Описание").click()
        self.page.get_by_label("Описание").fill(DataGenerator.description)
        self.page.get_by_text("2Параметры").nth(1).click()
        # self.page.get_by_role("button", name="Далее").click()
        self.page.get_by_label("Объем валидационной выборки").click()
        self.page.get_by_label("Объем валидационной выборки").fill("0.2")
        self.page.locator(
            ".AppSelect_wrap_SkwRi > .q-field > .q-field__inner > .q-field__control > .q-field__control-container > .q-field__native").first.click()
        self.page.get_by_role("option", name="accuracy", exact=True).locator("div").nth(2).click()
        self.page.get_by_role("option", name="precision").locator("div").nth(2).click()
        self.page.get_by_role("option", name="recall").locator("div").nth(2).click()
        self.page.get_by_role("option", name="f1").locator("div").nth(2).click()
        self.page.get_by_role("option", name="roc", exact=True).locator("div").nth(2).click()
        self.page.get_by_role("option", name="roc_auc").locator("div").nth(2).click()
        self.page.get_by_role("option", name="confusion_matrix").locator("div").nth(2).click()
        self.page.locator("label").filter(has_text="accuracy, precision, recall,").locator("i").click()
        self.page.get_by_role("button", name="Сохранить").click()

    def create_link(self):  #TODO REFACTOR
        self.page.get_by_role("button", name="Препроцессинг Источник данных ETL-хранилище_ml_demo (public").click()
        self.page.locator(".vue-flow__pane").click()
        self.page.locator("button:nth-child(6)").click()
        self.page.get_by_role("button", name="Препроцессинг Источник данных ETL-хранилище_ml_demo (public").click()
        self.page.locator(".vue-flow__pane").click()
        self.page.get_by_role("button", name="Тренировка Метрики качества").click()
        self.page.locator(".vue-flow__pane").click(button="right")
        self.page.get_by_role("button", name="Параметры модели Тип задачи").click()
        self.page.locator(".vue-flow__pane").click()
        self.page.get_by_role("button", name="Тренировка Метрики качества").click()

    def run_model(self):
        self.page.locator("button:nth-child(6)").click()
        self.page.locator("div:nth-child(3) > .index_wrapper_YHBfX > button").first.click()
        self.page.locator("div:nth-child(3) > .index_wrapper_YHBfX > button:nth-child(4)").click()
        expect(self.page.get_by_role("main")).to_contain_text("Выполняется")
        time.sleep(20)  #TODO wait_for_selector
        self.page.locator("div:nth-child(3) > .index_wrapper_YHBfX > button:nth-child(4)").click()

    def check_run_finished(self):
        expect(self.page.get_by_role("main")).to_contain_text("Завершен")
        expect(self.page.get_by_role("main")).to_contain_text("1")
        self.page.locator("div").filter(
            has_text=re.compile(r"^fgh Номер запуска1Номер версии1Статус запускаЗавершен$")).get_by_role(
            "button").click()

    def change_run_description(self):
        expect(self.page.get_by_role("heading")).to_contain_text("Редактирование запуска")
        self.page.get_by_label("Описание").click()
        self.page.get_by_label("Описание").fill(DataGenerator.description)
        self.page.get_by_role("button", name="Сохранить").click()
        expect(self.page.get_by_role("main")).to_contain_text(DataGenerator.description)

    def delete_run_model(self):
        self.page.get_by_role("button", name="Назад").click()
        self.page.get_by_label("Таблица данных с {0").locator("button").click()
        self.page.get_by_text("Удалить").click()
        self.page.get_by_role("button", name="Удалить").click()

    def delete_experiment(self):
        self.page.get_by_role("link", name="Эксперименты").click()
        expect(self.page.locator("section")).to_contain_text(DataGenerator.name)
        self.page.locator("div:last-child > .index_wrapper_M6fL4 > .index_panel_svWK0 > .q-btn").click()
        self.page.get_by_text("Удалить").click()
        self.page.get_by_role("button", name="Удалить").click()


def calculate_margin(profit, revenue):
    """Функция для расчета маржинальности."""
    if revenue == 0:
        return 0  # Избегаем деления на ноль
    return (profit / revenue) * 100


def linear_regression(x, y):
    """Реализация линейной регрессии с нуля."""
    n = len(x)

    # Вычисление средних значений
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Вычисление коэффициента b
    b_numerator = np.sum(x * y) - n * x_mean * y_mean
    b_denominator = np.sum(x ** 2) - n * x_mean ** 2
    b = b_numerator / b_denominator

    # Вычисление коэффициента a
    a = y_mean - b * x_mean

    return a, b