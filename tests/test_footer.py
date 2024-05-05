import allure

from models.pages.career_page import career_page
from models.pages.footer import footer


def test_have_social_medias():
    with allure.step("Открытие страницы"):
        career_page.open()

    with allure.step("Проверка наличия ссылок на социальные сети в футере"):
        footer.should_have_social_medias()
