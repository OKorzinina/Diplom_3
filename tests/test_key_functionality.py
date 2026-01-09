import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestKeyFunctionality:
    
    @allure.title("Тест 1: Переход по клику на 'Конструктор' и 'Лента заказов'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigation_between_constructor_and_order_feed(self, driver):
        """Атомарный тест навигации с проверкой URL"""
        main_page = MainPage(driver)

        # 1. Открыть главную страницу
        main_page.open()

        # 2. Перейти в ленту заказов
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"

        # 3. Вернуться в конструктор
        main_page.click_constructor()
        assert "stellarburgers" in driver.current_url, "Не вернулись в конструктор"
    
    @allure.title("Тест 2: Открытие и закрытие модального окна ингредиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_open_and_close(self, driver):
        """Линейный тест модального окна с проверками"""
        main_page = MainPage(driver)

        # 1. Открыть главную страницу
        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"

        # 2. Кликнуть на ингредиент и проверить заголовок модального окна
        main_page.click_ingredient_and_wait_modal()
        
        # Проверяем что модальное окно открылось через заголовок
        modal_title = main_page.get_modal_title()
        assert "ингредиент" in modal_title.lower(), f"Неверный заголовок модального окна: {modal_title}"

        # 3. Закрыть модальное окно основной кнопкой
        main_page.close_modal_and_wait()
        
        # Проверяем что конструктор доступен после закрытия
        main_page.click_constructor()
        assert "stellarburgers" in driver.current_url, "Конструктор не доступен после закрытия модалки"
    
    @allure.title("Тест 3: Закрытие модального окна через ESCAPE")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_close_with_escape(self, driver):
        """Тест закрытия модального окна клавишей ESC с проверками"""
        main_page = MainPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_ingredient_and_wait_modal()
        
        # Проверяем заголовок модального окна
        modal_title = main_page.get_modal_title()
        assert "ингредиент" in modal_title.lower(), f"Неверный заголовок модального окна: {modal_title}"
        
        main_page.close_modal_with_escape_and_wait()
        
        # Проверяем что конструктор доступен после ESC
        main_page.click_constructor()
        assert "stellarburgers" in driver.current_url, "Конструктор не доступен после ESC"
    
    @allure.title("Тест 4: Закрытие модального окна альтернативной кнопкой")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_close_with_alt_button(self, driver):
        """Тест закрытия модального окна альтернативной кнопкой с проверками"""
        main_page = MainPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_ingredient_and_wait_modal()
        
        # Проверяем заголовок модального окна
        modal_title = main_page.get_modal_title()
        assert "ингредиент" in modal_title.lower(), f"Неверный заголовок модального окна: {modal_title}"
        
        # Если альтернативной кнопки нет - тест упадет (как и должно быть)
        main_page.close_modal_with_alt_button_and_wait()
        
        # Проверяем что конструктор доступен
        main_page.click_constructor()
        assert "stellarburgers" in driver.current_url, "Конструктор не доступен после закрытия"
    
    @allure.title("Тест 5: Проверка счетчика ингредиента при открытии")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_counter_initial_state(self, driver):
        """Тест начального состояния счетчика ингредиента с проверками"""
        main_page = MainPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        # ЛИНЕЙНЫЙ СЦЕНАРИЙ: если элемента счетчика нет - тест ПАДАЕТ
        counter = main_page.get_ingredient_counter()
        
        # Проверки счетчика
        assert counter >= 0, f"Счетчик не может быть отрицательным: {counter}"
        assert isinstance(counter, int), f"Счетчик должен быть целым числом, а не {type(counter)}"
    
    @allure.title("Тест 6: Добавление ингредиента через drag-and-drop")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_ingredient_by_drag_and_drop(self, driver):
        """Линейный тест добавления ингредиента с проверками"""
        main_page = MainPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        # Получаем начальный счетчик
        initial_counter = main_page.get_ingredient_counter()
        
        # Добавляем ингредиент
        main_page.drag_ingredient_to_constructor()
        
        # Проверяем что счетчик увеличился
        new_counter = main_page.get_ingredient_counter()
        assert new_counter > initial_counter, f"Счетчик не увеличился: было {initial_counter}, стало {new_counter}"
    
    @allure.title("Тест 7: Проверка ленты заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_feed_basic_functionality(self, driver):
        """Базовый тест ленты заказов с проверками"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        # Перейти в ленту заказов
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"
        
        # Дождаться появления карточек заказов
        order_page.wait_for_order_cards_visible()
        
        # Раздел "В работе" должен быть виден
        order_page.wait_for_in_progress_section_visible()
    
    @allure.title("Тест 8: Работа с модальным окном заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_modal_functionality(self, driver):
        """Тест модального окна заказа с проверками"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"
        
        order_page.wait_for_order_cards_visible()
        
        # Открываем модальное окно заказа
        order_page.click_first_order_card_and_wait_modal()
        
        # Проверяем что URL изменился или есть параметр модального окна
        # Можно проверить что остались в ленте заказов
        assert "feed" in driver.current_url, "Не находимся в ленте заказов после открытия модалки"
        
        # Закрываем модальное окно клавишей ESCAPE
        main_page.send_keys_escape()
        
        # Проверяем что остались в ленте заказов после закрытия
        assert "feed" in driver.current_url, "Не остались в ленте заказов после закрытия модалки"