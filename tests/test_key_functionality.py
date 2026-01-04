import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestKeyFunctionality:
    
    @allure.title("Тест 1: Переход по клику на 'Конструктор' и 'Лента заказов'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigation_between_constructor_and_order_feed(self, driver):
        """Атомарный тест навигации БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)

        # 1. Открыть главную страницу
        main_page.open()

        # 2. Перейти в ленту заказов
        main_page.click_order_feed()

        # 3. Вернуться в конструктор
        main_page.click_constructor()
    
    @allure.title("Тест 2: Открытие и закрытие модального окна ингредиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_open_and_close(self, driver):
        """Линейный тест модального окна БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)

        # 1. Открыть главную страницу
        main_page.open()

        # 2. Кликнуть на ингредиент и дождаться открытия
        main_page.click_ingredient_and_wait_modal()

        # 3. Закрыть модальное окно основной кнопкой и дождаться закрытия
        main_page.close_modal_and_wait()
    
    @allure.title("Тест 3: Закрытие модального окна через ESCAPE")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_close_with_escape(self, driver):
        """Тест закрытия модального окна клавишей ESC БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_ingredient_and_wait_modal()
        main_page.close_modal_with_escape_and_wait()
    
    @allure.title("Тест 4: Закрытие модального окна альтернативной кнопкой")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_close_with_alt_button(self, driver):
        """Тест закрытия модального окна альтернативной кнопкой БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_ingredient_and_wait_modal()
        # ЛИНЕЙНЫЙ СЦЕНАРИЙ: если кнопки нет - тест ПАДАЕТ
        main_page.close_modal_with_alt_button_and_wait()
    
    @allure.title("Тест 5: Проверка счетчика ингредиента при открытии")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_counter_initial_state(self, driver):
        """Тест начального состояния счетчика ингредиента БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)

        main_page.open()
        
        # ЛИНЕЙНЫЙ СЦЕНАРИЙ: если элемента счетчика нет - тест ПАДАЕТ
        # Это показывает баг 
        counter = main_page.get_ingredient_counter()
        
        # Простая проверка: счетчик должен быть 0
        assert counter == 0, f"Начальный счетчик должен быть 0, а не {counter}"
    
    @allure.title("Тест 6: Добавление ингредиента через drag-and-drop")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_ingredient_by_drag_and_drop(self, driver):
        """Линейный тест добавления ингредиента БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)

        main_page.open()
        
        # Получаем начальный счетчик (если элемента нет - тест падает)
        initial_counter = main_page.get_ingredient_counter()
        
        # Добавляем ингредиент (если не получается - тест падает)
        main_page.drag_ingredient_to_constructor()
        
        # Проверяем что счетчик увеличился (если не увеличился - тест падает)
        main_page.verify_counter_increased(initial_counter)
    
    @allure.title("Тест 7: Проверка ленты заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_feed_basic_functionality(self, driver):
        """Базовый тест ленты заказов БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        
        # Перейти в ленту заказов
        main_page.click_order_feed()
        
        # Дождаться появления карточек заказов
        order_page.wait_for_order_cards_visible()
        
        # Раздел "В работе" должен быть виден
        order_page.wait_for_in_progress_section_visible()
    
    @allure.title("Тест 8: Работа с модальным окном заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_modal_functionality(self, driver):
        """Тест модального окна заказа БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_feed()
        order_page.wait_for_order_cards_visible()
        
        # Открываем модальное окно заказа
        order_page.click_first_order_card_and_wait_modal()
        
        # Закрываем модальное окно
        order_page.close_order_modal_and_wait()