import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderFeed:
    
    @allure.title("Тест: Отображение ленты заказов")
    def test_order_feed_display(self, driver):
        """Проверка отображения ленты заказов с проверками"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"
        
        # Метод сам генерирует исключение при таймауте
        order_page.wait_for_order_cards_visible()
    
    @allure.title("Тест: Карточки заказов в ленте")
    def test_order_cards(self, driver):
        """Проверка отображения карточек заказов с проверками"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"

        # Метод сам генерирует исключение при таймауте
        order_page.wait_for_order_cards_visible()
    
    @allure.title("Тест: Открытие и закрытие модального окна заказа")
    def test_order_modal(self, driver):
        """Проверка работы с модальным окном заказа с проверками"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"
        
        # Метод сам генерирует исключение при таймауте
        order_page.wait_for_order_cards_visible()
        
        # Кликаем на первую карточку
        # Метод сам генерирует исключение при таймауте
        order_page.click_first_order_card_and_wait_modal()
        
        # Проверяем что остались в ленте заказов
        assert "feed" in driver.current_url, "Не находимся в ленте заказов после открытия модалки"
        
        # Закрываем модальное окно клавишей ESCAPE
        main_page.send_keys_escape()
        
        # Проверяем что остались в ленте заказов после закрытия
        assert "feed" in driver.current_url, "Не остались в ленте заказов после закрытия модалки"
    
    @allure.title("Тест: Раздел 'В работе'")
    def test_in_progress_section(self, driver):
        """Проверка раздела 'В работе' с проверками"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"

        # Метод сам генерирует исключение при таймауте
        order_page.wait_for_in_progress_section_visible()
    
    @allure.title("Тест: Обновление страницы")
    def test_page_refresh(self, driver):
        """Проверка обновления страницы с проверками"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"
        
        # Метод сам генерирует исключение при таймауте
        order_page.wait_for_order_cards_visible()
        
        # Проверяем что находимся в ленте заказов до обновления
        assert "feed" in driver.current_url, "Не находимся в ленте заказов до обновления"
        
        # Обновляем страницу
        driver.refresh()
        
        # Проверяем что остались в ленте заказов после обновления
        assert "feed" in driver.current_url, "Не остались в ленте заказов после обновления"
        
        # После обновления снова проверяем карточки
        # Метод сам генерирует исключение при таймауте
        order_page.wait_for_order_cards_visible()