from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
import selenium.webdriver.common.keys as keys
import selenium.webdriver.common.action_chains as action_chains
from locators.order_page_locators import OrderPageLocators as locator
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Нажимаем на  Заказать')
    def click_on_button_order(self, button):
        super().click_on_element(button)

    @allure.step('Нажимаем на  Далее')
    def click_on_button_next(self):
        super().click_on_element(locator.next_button)

    @allure.step('Ввод перональных данных')
    def input_personal_data(self, name, second_name, address, metro,
                            phone_number):
        self.driver.find_element(*locator.name_input).send_keys(name)
        self.driver.find_element(*locator.second_name_input).send_keys(
            second_name)
        self.driver.find_element(*locator.address_input).send_keys(address)
        metro_st = self.driver.find_element(*locator.metro_input)
        metro_st.click()
        self.driver.find_element(*metro).click()
        self.driver.find_element(*locator.phone_number_input).send_keys(
            phone_number)

    @allure.step('Ввод даты бронирования')
    def input_renta_data(self, date, rental_period, checkbox, comment):
        self.driver.find_element(*locator.date_input).send_keys(date)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(keys.Keys.ENTER)
        action.perform()
        self.driver.find_element(*locator.rental_period_input).click()
        self.driver.find_element(*rental_period).click()
        self.driver.find_element(*checkbox).click()
        self.driver.find_element(*locator.comment_input).send_keys(comment)

    @allure.step('Нажимаем на Заказать')
    def click_on_button_create_order(self):
        super().click_on_element(locator.button_order)

    @allure.step('Нажимаем на кнопку Да')
    def click_on_yes_button(self):
        super().click_on_element(locator.yes_button)

    @allure.step('Нажимаем на Посмотреть статус')
    def click_on_order_status(self):
        super().click_on_element(locator.order_status)

    @allure.step('Нажимаем на Самокат')
    def click_on_scooter(self):
        super().click_on_element(locator.scooter_image)

    @allure.step('Нажимаем на Яндекс')
    def click_on_yandex(self):
        super().click_on_element(locator.yandex)

    @allure.step('Переключаемся на кладку Дзен. Ждем загрузку страницы')
    def swich_between_tabs(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        element = self.driver.find_element(*locator.dzen_search_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
