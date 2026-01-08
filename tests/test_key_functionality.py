# Вариант 1
 # asserts добавлены в тесты, где можно было их добавить без изменения логики тестов,
 # а также, чтобы не нарушать замечания, которые были ранее. 
 # После кода для Варианта 1, есть код Варианта 2, там больше ассертов, 
 #но в некоторых тестах изменена логика, что частично не учитывает ранее полученные замечания

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
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"  # добавлен

        # 3. Вернуться в конструктор
        main_page.click_constructor()
        assert "stellarburgers" in driver.current_url, "Не вернулись в конструктор"  # добавлен
    
    @allure.title("Тест 2: Открытие и закрытие модального окна ингредиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_open_and_close(self, driver):
        """Линейный тест модального окна БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)

        # 1. Открыть главную страницу
        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"  # добавлен

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
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"  # добавлен
        
        main_page.click_ingredient_and_wait_modal()
        main_page.close_modal_with_escape_and_wait()
    
    @allure.title("Тест 4: Закрытие модального окна альтернативной кнопкой")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_close_with_alt_button(self, driver):
        """Тест закрытия модального окна альтернативной кнопкой БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"  # добавлен
        
        main_page.click_ingredient_and_wait_modal()
        # ЛИНЕЙНЫЙ СЦЕНАРИЙ: если кнопки нет - тест ПАДАЕТ
        main_page.close_modal_with_alt_button_and_wait()
    
    @allure.title("Тест 5: Проверка счетчика ингредиента при открытии")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_counter_initial_state(self, driver):
        """Тест начального состояния счетчика ингредиента БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"  # добавлен
        
        # ЛИНЕЙНЫЙ СЦЕНАРИЙ: если элемента счетчика нет - тест ПАДАЕТ
        counter = main_page.get_ingredient_counter()
        
        # Простая проверка: счетчик должен быть 0
        assert counter == 0, f"Начальный счетчик должен быть 0, а не {counter}"
        assert isinstance(counter, int), f"Счетчик должен быть целым числом, а не {type(counter)}"  # добавлен
    
    @allure.title("Тест 6: Добавление ингредиента через drag-and-drop")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_ingredient_by_drag_and_drop(self, driver):
        """Линейный тест добавления ингредиента БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"  # добавлен
        
        # Получаем начальный счетчик (если элемента нет - тест падает)
        initial_counter = main_page.get_ingredient_counter()
        
        # Добавляем ингредиент (если не получается - тест падает)
        main_page.drag_ingredient_to_constructor()
        
        # Проверяем что счетчик увеличился (если не увеличился - тест падает)
        main_page.verify_counter_increased(initial_counter)
        
        # Дополнительная проверка что счетчик стал больше 0
        new_counter = main_page.get_ingredient_counter()
        assert new_counter > 0, f"Счетчик должен быть больше 0 после добавления, а равен {new_counter}"  # добавлен
    
    @allure.title("Тест 7: Проверка ленты заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_feed_basic_functionality(self, driver):
        """Базовый тест ленты заказов БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"  # добавлен
        
        # Перейти в ленту заказов
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"  # добавлен
        
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
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"  # добавлен
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"  # добавлен
        
        order_page.wait_for_order_cards_visible()
        
        # Открываем модальное окно заказа
        order_page.click_first_order_card_and_wait_modal()
        
        # Закрываем модальное окно
        order_page.close_order_modal_and_wait()
        
        # Проверка что остались в ленте заказов после закрытия модалки
        assert "feed" in driver.current_url, "Не остались в ленте заказов после закрытия модалки"  # добавлен
     
#ВАРИАНТ 2 (в некторых тестах изменена логика)
#import allure
#import pytest
#from pages.main_page import MainPage
#from pages.order_page import OrderPage
#class TestKeyFunctionality:
    
    #@allure.title("Тест 1: Переход по клику на 'Конструктор' и 'Лента заказов'")
    #@allure.severity(allure.severity_level.CRITICAL)
    #def test_navigation_between_constructor_and_order_feed(self, driver):
        #"""Атомарный тест навигации БЕЗ ВЕТВЛЕНИЙ"""
        #main_page = MainPage(driver)

        # 1. Открыть главную страницу
        #main_page.open()

        # 2. Перейти в ленту заказов
        #main_page.click_order_feed()
        #assert "feed" in driver.current_url, "Не перешли в ленту заказов"

        # 3. Вернуться в конструктор
        #main_page.click_constructor()
        #assert "stellarburgers" in driver.current_url, "Не вернулись в конструктор"
    
    #@allure.title("Тест 2: Открытие и закрытие модального окна ингредиента")
    #@allure.severity(allure.severity_level.NORMAL)
    #def test_ingredient_modal_open_and_close(self, driver):
       # """Линейный тест модального окна БЕЗ ВЕТВЛЕНИЙ"""
        #main_page = MainPage(driver)

        # 1. Открыть главную страницу
        #main_page.open()
        #assert "stellarburgers" in driver.current_url, "Главная страница не открылась"

        # 2. Кликнуть на ингредиент и дождаться открытия
        #main_page.click_ingredient_and_wait_modal()
        #assert main_page.is_modal_open(), "Модальное окно ингредиента не открылось"  # ДОБАВЛЕН
        
        # 3. Закрыть модальное окно основной кнопкой и дождаться закрытия
        #main_page.close_modal_and_wait()
        #assert main_page.is_modal_closed(), "Модальное окно ингредиента не закрылось"  # ДОБАВЛЕН
    
    #@allure.title("Тест 3: Закрытие модального окна через ESCAPE")
    #@allure.severity(allure.severity_level.NORMAL)
    #def test_ingredient_modal_close_with_escape(self, driver):
        #"""Тест закрытия модального окна клавишей ESC БЕЗ ВЕТВЛЕНИЙ"""
        #main_page = MainPage(driver)

        #main_page.open()
        #assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        #main_page.click_ingredient_and_wait_modal()
        #assert main_page.is_modal_open(), "Модальное окно не открылось перед нажатием ESC"  # ДОБАВЛЕН
        
        #main_page.close_modal_with_escape_and_wait()
        #assert main_page.is_modal_closed(), "Модальное окно не закрылось после нажатия ESC"  # ДОБАВЛЕН
    
    #@allure.title("Тест 4: Закрытие модального окна альтернативной кнопкой")
    #@allure.severity(allure.severity_level.NORMAL)
    #def test_ingredient_modal_close_with_alt_button(self, driver):
       # """Тест закрытия модального окна альтернативной кнопкой БЕЗ ВЕТВЛЕНИЙ"""
        #main_page = MainPage(driver)

        #main_page.open()
        #assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        #main_page.click_ingredient_and_wait_modal()
        #assert main_page.is_modal_open(), "Модальное окно не открыто перед закрытием альтернативной кнопкой"  # ДОБАВЛЕН
        
        # ЛИНЕЙНЫЙ СЦЕНАРИЙ: если кнопки нет - тест ПАДАЕТ
        #main_page.close_modal_with_alt_button_and_wait()
        #assert main_page.is_modal_closed(), "Модальное окно не закрылось альтернативной кнопкой"  # ДОБАВЛЕН
    
    #@allure.title("Тест 5: Проверка счетчика ингредиента при открытии")
    #@allure.severity(allure.severity_level.NORMAL)
    #def test_ingredient_counter_initial_state(self, driver):
        #"""Тест начального состояния счетчика ингредиента БЕЗ ВЕТВЛЕНИЙ"""
        #main_page = MainPage(driver)

        #main_page.open()
        #assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        # ЛИНЕЙНЫЙ СЦЕНАРИЙ: если элемента счетчика нет - тест ПАДАЕТ
        #counter = main_page.get_ingredient_counter()
        
        # Простая проверка: счетчик должен быть 0
        #assert counter == 0, f"Начальный счетчик должен быть 0, а не {counter}"
        #assert isinstance(counter, int), f"Счетчик должен быть целым числом, а не {type(counter)}"
    
    #@allure.title("Тест 6: Добавление ингредиента через drag-and-drop")
    #@allure.severity(allure.severity_level.NORMAL)
    #def test_add_ingredient_by_drag_and_drop(self, driver):
        #"""Линейный тест добавления ингредиента БЕЗ ВЕТВЛЕНИЙ"""
        #main_page = MainPage(driver)

        #main_page.open()
        #assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        # Получаем начальный счетчик (если элемента нет - тест падает)
        #initial_counter = main_page.get_ingredient_counter()
        
        # Добавляем ингредиент (если не получается - тест падает)
        #main_page.drag_ingredient_to_constructor()
        
        # Проверяем что счетчик увеличился (если не увеличился - тест падает)
        #main_page.verify_counter_increased(initial_counter)
        
        # Дополнительная проверка что счетчик стал больше 0
        #new_counter = main_page.get_ingredient_counter()
        #assert new_counter > 0, f"Счетчик должен быть больше 0 после добавления, а равен {new_counter}"
    
    #@allure.title("Тест 7: Проверка ленты заказов")
    #@allure.severity(allure.severity_level.CRITICAL)
    #def test_order_feed_basic_functionality(self, driver):
        #"""Базовый тест ленты заказов БЕЗ ВЕТВЛЕНИЙ"""
        #main_page = MainPage(driver)
        #order_page = OrderPage(driver)

        #main_page.open()
        #assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        # Перейти в ленту заказов
        #main_page.click_order_feed()
        #assert "feed" in driver.current_url, "Не перешли в ленту заказов"
        
        # Дождаться появления карточек заказов
        #order_page.wait_for_order_cards_visible()
        
        # Раздел "В работе" должен быть виден
        #order_page.wait_for_in_progress_section_visible()
    
    #@allure.title("Тест 8: Работа с модальным окном заказа")
    #@allure.severity(allure.severity_level.CRITICAL)
    #def test_order_modal_functionality(self, driver):
       # """Тест модального окна заказа БЕЗ ВЕТВЛЕНИЙ"""
        #main_page = MainPage(driver)
        #order_page = OrderPage(driver)

        #main_page.open()
        #assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        #main_page.click_order_feed()
        #assert "feed" in driver.current_url, "Не перешли в ленту заказов"
        
        #order_page.wait_for_order_cards_visible()
        
        # Открываем модальное окно заказа
        #order_page.click_first_order_card_and_wait_modal()
        #assert order_page.is_order_modal_open(), "Модальное окно заказа не открылось"  # ДОБАВЛЕН
        
        # Закрываем модальное окно
        #order_page.close_order_modal_and_wait()
        #assert order_page.is_order_modal_closed(), "Модальное окно заказа не закрылось"  # ДОБАВЛЕН
        
        # Проверка что остались в ленте заказов после закрытия модалки
        #assert "feed" in driver.current_url, "Не остались в ленте заказов после закрытия модалки"
