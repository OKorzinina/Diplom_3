
import allure
import re
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):
    locators_class = MainPageLocators

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_url(Urls.BASE_URL)
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=15)
        return self
    
    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click(MainPageLocators.FLUORESCENT_BUN)
        self.wait_for_visible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Проверить открытие модального окна")
    def is_modal_open(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL, timeout=2)
    
    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        return self.get_text(MainPageLocators.MODAL_TITLE)
    
    @allure.step("Закрыть модальное окно основной кнопкой")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Закрыть модальное окно через ESCAPE")
    def close_modal_with_escape(self):
        self.send_keys_escape()
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Закрыть модальное окно альтернативной кнопкой")
    def close_modal_with_alt_button(self):
        # Клик по оверлею
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON_ALT)
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        if self.is_element_present(MainPageLocators.INGREDIENT_COUNTER, timeout=2):
            counter_text = self.get_text(MainPageLocators.INGREDIENT_COUNTER)
            numbers = re.findall(r'\d+', counter_text)
            return int(numbers[0]) if numbers else 0
        return 0
    
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.FLUORESCENT_BUN,
            MainPageLocators.BUN_DROP_AREA
        )