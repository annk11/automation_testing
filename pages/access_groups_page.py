from playwright.sync_api import expect

from data.data import UserData, DataGenerator
from pages.base_page import BasePage


class AccessGroupsPage(BasePage):
    url = 'http://bi-tst-01:8082/security/groups'

    def create_access_group(self):
        """
        Создает группу доступа.
        """
        self.page.get_by_role("main").get_by_role("button").nth(2).click()
        self.page.get_by_label("Наименование").fill(DataGenerator.name)
        self.page.get_by_label("Описание").fill(DataGenerator.description)
        self.page.get_by_role("button", name="Сохранить").click()

    def check_access_group(self):
        """
        Проверяет корректность созданной группы доступа.
        """
        expect(self.page.get_by_role("table")).to_contain_text(DataGenerator.name)

    def update_access_group(self):
        """
        Обновляет группу доступа.
        """
        self.page.locator("td").filter(has_text="more_vert").nth(1).click()
        self.page.get_by_text("Редактировать").click()
        self.page.get_by_label("Наименование").fill(DataGenerator.name)
        self.page.get_by_label("Описание").fill(DataGenerator.description)
        self.page.get_by_role("button", name="Сохранить").click()

    def add_user_in_access_group(self):
        """
        Добавляет пользователя в группу доступа.
        """
        self.page.locator("td").filter(has_text="more_vert").nth(1).click()
        self.page.get_by_text("Пользователи").click()
        self.page.get_by_text("Никитина Анастасия Олеговнаnikia").click()
        self.page.get_by_role("button", name="Сохранить").click()

    def access_groups_settings(self):
        """
        Переходит в настройки группы доступа.
        """
        self.page.locator("a").filter(has_text="Группы доступа").click()
        self.page.locator("td").filter(has_text="more_vert").nth(1).click()
        self.page.get_by_text("Настройки").click()

    def add_pattern_in_access_group(self):
        """
        Добавляет ML-шаблон в группу доступа.
        """
        self.page.get_by_text("ML-шаблоны").click()
        self.page.get_by_role("button", name="Добавить").click()
        self.page.get_by_role("row", name="Пользовательский шаблон MLP").get_by_role("checkbox").click()
        self.page.get_by_role("button", name="Выбрать").click()

    def check_pattern_in_access_group(self):
        """
        Проверяет ML-шаблон в группе доступа.
        """
        expect(self.page.get_by_role("table")).to_contain_text("Пользовательский шаблон MLP")

    def add_experiment_in_access_group(self):
        """
        Добавляет ML-эксперимент в группу доступа.
        """
        self.page.get_by_text("Эксперименты").click()
        self.page.get_by_role("button", name="Добавить").click()
        self.page.get_by_role("row", name="Прогнозирование неисправностей оборудования Эксперимент направлен на разработку модели прогнозирования неисправностей оборудования с использованием алгоритмов машинного обучения для улучшения эффективности технического обслуживания и предотвращения потенциальных простоев производственных процессов").get_by_role("checkbox").click()
        self.page.get_by_role("button", name="Выбрать").click()

    def check_experiment_in_access_group(self):
        """
        Проверяет ML-эксперимент в группе доступа.
        """
        expect(self.page.get_by_role("table")).to_contain_text("Прогнозирование неисправностей оборудования")

    def delete_access_group(self):
        """
        Удаляет группу доступа.
        """
        self.page.locator("a").filter(has_text="Группы доступа").click()
        self.page.locator("td").filter(has_text="more_vert").nth(1).click()
        self.page.get_by_text("Удалить").click()
        self.page.get_by_role("button", name="Удалить").click()
