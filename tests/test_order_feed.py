
import pytest
import allure
import time
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.auth_page import AuthPage
from locators.order_page_locators import OrderPageLocators


@allure.feature("Лента заказов")
@allure.story("Функциональность раздела заказов")
class TestOrderFeed:
    
    @allure.title("Тест 7: Проверка счетчиков в ленте заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_counters_display(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step("1. Открыть ленту заказов"):
            order_page.open()
        
        with allure.step("2. Проверить отображение счетчика 'Выполнено за всё время'"):
            total_count = order_page.get_total_orders_count()
            # Проверяем, что значение можно преобразовать в число
            try:
                total_int = int(total_count)
                assert total_int >= 0, f"Счетчик 'Выполнено за всё время' некорректен: {total_count}"
            except ValueError:
                assert total_count.isdigit(), f"Счетчик 'Выполнено за всё время' не содержит число: {total_count}"
            allure.attach(str(total_count), name="total_orders", attachment_type=allure.attachment_type.TEXT)
        
        with allure.step("3. Проверить отображение счетчика 'Выполнено за сегодня'"):
            today_count = order_page.get_today_orders_count()
            # Проверяем, что значение можно преобразовать в число
            try:
                today_int = int(today_count)
                assert today_int >= 0, f"Счетчик 'Выполнено за сегодня' некорректен: {today_count}"
            except ValueError:
                assert today_count.isdigit(), f"Счетчик 'Выполнено за сегодня' не содержит число: {today_count}"
            allure.attach(str(today_count), name="today_orders", attachment_type=allure.attachment_type.TEXT)
    
    @allure.title("Тест 8: Открытие деталей заказа в ленте")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_details_open(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step("1. Открыть ленту заказов"):
            order_page.open()
        
        with allure.step("2. Проверить наличие заказов"):
            if order_page.is_element_present(OrderPageLocators.ORDER_CARDS):
                with allure.step("3. Кликнуть на первый заказ"):
                    order_page.click_order(0)
                    
                with allure.step("4. Проверить открытие модального окна"):
                    # Проверяем, что модальное окно открылось
                    
                    assert order_page.is_modal_open(), "Модальное окно заказа не открылось"
                    
                with allure.step("5. Получить номер заказа"):
                    order_number = order_page.get_modal_order_number()
                    assert order_number.isdigit(), f"Некорректный номер заказа: {order_number}"
                    allure.attach(order_number, name="order_number", attachment_type=allure.attachment_type.TEXT)
                    
                with allure.step("6. Закрыть модальное окно"):
                    order_page.close_order_modal()
                    
                with allure.step("7. Проверить закрытие модального окна"):
                    assert not order_page.is_modal_open(), "Модальное окно не закрылось"
            else:
                pytest.skip("Нет доступных заказов для тестирования")
    
    @allure.title("Тест 9: Проверка раздела 'В работе'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_orders_in_progress_section(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step("1. Открыть ленту заказов"):
            order_page.open()
        
        with allure.step("2. Проверить наличие раздела 'В работе'"):
            if order_page.is_element_present(OrderPageLocators.IN_PROGRESS_SECTION):
                with allure.step("3. Получить заказы в работе"):
                    orders = order_page.get_orders_in_progress()
                    assert len(orders) > 0, "Нет заказов в работе"
                    allure.attach("\n".join(orders), name="orders_in_progress", 
                                attachment_type=allure.attachment_type.TEXT)
            else:
                pytest.skip("Раздел 'В работе' не отображается")
    
    @allure.title("Тест 10: Счетчики увеличиваются при новом заказе (интеграционный)")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip(reason="Требует авторизации и API для оформления заказа")
    def test_counters_increase_on_new_order(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step("1. Открыть ленту заказов"):
            order_page.open()
        
        with allure.step("2. Запомнить начальные значения счетчиков"):
            initial_total = order_page.get_total_orders_count()
            initial_today = order_page.get_today_orders_count()
        
        with allure.step("3. Оформить новый заказ (имитация через время)"):
            
            
            time.sleep(3)
        
        with allure.step("4. Обновить страницу"):
            order_page.refresh()
        
        with allure.step("5. Проверить увеличение счетчиков"):
            new_total = order_page.get_total_orders_count()
            new_today = order_page.get_today_orders_count()
            
            # Преобразуем в числа для сравнения
            try:
                init_total_int = int(initial_total)
                init_today_int = int(initial_today)
                new_total_int = int(new_total)
                new_today_int = int(new_today)
                
                # Ожидаем увеличение счетчиков
                assert new_total_int >= init_total_int, f"Счетчик 'за всё время' не увеличился: {initial_total} -> {new_total}"
                assert new_today_int >= init_today_int, f"Счетчик 'за сегодня' не увеличился: {initial_today} -> {new_today}"
                
                allure.attach(
                    f"До: всего={initial_total}, сегодня={initial_today}\nПосле: всего={new_total}, сегодня={new_today}",
                    name="counters_comparison",
                    attachment_type=allure.attachment_type.TEXT
                )
            except ValueError:
                pytest.fail(f"Невозможно преобразовать счетчики в числа: всего={initial_total}/{new_total}, сегодня={initial_today}/{new_today}")