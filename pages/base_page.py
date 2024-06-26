from playwright.sync_api import Page


class BasePage:
    """
    Базовый класс страницы. Класс содержит общие методы,
    которые могут быть использованы на любой странице.
    """
    url = None

    def __init__(self, page: Page) -> None:
        """
        Инициализация экземпляра BasePage.

        :param page: Экземпляр страницы, который будет
        использоваться для взаимодействия со страницей.
        """
        self.page = page

    def open(self):
        """
        Открывает страницу, указанную в self.URL.
        """
        if self.url:
            self.page.goto(self.url)

    def locator(self, selector: str):
        """
        Ищет элемент по указанному селектору.\n
        - Селектор CSS: button.submit-button
        - Селектор XPath: //button[@id='submit-button']

        :param selector: Селектор элемента, который нужно найти.
        """
        self.page.locator(selector)

    def click_button(self, selector: str):
        """
        Кликает по кнопке, соответствующей указанному селектору.\n
        - Селектор CSS: button.submit-button
        - Селектор XPath: //button[@id='submit-button']

        :param selector: Селектор кнопки, по которой нужно кликнуть.
        """
        self.page.click(selector)

    def click(self, selector: str):
        """
        Кликает по кнопке, соответствующей указанному селектору.
        Н-р: - Селектор CSS: button.submit-button
             - Селектор XPath: //button[@id='submit-button']

        :param selector: Селектор кнопки, по которой нужно кликнуть.
        """
        self.page.click(selector)

    def get_by_label(self, selector: str):
        """
        Позволяет находить элементы ввода по тексту связанного элемента
        <label> или aria-labeledby или по атрибуту aria-label

        :param selector: Селектор элемента ввода, которое нужно найти.
        """
        self.page.get_by_label(selector)

    def fill(self, selector: str, value: str):
        """
        Заполняет поле ввода, выбранное селектором, указанным значением.

        :param selector: Селектор поля ввода, которое нужно заполнить.
        :param value: Значение, которым нужно заполнить поле ввода.
        """
        self.page.fill(selector, value)

    def title(self):
        """
        Возвращает заголовок текущей страницы.

        :return: Заголовок текущей страницы.
        """
        return self.page.title()

    def inner_text(self, selector: str):
        """
        Возвращает текст элемента, выбранного селектором.

        :param selector: Селектор элемента, текст которого нужно получить.
        :return: Текст выбранного элемента.
        """
        return self.page.inner_text(selector)

    def query_selector_all(self, selector):
        """
        Возвращает все элементы на странице, которые соответствуют
        указанному селектору.

        :param selector: Селектор для поиска элементов на странице.
        :return: Список элементов, соответствующих селектору.
        """
        return self.page.query_selector_all(selector)

    def wait_for_selector(self, selector: str):
        """
        Ожидает, пока на странице не появится элемент, соответствующий
        указанному селектору.

        :param selector: Селектор элемента, который нужно дождаться.
        """
        self.page.wait_for_selector(selector)

    def check_element_is_visible(self, selector):
        """
        Проверяет, есть ли элемент на странице, соответствующий
        указанному селектору.

        :param selector: Селектор элемента, которого нужно проверить.
        """

        return self.page.is_visible(selector)

    def scroll_down(self) -> None:
        """
        Прокручивает страницу вниз.
        """
        self.page.keyboard.press("End")

    def click_button_by_role(self, name: str) -> None:
        """
        Метод для клика по кнопке с указанным именем.
        """
        self.page.get_by_role("button", name=name).click()

    def get_by_role_(self, name: str):
        """
        TODO
        """
        self.page.get_by_role(name)

    def get_by_text_(self, text: str):
        """
        TODO
        """
        self.page.get_by_text(text)

    def click_option_by_role(self, name: str):
        """
        Метод для клика по кнопке с указанным именем.
        """
        self.page.get_by_role("option", name=name).locator("div").nth(2).click() #TODO move to login page class

    def bring_to_front(self):
        """
        Метод для перевода страницы на передний план.
        """
        self.page.bring_to_front()

    def screenshot(self, path: str):
        """
        Метод для снимка экрана.
        """
        self.page.screenshot(path=path, full_page=True)

    def wait_for_event(self, event: str):
        """
        Метод для ожидания события.
        """
        self.page.wait_for_event(event)

    def handle_popup(self):
        """
        Метод для обработки всплывающего окна.
        """

        self.wait_for_load_state()
        print(self.title())

    def wait_for_load_state(self):
        """
        Метод для ожидания загрузки состояния.
        """
        self.wait_for_load_state()

    def element_is_visible(self, selector: str):
        return self.page.is_visible(selector)
