import allure
import logging
import sys

from data.data import UserData
from pages.home_page import HomePage
from pages.login_page import LoginPage

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


@allure.epic('UI')
@allure.feature('Авторизация')
@allure.story('Вход в систему')
@allure.link("https://yt.omegafuture.ru/issue/OBI-1973", name="OBI-1973")
@allure.testcase("https://yt.omegafuture.ru/issue/OBI-1973", name="TC-001")
@allure.description('Проверка функциональности входа пользователя в систему.')
@allure.tag("Авторизация", "БФС")
@allure.severity(allure.severity_level.CRITICAL)
class TestLoginPage:
    @allure.title("Вход в систему")
    def test_login(self, page):
        login_page = LoginPage(page)
        home_page = HomePage(page)

        with allure.step("Открытие страницы входа"):
            logger.info("Открытие страницы входа")
            login_page.open()

        with allure.step("Ввод логина и пароля"):
            logger.info("Ввод логина и пароля")
            login_page.login(UserData.username, UserData.password)

        with allure.step("Выбор домена"):
            logger.info("Выбор домена")
            login_page.set_realm()

        with allure.step("Проверка домашней страницы"):
            logger.info("Проверка домашней страницы")
            home_page.check_home_page()
            home_page.check_menu_availability()

        logger.info("Тест завершен")

    assert "Тест завершен"
