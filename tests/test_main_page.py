import allure

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators as locator


class TestMainPage:

    @allure.title(
        'Проверка вопроса - Сколько это стоит? И как оплатить?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_1(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_base_url()
        main_page.wait_for_load_main_page()
        main_page.click_on_question(
            locator.first_question)
        main_page.check_text(locator.first_answer)
        assert main_page.get_attribute_of_element(locator.first_question,
                                                  'aria-expanded') == 'true'

    @allure.title(
        'Проверка вопроса - Хочу сразу несколько самокатов! Так можно?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_2(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_base_url()
        main_page.wait_for_load_main_page()
        main_page.click_on_question(
            locator.second_question)
        main_page.check_text(locator.second_answer)
        assert main_page.get_attribute_of_element(locator.second_question,
                                                  'aria-expanded') == 'true'

    @allure.title(
        'Проверка вопроса - Как рассчитывается время аренды?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_3(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_base_url()
        main_page.wait_for_load_main_page()
        main_page.click_on_question(
            locator.third_question)
        main_page.check_text(locator.third_answer)
        assert main_page.get_attribute_of_element(locator.third_question,
                                                  'aria-expanded') == 'true'

    @allure.title(
        'Можно ли заказать самокат прямо на сегодня?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_4(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_base_url()
        main_page.wait_for_load_main_page()
        main_page.click_on_question(
            locator.fourth_question)
        main_page.check_text(locator.fourth_answer)
        assert main_page.get_attribute_of_element(locator.fourth_question,
                                                  'aria-expanded') == 'true'

    @allure.title(
        'Можно ли продлить заказ или вернуть самокат раньше?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_5(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_base_url()
        main_page.wait_for_load_main_page()
        main_page.click_on_question(
            locator.fifth_question)
        main_page.check_text(locator.fifth_answer)
        assert main_page.get_attribute_of_element(locator.fifth_question,
                                                  'aria-expanded') == 'true'

    @allure.title(
        'Вы привозите зарядку вместе с самокатом?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_6(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_base_url()
        main_page.wait_for_load_main_page()
        main_page.click_on_question(
            locator.sixth_question)
        main_page.check_text(locator.sixth_answer)
        assert main_page.get_attribute_of_element(locator.sixth_question,
                                                  'aria-expanded') == 'true'

    @allure.title(
        'Можно ли отменить заказ?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_7(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_base_url()
        main_page.wait_for_load_main_page()
        main_page.click_on_question(
            locator.seventh_question)
        main_page.check_text(locator.seventh_answer)
        assert main_page.get_attribute_of_element(locator.seventh_question,
                                                  'aria-expanded') == 'true'

    @allure.title(
        'Я жизу за МКАДом, привезёте?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_8(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_base_url()
        main_page.wait_for_load_main_page()
        main_page.click_on_question(
            locator.eighth_question)
        main_page.check_text(locator.eighth_answer)

        assert main_page.get_attribute_of_element(locator.eighth_question,
                                                  'aria-expanded') == 'true'
