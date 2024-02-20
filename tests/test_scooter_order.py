import allure
import pytest

from order_locators import OrderPage

BASE_URL = 'https://qa-scooter.praktikum-services.ru/'


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
        driver.get(BASE_URL)

        order_page = OrderPage(driver)
        order_page.wait_for_load_main_page()
        params = {'button_order_top': order_page.button_order_top,
                  'button_order': order_page.button_order,
                  'Сокольники': order_page.sokolniki,
                  'Бульвар Рокоссовского': order_page.rokossovski,
                  'пятеро суток': order_page.five_days_order,
                  'сутки': order_page.one_days_order,
                  'черный жемчуг': order_page.black_pearl_checkbox,
                  'серая безысходность': order_page.grey_checkbox}
        # параметризируем кнопку заказать order_top
        order_page.click_on_button_order(driver, params[order_button])
        assert driver.find_element(
            *order_page.for_whom_scooter).is_displayed()
        # персональные данные
        order_page.input_personal_data(name, second_name, address,
                                       params[metro],
                                       phone_number)
        order_page.click_on_button_next(driver, order_page.next_button)
        assert driver.find_element(
            *order_page.order_final_button).is_displayed()
        # данные заказа
        order_page.input_renta_data(driver, date, params[rental_period],
                                    params[scooter_color],
                                    comment)
        order_page.click_on_button_create_order(driver,
                                                order_page.button_order)
        assert driver.find_element(
            *order_page.yes_button).is_displayed()

        order_page.click_on_yes_button(driver,
                                       order_page.yes_button)

        assert driver.find_element(
            *order_page.order_status).is_displayed()

        order_page.click_on_order_status(driver)

        order_page.click_on_scooter(driver)
        assert driver.current_url == BASE_URL

        order_page.click_on_yandex(driver)

        order_page.swich_between_tabs(driver)

        assert driver.current_url == order_page.dzen_url
