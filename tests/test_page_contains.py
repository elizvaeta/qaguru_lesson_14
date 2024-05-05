import allure

from models.pages.career_page import career_page


def test_have_info_blocks():
    with allure.step("Открытие страницы"):
        career_page.open()

    with allure.step("Проверка наличия блоков с информацией"):
        career_page.should_have_info_blocks()


def test_go_to_vacancies():
    with allure.step("Открытие страницы"):
        career_page.open()

    with allure.step("Проверка перехода на страницу с вакансиями"):
        career_page.should_go_to_vacancies()


def test_go_to_blog():
    with allure.step("Открытие страницы"):
        career_page.open()

    with allure.step("Проверка перехода на страницу блога"):
        career_page.should_go_to_blog()
