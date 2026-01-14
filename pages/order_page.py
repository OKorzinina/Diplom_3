import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Дождаться загрузки страницы ленты заказов")
    def wait_for_order_feed_loaded(self):
        return self.wait_for_visible(OrderPageLocators.PAGE_HEADER, timeout=15)

    @allure.step("Получить значение счетчика 'Выполнено за все время'")
    def get_total_orders_counter(self):
        element = self.wait_for_visible(OrderPageLocators.TOTAL_ORDERS_COUNTER)
        return element.text.strip()

    @allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    def get_today_orders_counter(self):
        element = self.wait_for_visible(OrderPageLocators.TODAY_ORDERS_COUNTER)
        return element.text.strip()

    @allure.step("Проверить, есть ли заказ {order_number} в разделе 'В работе'")
    def is_order_in_progress_section(self, order_number):
        clean_number = str(order_number).replace('#', '').strip()
        formatted_number = clean_number.zfill(6) 
        dynamic_xpath = (By.XPATH, f"//ul[contains(@class, 'orderList')]//li[text()='{formatted_number}']")
        element = self.wait_for_visible(dynamic_xpath, timeout=20)
        return element.is_displayed()