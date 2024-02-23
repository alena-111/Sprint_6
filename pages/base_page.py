from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators.order_page_locators import OrderPageLocators as loc

BASE_URL = 'https://qa-scooter.praktikum-services.ru/'


class BasePage:
    @allure.step('Иницилизация драйвера')
    def __init__(self, driver):
        self.driver = driver
        self.BASE_URL = BASE_URL

    @allure.step('Открываем главную страницу самокатов')
    def go_to_base_url(self):
        self.driver.get(self.BASE_URL)

    @allure.step('Ждем полной загрузки главной страницы')
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                loc.button_order_top))

    @allure.step('Открываем страницу')
    def go_to_custom_url(self, url: str):
        self.driver.get(self.BASE_URL + url)

    @allure.step('Сравниваем текущий url страницы')
    def current_url_match(self, url: str = BASE_URL):
        match = url == self.driver.current_url
        return match

    @allure.step('Ожидаем кликабельности и нажимаем на элемент')
    def click_on_element(self, button):
        element = self.driver.find_element(*button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Элемент отображается на странице')
    def element_displayed(self, element):
        self.driver.find_element(
            *element).is_displayed()

    @allure.step('У нужного элемента присутствует аттрибут')
    def get_attribute_of_element(self, locator, attribute):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(element))
        return element.get_attribute(attribute)
