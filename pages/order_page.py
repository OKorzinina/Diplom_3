

import allure
import time  
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from urls import Urls


class OrderPage(BasePage):
    # Добавляем ссылку на класс локаторов
    locators_class = OrderPageLocators
    
    @allure.step("Открыть ленту заказов")
    def open(self):
        self.driver.get(Urls.ORDER_FEED_URL)
        self.wait_for_visible(OrderPageLocators.ORDER_FEED_TITLE)
    
    @allure.step("Получить количество 'Выполнено за всё время'")
    def get_total_orders_count(self):
        count_text = self.get_text(OrderPageLocators.TOTAL_ORDERS)
        
        try:
            return int(count_text.replace(',', '').strip())
        except ValueError:
           
            return count_text.strip()
    
    @allure.step("Получить количество 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        count_text = self.get_text(OrderPageLocators.TODAY_ORDERS)
        
        try:
            return int(count_text.replace(',', '').strip())
        except ValueError:
            
            return count_text.strip()
    
    @allure.step("Получить заказы 'В работе'")
    def get_orders_in_progress(self):
        orders = self.find_elements(OrderPageLocators.ORDERS_IN_PROGRESS)
        return [order.text for order in orders if order.text.strip()]
    
    @allure.step("Кликнуть на заказ в ленте")
    def click_order(self, order_index=0):
        orders = self.find_elements(OrderPageLocators.ORDER_CARDS)
        if orders and order_index < len(orders):
            orders[order_index].click()
            self.wait_for_visible(OrderPageLocators.ORDER_MODAL)
        else:
            raise ValueError(f"Нет заказа с индексом {order_index}")
    
    @allure.step("Получить номер заказа из модального окна")
    def get_modal_order_number(self):
        if self.is_element_present(OrderPageLocators.MODAL_ORDER_NUMBER):
            text = self.get_text(OrderPageLocators.MODAL_ORDER_NUMBER)
            return text.replace("#", "").strip()
        return ""
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.close_modal()
    
    @allure.step("Проверить наличие заказов в работе")
    def has_orders_in_progress(self):
        return self.is_element_present(OrderPageLocators.IN_PROGRESS_SECTION)
    
    @allure.step("Проверить наличие выполненных заказов")
    def has_orders_done(self):
        return self.is_element_present(OrderPageLocators.DONE_SECTION)
    
    @allure.step("Проверить, открыто ли модальное окно")
    def is_modal_open(self):
        return self.is_element_present(OrderPageLocators.ORDER_MODAL)
    
    @allure.step("Обновить страницу")
    def refresh(self):
        self.driver.refresh()
        time.sleep(2)  # Ждем обновления
    
    @allure.step("Проверить наличие заказов в ленте")
    def has_orders(self):
        return self.is_element_present(OrderPageLocators.ORDER_CARDS, timeout=5)