import allure
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    
    @allure.step("Дождаться загрузки страницы ленты заказов")
    def wait_for_order_feed_loaded(self):
        self.wait_for_visible(OrderPageLocators.PAGE_HEADER, timeout=10)
    
    @allure.step("Получить счетчик 'Выполнено за всё время'")
    def get_total_orders_counter(self):
        self.wait_for_order_feed_loaded()
        return self.get_text(OrderPageLocators.TOTAL_ORDERS_COUNTER)
    
    @allure.step("Получить счетчик 'Выполнено за сегодня'")
    def get_today_orders_counter(self):
        self.wait_for_order_feed_loaded()
        return self.get_text(OrderPageLocators.TODAY_ORDERS_COUNTER)
    
    @allure.step("Получить оба счетчика")
    def get_both_counters(self):
        self.wait_for_order_feed_loaded()
        total = self.get_text(OrderPageLocators.TOTAL_ORDERS_COUNTER)
        today = self.get_text(OrderPageLocators.TODAY_ORDERS_COUNTER)
        return total, today
    
         
    @allure.step("Проверить есть ли заказ в разделе 'В работе'")
    def is_order_in_progress_section(self, order_number):
        self.wait_for_order_feed_loaded()
        
        # Находим список заказов "В работе"
        in_work_list = self.find_element(OrderPageLocators.IN_WORK_LIST)
        
        # Получаем весь текст списка
        list_text = in_work_list.text
        
        # Убираем # из номера заказа
        order_clean = order_number.replace('#', '')
        
        # Проверяем есть ли чистый номер в тексте
        return order_clean in list_text

    @allure.step("Получить все номера заказов из раздела 'В работе'")
    def get_in_progress_order_numbers(self):
        self.wait_for_order_feed_loaded()
        
        # Находим все элементы li в списке "В работе"
        order_elements = self.find_elements(OrderPageLocators.IN_WORK_ORDER_ITEMS)
        
        # Извлекаем номера заказов 
        order_numbers = [element.text.strip() for element in order_elements]
        
        return order_numbers   