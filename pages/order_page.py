import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    locators = OrderPageLocators

    @allure.step("Дождаться загрузки страницы ленты заказов")
    def wait_for_order_feed_loaded(self):
        self.wait_for_url_contains('/feed')
        self.wait_for_visible(self.locators.TOTAL_ORDERS_COUNTER, timeout=25)

    @allure.step("Получить счетчик 'Выполнено за все время'")
    def get_total_orders_counter(self):
        element = self.find_element(self.locators.TOTAL_ORDERS_COUNTER_FEED) #FEED ДОБАВЛЕНО
        count = "".join(filter(str.isdigit, element.text))
        return int(count)

    @allure.step("Получить счетчик 'Выполнено за сегодня'")
    def get_today_orders_counter(self):
        element = self.find_element(self.locators.TODAY_ORDERS_COUNTER_FEED) #FEED ДОБАВЛЕНО
        count = "".join(filter(str.isdigit, element.text))
        return int(count)

    @allure.step("Ожидание изменения счетчика 'Выполнено за все время'")
    def wait_for_total_counter_to_change(self, initial_value):
        self.wait_until_condition(lambda driver: self.get_total_orders_counter() != initial_value)
 #был скрыт
    @allure.step("Ожидание изменения счетчика 'Выполнено за сегодня'")
    def wait_for_today_counter_to_change(self, initial_value):
        #self.wait_until_condition(lambda driver: self.get_today_orders_counter() != initial_value)
        self.wait_until_condition(lambda driver: self.get_today_orders_counter() != initial_value)

    @allure.step("Проверить наличие заказа {order_number} в разделе 'В работе'")
    def is_order_in_progress_section(self, order_number):
        clean_number = str(order_number).replace('#', '').strip()
        formatted_number = f"0{clean_number}"[-6:] 
        order_locator = (By.XPATH, f"//*[contains(@class, 'orderListReady')]//li[text()='{formatted_number}']")

        element = self.wait_for_presence(order_locator, timeout=40)
        return element.is_displayed()

    @allure.step("Обновить страницу ленты заказов")
    def refresh_page(self):
        super().refresh_page()
        self.wait_for_order_feed_loaded()