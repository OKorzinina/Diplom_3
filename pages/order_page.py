import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    # Используем класс локаторов
    locators = OrderPageLocators

    @allure.step("Дождаться загрузки страницы ленты заказов")
    def wait_for_order_feed_loaded(self):
        WebDriverWait(self.driver, 20).until(
            EC.url_contains('/feed')
        )
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.locators.TOTAL_ORDERS_COUNTER)
        )

    @allure.step("Получить счетчик 'Выполнено за все время'")
    def get_total_orders_counter(self):
        """Получает число из счетчика 'Все время'"""
        element = self.find_element(self.locators.TOTAL_ORDERS_COUNTER)
        # Оставляем в строке только цифры и преобразуем в число
        count = "".join(filter(str.isdigit, element.text))
        return int(count)

    @allure.step("Получить счетчик 'Выполнено за сегодня'")
    def get_today_orders_counter(self):
        """Получает число из счетчика 'Сегодня' """
        element = self.find_element(self.locators.TODAY_ORDERS_COUNTER)
        # Оставляем в строке только цифры и преобразуем в число
        count = "".join(filter(str.isdigit, element.text))
        return int(count)

    @allure.step("Ожидание изменения счетчика 'Выполнено за все время'")
    def wait_for_total_counter_to_change(self, initial_value):
        """Ждет, пока текущее значение счетчика станет отличным от начального"""
        WebDriverWait(self.driver, 30).until(
            lambda driver: self.get_total_orders_counter() != initial_value
        )

    @allure.step("Ожидание изменения счетчика 'Выполнено за сегодня'")
    def wait_for_today_counter_to_change(self, initial_value):
        """Ждет, пока значение счетчика 'За сегодня' изменится"""
        WebDriverWait(self.driver, 30).until(
            lambda driver: self.get_today_orders_counter() != initial_value
        )

    @allure.step("Проверить наличие заказа {order_number} в разделе 'В работе'")
    def is_order_in_progress_section(self, order_number):
        # Форматируем номер заказа (например, 123 -> 000123)
        clean_number = str(order_number).replace('#', '').strip()
        formatted_number = f"0{clean_number}"[-6:] 

        order_locator = (By.XPATH, f"//*[contains(@class, 'orderListReady')]//li[text()='{formatted_number}']")

        # Ждем появления элемента в списке
        element = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(order_locator)
        )
        return element.is_displayed()

    @allure.step("Обновить страницу ленты заказов")
    def refresh_page(self):
        self.driver.refresh()
        self.wait_for_order_feed_loaded()



#СТАРЫЙ 

#import allure
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from .base_page import BasePage
#from locators.order_page_locators import OrderPageLocators

#class OrderPage(BasePage):

    #@allure.step("Дождаться загрузки страницы ленты заказов")
    #def wait_for_order_feed_loaded(self):
        #return self.wait_for_visible(OrderPageLocators.PAGE_HEADER, timeout=15)

    #@allure.step("Получить значение счетчика 'Выполнено за все время'")
    #def get_total_orders_counter(self):
        #element = self.wait_for_visible(OrderPageLocators.TOTAL_ORDERS_COUNTER)
        #return element.text.strip()

    #@allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    #def get_today_orders_counter(self):
        #element = self.wait_for_visible(OrderPageLocators.TODAY_ORDERS_COUNTER)
        #return element.text.strip()

    #@allure.step("Проверить, есть ли заказ {order_number} в разделе 'В работе'")
    #def is_order_in_progress_section(self, order_number):
        #clean_number = str(order_number).replace('#', '').strip()
        #formatted_number = clean_number.zfill(6) 
        #dynamic_xpath = (By.XPATH, f"//ul[contains(@class, 'orderList')]//li[text()='{formatted_number}']")
        #element = self.wait_for_visible(dynamic_xpath, timeout=20)
        #return element.is_displayed()