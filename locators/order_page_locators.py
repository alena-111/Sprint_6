from selenium.webdriver.common.by import By


class OrderPageLocators:
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
