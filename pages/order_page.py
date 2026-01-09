import allure
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):  
    locators_class = OrderPageLocators

    @allure.step("Дождаться появления карточек заказов")
    def wait_for_order_cards_visible(self):
        """Ждем карточки заказов - тест упадет если не появятся"""
        self.wait_for_visible(OrderPageLocators.ORDER_CARDS, timeout=10)
    
    @allure.step("Кликнуть на первую карточку заказа и дождаться модального окна")
    def click_first_order_card_and_wait_modal(self):
        """Линейный сценарий: клик → должно открыться модальное окно"""
        self.click(OrderPageLocators.ORDER_CARDS)
        self.wait_for_visible(OrderPageLocators.ORDER_MODAL, timeout=5)
    
    @allure.step("Дождаться открытия модального окна заказа")
    def wait_for_order_modal_open(self):
        """Ждем открытия модального окна заказа - тест упадет если не откроется"""
        self.wait_for_visible(OrderPageLocators.ORDER_MODAL, timeout=5)
    
    @allure.step("Дождаться закрытия модального окна заказа")
    def wait_for_order_modal_close(self):
        """Ждем закрытия модального окна заказа - тест упадет если не закроется"""
        self.wait_for_invisible(OrderPageLocators.ORDER_MODAL, timeout=5)
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal_and_wait(self):
        """Линейный сценарий: клик → должно закрыться"""
        self.click(OrderPageLocators.ORDER_MODAL_CLOSE)
        self.wait_for_invisible(OrderPageLocators.ORDER_MODAL, timeout=5)
    
    @allure.step("Дождаться появления раздела 'В работе'")
    def wait_for_in_progress_section_visible(self):
        """Ждем раздел 'В работе' - тест упадет если не появится"""
        self.wait_for_visible(OrderPageLocators.IN_PROGRESS_SECTION, timeout=10)