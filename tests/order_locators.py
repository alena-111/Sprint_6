from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
import selenium.webdriver.common.keys as keys
import selenium.webdriver.common.action_chains as action_chains


class OrderPage:
    button_order_top = [By.XPATH, '//button[@class="Button_Button__ra12g"]']
    button_order = [By.XPATH,
                    '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    for_whom_scooter = [By.XPATH, '//div[text()="Для кого самокат"]']
    name_input = [By.XPATH, '//input[@placeholder="* Имя"]']
    second_name_input = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    address_input = [By.XPATH,
                     '//input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_input = [By.XPATH,
                   '//input[@placeholder="* Станция метро"]']
    sokolniki = [By.XPATH, '//div[text()="Сокольники"]']
    rokossovski = [By.XPATH, '//div[text()="Бульвар Рокоссовского"]']
    phone_number_input = [By.XPATH,
                          '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    next_button = [By.XPATH, '//button[text()="Далее"]']
    date_input = [By.XPATH,
                  '//input[@placeholder="* Когда привезти самокат"]']
    rental_period_input = [By.CLASS_NAME, 'Dropdown-placeholder']
    five_days_order = [By.XPATH, '//div[text()="пятеро суток"]']
    one_days_order = [By.XPATH, '//div[text()="сутки"]']
    black_pearl_checkbox = [By.XPATH, '//input[@id="black"]']
    grey_checkbox = [By.XPATH, '//input[@id="grey"]']
    comment_input = [By.XPATH,
                     '//input[@placeholder="Комментарий для курьера"]']
    order_final_button = [By.XPATH, '//button[text()="Заказать"]']
    pop_up_text = [By.XPATH, '//div[text()="Хотите оформить заказ?"]']
    yes_button = [By.XPATH, '//button[text()="Да"]']
    order_status = [By.XPATH, '//button[text()="Посмотреть статус"]']
    inform_window = [By.XPATH,
                     '//div[text()="Номер заказа: 297895. Запишите его: пригодится, чтобы отслеживать статус"]']
    scooter_image = [By.XPATH, '//img[contains(@alt,"Scooter")]']
    yandex = [By.XPATH, '//img[contains(@alt,"Yandex")]']

    dzen_url = 'https://dzen.ru/?yredirect=true'
    dzen_search_button = [By.XPATH, '//button[text()="Найти"]']

    @allure.step('Иницилизация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загружаем страницу с важными вопросами')
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                self.button_order_top))

    @allure.step('Нажимаем на  Заказать')
    def click_on_button_order(self, driver, button):
        element = self.driver.find_element(*button)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Нажимаем на  Далее')
    def click_on_button_next(self, driver, button):
        element = self.driver.find_element(*button)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Ввод перональных данных')
    def input_personal_data(self, name, second_name, address, metro,
                            phone_number):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.second_name_input).send_keys(second_name)
        self.driver.find_element(*self.address_input).send_keys(address)
        metro_st = self.driver.find_element(*self.metro_input)
        metro_st.click()
        self.driver.find_element(*metro).click()
        self.driver.find_element(*self.phone_number_input).send_keys(
            phone_number)

    @allure.step('Ввод даты бронирования')
    def input_renta_data(self, driver, date, rental_period, checkbox, comment):
        self.driver.find_element(*self.date_input).send_keys(date)
        action = action_chains.ActionChains(driver)
        action.send_keys(keys.Keys.ENTER)
        action.perform()
        self.driver.find_element(*self.rental_period_input).click()
        self.driver.find_element(*rental_period).click()
        self.driver.find_element(*checkbox).click()
        self.driver.find_element(*self.comment_input).send_keys(comment)

    @allure.step('Нажимаем на  Заказать')
    def click_on_button_create_order(self, driver, button):
        element = self.driver.find_element(*button)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Нажимаем на  кнопку Да')
    def click_on_yes_button(self, driver, button):
        element = self.driver.find_element(*button)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Нажимаем на  Посмотреть статус')
    def click_on_order_status(self, driver):
        element = self.driver.find_element(*self.order_status)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Нажимаем на  Самокат')
    def click_on_scooter(self, driver):
        element = self.driver.find_element(*self.scooter_image)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Нажимаем на  Яндекс')
    def click_on_yandex(self, driver):
        element = self.driver.find_element(*self.yandex)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Переключаемся на кладку Дзен. Ждем загрузку страницы')
    def swich_between_tabs(self, driver):
        driver.switch_to.window(driver.window_handles[1])
        element = self.driver.find_element(*self.dzen_search_button)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
