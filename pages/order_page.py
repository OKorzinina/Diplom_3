import allure
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    locators_class = OrderPageLocators

    @allure.step("Проверить видимость карточек заказов")
    def is_order_cards_visible(self):
        return self.is_element_visible(OrderPageLocators.ORDER_CARDS, timeout=10)
    
    @allure.step("Кликнуть на первую карточку заказа")
    def click_first_order_card(self):
        self.click(OrderPageLocators.ORDER_CARDS)
    
    @allure.step("Проверить открытие модального окна заказа")
    def is_order_modal_open(self):
        return self.is_element_visible(OrderPageLocators.ORDER_MODAL, timeout=5)
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click(OrderPageLocators.ORDER_MODAL_CLOSE)
        self.wait_for_invisible(OrderPageLocators.ORDER_MODAL, timeout=5)
    
    @allure.step("Проверить видимость раздела 'В работе'")
    def is_in_progress_section_visible(self):
        return self.is_element_visible(OrderPageLocators.IN_PROGRESS_SECTION, timeout=10)