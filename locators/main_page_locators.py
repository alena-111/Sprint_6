from selenium.webdriver.common.by import By


class MainPageLocators:
    important_questions = [By.XPATH, '//div[text()="Вопросы о важном"]']
    first_question = [By.ID, 'accordion__heading-0']
    second_question = [By.ID, 'accordion__heading-1']
    third_question = [By.ID, 'accordion__heading-2']
    fourth_question = [By.ID, 'accordion__heading-3']
    fifth_question = [By.ID, 'accordion__heading-4']
    sixth_question = [By.ID, 'accordion__heading-5']
    seventh_question = [By.ID, 'accordion__heading-6']
    eighth_question = [By.ID, 'accordion__heading-7']

    first_answer = [By.XPATH,
                    '//p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]']
    second_answer = [By.XPATH,
                     '//p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]']
    third_answer = [By.XPATH,
                    '//p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]']
    fourth_answer = [By.XPATH,
                     '//p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]']
    fifth_answer = [By.XPATH,
                    '//p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]']
    sixth_answer = [By.XPATH,
                    '//p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]']
    seventh_answer = [By.XPATH,
                      '//p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]']
    eighth_answer = [By.XPATH,
                     '//p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]']
