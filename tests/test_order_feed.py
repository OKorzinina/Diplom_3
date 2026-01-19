from pages import main_page
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.auth_page import AuthPage
import allure
from urls import Urls

class TestOrderFeed:

    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_total_orders_counter_increases(self, driver, creating_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        auth_page = AuthPage(driver)
        _, email, password = creating_user
# Авторизация
        auth_page.open()
        auth_page.login(email, password)

# 1. Получаем начальное значение (заходим в ленту)
        main_page.click_order_feed()
        order_page.wait_for_order_feed_loaded()
        #driver.get(Urls.ORDER_FEED_URL) #ДОБАВИЛА
        order_page.get_to_go_feed() #ЗАМЕНА driver 
        initial_total = order_page.get_total_orders_counter()

# 2. Создаем заказ через UI
        main_page.click_constructor()
        main_page.drag_ingredient_to_constructor()
        main_page.click_make_order_button()

# 3. Ждем завершения создания заказа
        main_page.wait_for_order_id_visible()
        main_page.close_modal()
        main_page.wait_for_modal_closed()

# 4. Переходим в ленту и ждем обновления счетчика
        main_page.click_order_feed()
        order_page.wait_for_order_feed_loaded()
        order_page.wait_for_total_counter_to_change(initial_total)

        #driver.get(Urls.ORDER_FEED_URL) #ДОБАВИЛА
        order_page.get_to_go_feed() #ЗАМЕНА driver
        final_total = order_page.get_total_orders_counter()
        assert final_total > initial_total

 
    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_today_orders_counter_increases(self, driver, creating_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        auth_page = AuthPage(driver)
        _, email, password = creating_user

        # Авторизация
        auth_page.open()
        auth_page.login(email, password)

        # 1. Получаем начальное значение счётчика
        main_page.click_order_feed()
        order_page.wait_for_order_feed_loaded()
        #driver.get(Urls.ORDER_FEED_URL)
        order_page.get_to_go_feed() #ЗАМЕНА driver
        initial_today = order_page.get_today_orders_counter()

        # 2. Создаем заказ через UI
        main_page.click_constructor()
        main_page.drag_ingredient_to_constructor()
        main_page.click_make_order_button()


        # 3. Ждем появления номера заказа 
        main_page.wait_for_order_id_visible()
        main_page.close_modal()
        main_page.wait_for_modal_closed()

        # 4. Переходим в ленту заказов
        main_page.click_order_feed()
        order_page.wait_for_order_feed_loaded()
        order_page.wait_for_today_counter_to_change(initial_today)

        #driver.get(Urls.ORDER_FEED_URL)
        order_page.get_to_go_feed() #ЗАМЕНА driver
        final_today = order_page.get_today_orders_counter()

        # Проверяем увеличение
        assert final_today > initial_today

     

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_order_number_appears_in_progress(self, driver, creating_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        auth_page = AuthPage(driver)
        _, email, password = creating_user

        # Авторизация
        auth_page.open()
        auth_page.login(email, password)

        # Создание заказа
        main_page.click_constructor()
        main_page.drag_ingredient_to_constructor()
        main_page.click_make_order_button()

        # Получаем номер из модалки
        main_page.wait_for_order_id_visible()
        order_number = main_page.get_order_id_from_modal()

        main_page.close_modal()
        main_page.wait_for_modal_closed()

        # Проверка в ленте
        main_page.click_order_feed()
        order_page.wait_for_order_feed_loaded()
                
        # Вызываем метод для проверки наличия номера в списке 
        assert order_page.is_order_in_progress_section(order_number) is True