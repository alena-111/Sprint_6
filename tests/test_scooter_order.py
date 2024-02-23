import allure
import pytest

from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators as locator


class TestScooterOrder:
    @pytest.mark.parametrize(
        'order_button, name, second_name, address, metro, phone_number'
        ', date, rental_period, scooter_color, comment',
        [('button_order_top', 'Иван', 'Иванов', 'Арбатская 1',
          'Сокольники', '89688888888', '23.04.2024', 'пятеро суток',
          'черный жемчуг', 'Доставка до 14.00'),
         ('button_order', 'Маша', 'Сидорова', 'Ленинская 1',
          'Бульвар Рокоссовского', '89666677332', '29.02.2024', 'сутки',
          'серая безысходность', 'Стучите громче')],
        ids=['Проверка с первым набором данных',
             'Проверка со вторым набор данных'])
    @allure.title("Оформить заказ через кнопку Заказать: {order_button}")
    @allure.description(
        'Создаем заказ, возвращаемся на главную страницу и переходим на Дзен')
    def test_create_order(self, driver, order_button, name, second_name,
                          address, metro, phone_number, date, rental_period,
                          scooter_color, comment):
        order_page = OrderPage(driver)
        order_page.go_to_base_url()
        order_page.wait_for_load_main_page()
        params = {'button_order_top': locator.button_order_top,
                  'button_order': locator.button_order,
                  'Сокольники': locator.sokolniki,
                  'Бульвар Рокоссовского': locator.rokossovski,
                  'пятеро суток': locator.five_days_order,
                  'сутки': locator.one_days_order,
                  'черный жемчуг': locator.black_pearl_checkbox,
                  'серая безысходность': locator.grey_checkbox}
        # параметризируем кнопку заказать order_top
        order_page.click_on_button_order(params[order_button])
        order_page.element_displayed(locator.for_whom_scooter)
        # персональные данные
        order_page.input_personal_data(name, second_name, address,
                                       params[metro],
                                       phone_number)
        order_page.click_on_button_next()
        order_page.element_displayed(locator.order_final_button)
        # данные заказа
        order_page.input_renta_data(date, params[rental_period],
                                    params[scooter_color],
                                    comment)
        order_page.click_on_button_create_order()
        order_page.element_displayed(locator.yes_button)

        order_page.click_on_yes_button()

        order_page.element_displayed(locator.order_status)

        order_page.click_on_order_status()

        order_page.click_on_scooter()

        order_page.current_url_match()

        order_page.click_on_yandex()

        order_page.swich_between_tabs()

        assert order_page.current_url_match(locator.dzen_url)

    @allure.title("Переход на главную страницу при нажатии на Самокат")
    @allure.description(
        'Нажинаем на самокат, переходим на главную страницу')
    def test_click_on_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_custom_url('order')
        order_page.click_on_scooter()
        assert order_page.current_url_match()
