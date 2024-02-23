import allure
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажимаем на вопрос')
    def click_on_question(self, question):
        super().click_on_element(question)

    @allure.step('Сопоставляем текст ответа')
    def check_text(self, text):
        self.driver.find_element(*text).is_displayed()
