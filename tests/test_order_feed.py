import allure
import time
from pages.base_page import BasePage  
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.auth_page import AuthPage
from helper import CreatedOrder


class TestOrderFeed:

    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_total_orders_counter_increases(self, driver, creating_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        auth_page = AuthPage(driver)
        token, email, password = creating_user

        auth_page.open()
        auth_page.login(email, password)
        main_page.click_order_feed()

        # Получаем начальное значение
        initial_total = int(order_page.get_total_orders_counter())

        # Создаем заказ
        CreatedOrder.created_order(token)

        # Обновляем данные через метод Page Object
        main_page.refresh()
        main_page.click_order_feed()

        # Получаем новое значение
        new_total = int(order_page.get_total_orders_counter())

        # Проверка в конце теста
        assert new_total > initial_total

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_today_orders_counter_increases(self, driver, creating_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        auth_page = AuthPage(driver)
        token, email, password = creating_user

        auth_page.open()
        auth_page.login(email, password)
        main_page.click_order_feed()

        initial_today = int(order_page.get_today_orders_counter())

        # Создаем заказ
        CreatedOrder.created_order(token)

        # Пауза для обработки заказа сервером
        time.sleep(5)
          
        # Обновление данных через метод Page Object
        main_page.refresh()
        main_page.click_order_feed()
        new_today = int(order_page.get_today_orders_counter())
        assert new_today > initial_today

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_order_number_appears_in_progress(self, driver, creating_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        auth_page = AuthPage(driver)
        token, email, password = creating_user

        auth_page.open()
        auth_page.login(email, password)

        # Создаем заказ через API
        order_number = CreatedOrder.created_order(token)

        # Переходим в ленту заказов
        main_page.click_order_feed()

        # Ждем появления заказа
        time.sleep(15)

        # Вызываем метод Page Object
        is_in_progress = order_page.is_order_in_progress_section(order_number)

        # Финальный ассерт
        assert is_in_progress