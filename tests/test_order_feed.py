import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderFeed:
    
    @allure.title("Тест: Отображение ленты заказов")
    def test_order_feed_display(self, driver):
        """Проверка отображения ленты заказов БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"
        
        # Метод wait_for_order_cards_visible сам упадет если карточек нет
        order_page.wait_for_order_cards_visible()
    
    @allure.title("Тест: Карточки заказов в ленте")
    def test_order_cards(self, driver):
        """Проверка отображения карточек заказов БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"

        # Метод wait_for_order_cards_visible сам упадет если карточек нет
        order_page.wait_for_order_cards_visible()
    
    @allure.title("Тест: Открытие и закрытие модального окна заказа")
    def test_order_modal(self, driver):
        """Проверка работы с модальным окном заказа БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"
        
        order_page.wait_for_order_cards_visible()
        
        # Кликаем на первую карточку
        order_page.click_first_order_card_and_wait_modal()
        # Метод click_first_order_card_and_wait_modal уже ждет открытия модалки
        
        # Закрываем модальное окно
        order_page.close_order_modal_and_wait()
        # Метод close_order_modal_and_wait уже ждет закрытия модалки
    
    @allure.title("Тест: Раздел 'В работе'")
    def test_in_progress_section(self, driver):
        """Проверка раздела 'В работе' БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"

        # Метод wait_for_in_progress_section_visible сам упадет если раздела нет
        order_page.wait_for_in_progress_section_visible()
    
    @allure.title("Тест: Обновление страницы")
    def test_page_refresh(self, driver):
        """Проверка обновления страницы БЕЗ ВЕТВЛЕНИЙ"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        
        main_page.click_order_feed()
        assert "feed" in driver.current_url, "Не перешли в ленту заказов"
        
        order_page.wait_for_order_cards_visible()
        
        # Обновляем страницу
        driver.refresh()
        
        # После обновления снова проверяем карточки
        order_page.wait_for_order_cards_visible()