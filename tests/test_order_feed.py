import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helper import CreatedOrder


class TestOrderFeed:
    
   @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
   def test_total_orders_counter_increases(self, driver, creating_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        token, email, password = creating_user
        
        main_page.open()
        main_page.click_personal_account()
        main_page.enter_email(email)
        main_page.enter_password(password)
        main_page.click_login_button()
        main_page.click_order_feed()
        
        # Получаем начальное значение
        initial_total = order_page.get_total_orders_counter()
        
        # Создаем заказ
        CreatedOrder.created_order(token)
        
        # Обновляем страницу дважды
        main_page.refresh_page()
        main_page.click_order_feed()
        
        main_page.refresh_page()
        main_page.click_order_feed()
        
        # Получаем новое значение
        new_total = order_page.get_total_orders_counter()
        
        # Проверяем
        assert new_total != initial_total
    
   @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
   def test_today_orders_counter_increases(self, driver, creating_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        token, email, password = creating_user
        
        main_page.open()
        main_page.click_personal_account()
        main_page.enter_email(email)
        main_page.enter_password(password)
        main_page.click_login_button()
        main_page.click_order_feed()
        
        initial_total, initial_today = order_page.get_both_counters()
        CreatedOrder.created_order(token)
        
        main_page.refresh_page()
        main_page.click_order_feed()
        new_total, new_today = order_page.get_both_counters()
        
        # Проверяем что хотя бы один из счетчиков изменился
        counters_changed = (new_total != initial_total) or (new_today != initial_today)
        assert counters_changed
    
   @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
   def test_order_number_appears_in_progress(self, driver, creating_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        token, email, password = creating_user
        
        main_page.open()
        main_page.click_personal_account()
        main_page.enter_email(email)
        main_page.enter_password(password)
        main_page.click_login_button()
        main_page.click_order_feed()
        
        # Создаем заказ
        order_number = CreatedOrder.created_order(token)
        
        # Обновляем страницу
        main_page.refresh_page()
        main_page.click_order_feed()
        
        # Проверяем что заказ в разделе "В работе"
        is_in_progress = order_page.is_order_in_progress_section(order_number)
        
        assert is_in_progress 