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
    
    @allure.step("Кликнуть на ингредиент и дождаться открытия модального окна")
    def click_ingredient_and_wait_modal(self):
        """Линейный сценарий: клик → должно открыться"""
        self.click(MainPageLocators.FLUORESCENT_BUN)
        self.wait_for_visible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Дождаться открытия модального окна ингредиента")
    def wait_for_ingredient_modal_open(self):
        """Ждем открытия модального окна - тест упадет если не откроется"""
        self.wait_for_visible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Дождаться закрытия модального окна ингредиента")
    def wait_for_ingredient_modal_close(self):
        """Ждем закрытия модального окна - тест упадет если не закроется"""
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        return self.get_text(MainPageLocators.MODAL_TITLE)
    
    @allure.step("Закрыть модальное окно основной кнопкой")
    def close_modal_and_wait(self):
        """Линейный сценарий: клик → должно закрыться"""
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Закрыть модальное окно через ESCAPE")
    def close_modal_with_escape_and_wait(self):
        """Линейный сценарий: ESC → должно закрыться"""
        self.send_keys_escape()
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Закрыть модальное окно альтернативной кнопкой")
    def close_modal_with_alt_button_and_wait(self):
        """Линейный сценарий: клик → должно закрыться, если кнопки нет - тест падает"""
        # ПРЯМОЙ КЛИК БЕЗ ПРЕДВАРИТЕЛЬНЫХ ПРОВЕРОК
        
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON_ALT)
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        """Получить значение счетчика ингредиента - ЛИНЕЙНАЯ ВЕРСИЯ БЕЗ ВЕТВЛЕНИЙ"""
        # Находим элемент счетчика 
        element = self.find_element(MainPageLocators.INGREDIENT_COUNTER)
        counter_text = element.text
        numbers = re.findall(r'\d+', counter_text)
        return int(numbers[0]) if numbers else 0
    
    @allure.step("Дождаться появления счетчика ингредиента")
    def wait_for_ingredient_counter_visible(self):
        """Ждем появления счетчика - тест упадет если не появится"""
        self.wait_for_visible(MainPageLocators.INGREDIENT_COUNTER, timeout=5)
    
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        """Перетаскивание ингредиента - если не получается, тест падает"""
        self.drag_and_drop(
            MainPageLocators.FLUORESCENT_BUN,
            MainPageLocators.BUN_DROP_AREA
        )
    
    @allure.step("Проверить что счетчик увеличился")
    def verify_counter_increased(self, initial_counter):
        """Линейная проверка: счетчик должен быть больше начального"""
        new_counter = self.get_ingredient_counter()
        if new_counter <= initial_counter:
            raise AssertionError(
                f"Счетчик не увеличился после добавления ингредиента: "
                f"было {initial_counter}, стало {new_counter}"
            )
        return new_counter