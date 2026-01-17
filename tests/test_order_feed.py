from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.auth_page import AuthPage
import allure

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

        final_total = order_page.get_total_orders_counter()
        assert final_total > initial_total

    
    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_today_orders_counter_increases(self, driver, creating_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        auth_page = AuthPage(driver)
        _, email, password = creating_user

        print("\n" + "="*60)
        print("НАЧАЛО ТЕСТА: test_today_orders_counter_increases")
        print("="*60)

        # Авторизация
        auth_page.open()
        auth_page.login(email, password)

        # 1. Получаем начальное значение счетчика
        print("\nШаг 1: Получаем начальное значение счетчика")
        main_page.click_order_feed()
        order_page.wait_for_order_feed_loaded()
        initial_today = order_page.get_today_orders_counter()
        print(f"Начальное значение счетчика: {initial_today}")

        # 2. Создаем новый заказ
        print("\nШаг 2: Создаем новый заказ")
        main_page.click_constructor()
        main_page.drag_ingredient_to_constructor()
        main_page.click_make_order_button()
        main_page.wait_for_order_id_visible()
        print("  - Заказ создан, модальное окно появилось")
        main_page.close_modal()
        main_page.wait_for_modal_closed()
        print("  - Модальное окно закрыто")

        # 3. Ждем увеличения счетчика
        print("\nШаг 3: Переходим в ленту заказов")
        main_page.click_order_feed()
        order_page.wait_for_order_feed_loaded()
        print("  - Лента заказов загружена")
        
        # Проверяем счетчик сразу после загрузки
        current_after_load = order_page.get_today_orders_counter()
        print(f"  - Счетчик после загрузки: {current_after_load}")
        print(f"  - Разница: {current_after_load - initial_today}")

        print("\nШаг 4: Обновляем страницу")
        # Используем метод Page Object для обновления страницы
        order_page.refresh_page()
        print("  - Страница обновлена")
        
        # Проверяем счетчик после обновления
        current_after_refresh = order_page.get_today_orders_counter()
        print(f"  - Счетчик после обновления: {current_after_refresh}")
        print(f"  - Разница: {current_after_refresh - initial_today}")

        print("\nШаг 5: Ждем увеличения счетчика")
        # Ждем увеличения счетчика
        #order_page.wait_for_today_counter_to_increase(initial_today)
        order_page.wait_for_today_counter_to_change(initial_today)

        # Получаем конечное значение счетчика
        final_today = order_page.get_today_orders_counter()
        print(f"\nФинальное значение счетчика: {final_today}")
        print(f"Начальное значение: {initial_today}")
        print(f"Увеличение на: {final_today - initial_today}")
        
        # Проверяем увеличение
        print(f"\nПроверка assert: {final_today} > {initial_today} = {final_today > initial_today}")
        assert final_today > initial_today
        
        print("\n" + "="*60)
        print("ТЕСТ УСПЕШНО ЗАВЕРШЕН")
        print("="*60)

    

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
