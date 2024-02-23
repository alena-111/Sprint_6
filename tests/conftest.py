import pytest
from selenium import webdriver
import allure


@pytest.fixture()
@allure.title('set up - Запуск браузера, tear down - Закрытие браузера')
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(7)
    yield driver
    driver.quit()
