import allure
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from urls import Urls


class OrderPage(BasePage):
    
    locators_class = OrderPageLocators
    
    @allure.step("Открыть ленту заказов")
    def open(self):
        self.open_url(Urls.ORDER_FEED_URL)
        self.wait_for_visible(OrderPageLocators.ORDER_FEED_TITLE)
    
    @allure.step("Получить количество 'Выполнено за всё время'")
    def get_total_orders_count(self):
        """Возвращает текст счетчика"""
        return self.get_text(OrderPageLocators.TOTAL_ORDERS)
    
    @allure.step("Получить количество 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        """Возвращает текст счетчика"""
        return self.get_text(OrderPageLocators.TODAY_ORDERS)
    
    @allure.step("Получить счетчик 'Выполнено за всё время' как число")
    def get_total_orders_count_as_number(self):
        """Возвращает числовое значение счетчика"""
        text = self.get_total_orders_count()
        return self._extract_number_from_text(text)
    
    @allure.step("Получить счетчик 'Выполнено за сегодня' как число")
    def get_today_orders_count_as_number(self):
        """Возвращает числовое значение счетчика"""
        text = self.get_today_orders_count()
        return self._extract_number_from_text(text)
    
    def _extract_number_from_text(self, text):
        """Вспомогательный метод для извлечения числа из текста"""
        if not text:
            return 0
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else 0
    
    @allure.step("Ждать появления карточек заказов")
    def wait_for_order_cards(self, timeout=10):
        """Ждёт появления хотя бы одной карточки заказа."""
        try:
            WebDriverWait(self.driver, timeout).until(
                # ИСПРАВЛЕНИЕ: используем driver.find_elements напрямую
                lambda driver: len(driver.find_elements(*OrderPageLocators.ORDER_CARDS)) > 0
            )
            return True
        except TimeoutException:
            self.take_screenshot("no_order_cards")
            return False
    
    @allure.step("Получить все карточки заказов")
    def get_order_cards(self):
        # ИСПРАВЛЕНИЕ: используем driver.find_elements напрямую
        return self.driver.find_elements(*OrderPageLocators.ORDER_CARDS)
    
    @allure.step("Получить номера заказов 'В работе'")
    def get_in_progress_order_numbers(self):
        """Получить список номеров заказов из раздела 'В работе'"""
        # ИСПРАВЛЕНИЕ: используем driver.find_elements напрямую
        elements = self.driver.find_elements(*OrderPageLocators.IN_PROGRESS_ORDER_NUMBERS)
        return [elem.text.strip() for elem in elements if elem.text.strip()]
    
    @allure.step("Кликнуть на заказ в ленте")
    def click_order(self, order_index=0):
        orders = self.get_order_cards()
        if orders and order_index < len(orders):
            # ИСПРАВЛЕНИЕ: используем click() из BasePage или напрямую
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(orders[order_index])
            )
            orders[order_index].click()
            self.wait_for_order_modal()
        else:
            raise ValueError(f"Нет заказа с индексом {order_index}")
    
    @allure.step("Ждать открытия модального окна заказа")
    def wait_for_order_modal(self, timeout=5):
        """Ждёт открытия модального окна с деталями заказа"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(OrderPageLocators.ORDER_MODAL)
            )
            return True
        except TimeoutException:
            self.take_screenshot("order_modal_not_opened")
            return False
    
    @allure.step("Ждать закрытия модального окна заказа")
    def wait_for_order_modal_to_close(self, timeout=5):
        """Ждёт закрытия модального окна"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(OrderPageLocators.ORDER_MODAL)
            )
            return True
        except TimeoutException:
            self.take_screenshot("order_modal_not_closed")
            return False
    
    @allure.step("Получить номер заказа из модального окна")
    def get_modal_order_number(self):
        if self.is_element_present(OrderPageLocators.MODAL_ORDER_NUMBER):
            text = self.get_text(OrderPageLocators.MODAL_ORDER_NUMBER)
            # Убираем нецифровые символы
            numbers = re.findall(r'\d+', text)
            return numbers[0] if numbers else ""
        return ""
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        if self.is_element_present(OrderPageLocators.CLOSE_MODAL_BUTTON):
            # Используем метод click из BasePage
            self.click(OrderPageLocators.CLOSE_MODAL_BUTTON)
        self.wait_for_order_modal_to_close()
    
    @allure.step("Обновить страницу")
    def refresh(self):
        self.driver.refresh()
        self.wait_for_page_load()
        self.wait_for_visible(OrderPageLocators.ORDER_FEED_TITLE)
    
    @allure.step("Проверить наличие раздела 'В работе'")
    def is_in_progress_section_present(self):
        return self.is_element_present(OrderPageLocators.IN_PROGRESS_SECTION)
    
    @allure.step("Проверить, открыто ли модальное окно")
    def is_modal_open(self):
        return self.is_element_present(OrderPageLocators.ORDER_MODAL)
