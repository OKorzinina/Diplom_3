
import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestKeyFunctionality:
    
    @allure.title("Тест 1: Переход по клику на 'Конструктор' и 'Лента заказов'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigation_between_constructor_and_order_feed(self, driver):
        """Атомарный тест навигации"""
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
        """Линейный тест модального окна"""
        main_page = MainPage(driver)

        # 1. Открыть главную страницу
        main_page.open()

        # 2. Кликнуть на ингредиент
        main_page.click_ingredient()

        # 3. Проверить что модальное окно открылось
        assert main_page.is_modal_open(), \
            "Модальное окно не открылось после клика на ингредиент"

        # 4. Закрыть модальное окно основной кнопкой
        main_page.close_modal()

        # 5. Проверить что модальное окно закрылось
        assert not main_page.is_modal_open(), \
            "Модальное окно не закрылось после клика на кнопку закрытия"
    
    @allure.title("Тест 3: Закрытие модального окна через ESCAPE")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_close_with_escape(self, driver):
        """Тест закрытия модального окна клавишей ESC"""
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_ingredient()
        main_page.close_modal_with_escape()
        
        assert not main_page.is_modal_open(), \
            "Модальное окно не закрылось после нажатия ESCAPE"
    
    @allure.title("Тест 4: Закрытие модального окна альтернативной кнопкой")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_close_with_alt_button(self, driver):
        """Тест закрытия модального окна альтернативной кнопкой"""
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_ingredient()
        main_page.close_modal_with_alt_button()
        
        assert not main_page.is_modal_open(), \
            "Модальное окно не закрылось после клика на альтернативную кнопку"
    
    @allure.title("Тест 5: Проверка счетчика ингредиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_counter(self, driver):
        """Тест счетчика ингредиента"""
        main_page = MainPage(driver)

        main_page.open()
        
        # Счетчик должен быть 0 при открытии страницы
        initial_counter = main_page.get_ingredient_counter()
        assert initial_counter == 0, f"Начальный счетчик должен быть 0, а не {initial_counter}"
    
    @allure.title("Тест 6: Добавление ингредиента через drag-and-drop")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_ingredient_by_drag_and_drop(self, driver):
        """Линейный тест добавления ингредиента"""
        main_page = MainPage(driver)

        main_page.open()
        initial_counter = main_page.get_ingredient_counter()

        # Добавить ингредиент
        main_page.drag_ingredient_to_constructor()
        
        # Проверить что счетчик изменился
        new_counter = main_page.get_ingredient_counter()
        assert new_counter > initial_counter, \
            f"Счетчик не увеличился после добавления ингредиента: было {initial_counter}, стало {new_counter}"