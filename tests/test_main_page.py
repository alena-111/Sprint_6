import allure

from main_page_locators import MainPage

BASE_URL = 'https://qa-scooter.praktikum-services.ru/'


class TestMainPage:

    @allure.title(
        'Проверка вопроса - Сколько это стоит? И как оплатить?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_1(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        question_element = main_page.click_on_question(driver,
                                                       main_page.first_question)

        # assert текста выполяется внутри метода check_text
        main_page.check_text(main_page.first_answer)
        assert question_element.get_attribute('aria-expanded') == 'true'

    @allure.title(
        'Проверка вопроса - Хочу сразу несколько самокатов! Так можно?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_2(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        question_element = main_page.click_on_question(driver,
                                                       main_page.second_question)

        # assert текста выполяется внутри метода check_text
        main_page.check_text(main_page.second_answer)
        assert question_element.get_attribute('aria-expanded') == 'true'

    @allure.title(
        'Проверка вопроса - Как рассчитывается время аренды?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_3(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        question_element = main_page.click_on_question(driver,
                                                       main_page.third_question)
        # assert текста выполяется внутри метода check_text
        main_page.check_text(main_page.third_answer)
        assert question_element.get_attribute('aria-expanded') == 'true'

    @allure.title(
        'Можно ли заказать самокат прямо на сегодня?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_4(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        question_element = main_page.click_on_question(driver,
                                                       main_page.fourth_question)
        # assert текста выполяется внутри метода check_text
        main_page.check_text(main_page.fourth_answer)
        assert question_element.get_attribute('aria-expanded') == 'true'

    @allure.title(
        'Можно ли продлить заказ или вернуть самокат раньше?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_5(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        question_element = main_page.click_on_question(driver,
                                                       main_page.fifth_question)
        # assert текста выполяется внутри метода check_text
        main_page.check_text(main_page.fifth_answer)
        assert question_element.get_attribute('aria-expanded') == 'true'

    @allure.title(
        'Вы привозите зарядку вместе с самокатом?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_6(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        question_element = main_page.click_on_question(driver,
                                                       main_page.sixth_question)
        # assert текста выполяется внутри метода check_text
        main_page.check_text(main_page.sixth_answer)
        assert question_element.get_attribute('aria-expanded') == 'true'

    @allure.title(
        'Можно ли отменить заказ?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_7(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        question_element = main_page.click_on_question(driver,
                                                       main_page.seventh_question)
        # assert текста выполяется внутри метода check_text
        main_page.check_text(main_page.seventh_answer)
        assert question_element.get_attribute('aria-expanded') == 'true'

    @allure.title(
        'Я жизу за МКАДом, привезёте?')
    @allure.description('Ищем вопрос на странице и проверяем ответ на него.')
    def test_question_8(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        question_element = main_page.click_on_question(driver,
                                                       main_page.eighth_question)
        # assert текста выполяется внутри метода check_text
        main_page.check_text(main_page.eighth_answer)

        assert question_element.get_attribute('aria-expanded') == 'true'
