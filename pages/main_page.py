import allure
import re
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):
    locators_class = MainPageLocators

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_url(Urls.BASE_URL)
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BUTTON_SIMPLE, timeout=10)
        return self
    
    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON_SIMPLE)
    
    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON_SIMPLE)
    
    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click(MainPageLocators.FLUORESCENT_BUN)
        self.wait_for_visible(MainPageLocators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Проверить открытие модального окна")
    def is_modal_open(self):
        """Проверить, открыто ли модальное окно (видимо и присутствует)"""
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL, timeout=2)
    
    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        return self.get_text(MainPageLocators.MODAL_TITLE)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        # Проверим, открыто ли окно - используем is_modal_open() для единообразия
        if not self.is_modal_open():
            raise AssertionError("Попытка закрыть неоткрытое модальное окно")

        # Пробуем закрыть основную кнопку закрытия
        try:
            self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        except TimeoutException:
            # Если основная кнопка не найдена, пробуем альтернативную
            try:
                self.click(MainPageLocators.MODAL_CLOSE_BUTTON_ALT)
            except TimeoutException:
                # Если альтернативная кнопка не найдена, пробуем закрыть через ESCAPE
                try:
                    self.send_escape_key()
                except Exception:
                    # Последняя попытка - клик вне модального окна
                    self.click_outside_modal()
        
        # Дождаться, пока модальное окно закроется
        return self.wait_for_modal_close()
    
    @allure.step("Отправить клавишу ESCAPE")
    def send_escape_key(self):
        """Отправить клавишу ESCAPE с помощью ActionChains"""
        self.send_keys_escape()
    
    @allure.step("Кликнуть вне модального окна")
    def click_outside_modal(self):
        """Кликнуть вне модального окна для его закрытия"""
        self.click_by_offset(10, 10)
    
    @allure.step("Дождаться закрытия модального окна")
    def wait_for_modal_close(self, timeout=5):
        """Ожидать закрытия модального окна"""
        try:
            # Ждем, пока модальное окно станет невидимым
            self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL, timeout=timeout)
            return True
        except TimeoutException:
            self.take_screenshot("modal_not_closed")
            # Проверим еще раз, возможно окно все же закрылось
            return not self.is_modal_open()
    
    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        try:
            if self.is_element_present(MainPageLocators.INGREDIENT_COUNTER, timeout=2):
                counter_text = self.get_text(MainPageLocators.INGREDIENT_COUNTER)
                numbers = re.findall(r'\d+', counter_text)
                return int(numbers[0]) if numbers else 0
            return 0
        except TimeoutException:
            return 0
    
    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        """Добавить ингредиент в конструктор"""
        initial_counter = self.get_ingredient_counter()
        
        # Кликаем на ингредиент (открывает модальное окно)
        self.click_ingredient()
        
        # Закрываем модальное окно если оно открылось
        if self.is_modal_open():
            self.close_modal()
        
        # Ждём изменения счётчика
        self.wait_for_counter_change(initial_counter)
        
        # Получаем новое значение
        return self.get_ingredient_counter()
    
    @allure.step("Ожидать изменения счетчика")
    def wait_for_counter_change(self, initial_value, timeout=5):
        """Ожидание изменения счётчика"""
        try:
            self.wait_for_condition(
                lambda driver: self.get_ingredient_counter() != initial_value,
                timeout=timeout
            )
            return True
        except TimeoutException:
            self.take_screenshot("counter_not_changed")
            return False
    
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        """Альтернативный метод добавления ингредиента"""
        initial_counter = self.get_ingredient_counter()
        
        try:
            # Используем drag-and-drop из BasePage
            self.drag_and_drop(
                MainPageLocators.FLUORESCENT_BUN,
                MainPageLocators.BUN_DROP_AREA
            )
            
            # Ждём изменения счётчика
            self.wait_for_counter_change(initial_counter)
            return self.get_ingredient_counter()
        except Exception as e:
            self.take_screenshot("drag_and_drop_failed")
            return initial_counter
    
    @allure.step("Получить текущий URL")
    def get_current_page_url(self):
        return self.get_current_url()
