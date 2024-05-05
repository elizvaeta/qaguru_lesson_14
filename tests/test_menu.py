import allure

from models.pages.career_page import career_page
from models.pages.menu import menu


def test_have_items():
    with allure.step("Открытие страницы"):
        career_page.open()

    with allure.step("Проверка наличия пунктов меню"):
        menu.should_have_items()
