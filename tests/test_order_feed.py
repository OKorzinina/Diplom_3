
import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderFeed:
    
    @allure.title("Тест: Отображение ленты заказов и счетчиков")
    def test_order_feed_display(self, driver):
        """Проверка базовой функциональности ленты заказов"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Линейный сценарий
        main_page.open()
        main_page.click_order_feed()
        
        # Проверить что перешли на ленту заказов
        current_url = main_page.get_current_url()
        assert "feed" in current_url, f"Не перешли на ленту заказов. URL: {current_url}"
    
    @allure.title("Тест: Карточки заказов в ленте")
    def test_order_cards(self, driver):
        """Проверка отображения карточек заказов"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_feed()
        
        # Линейный сценарий: проверяем что карточки есть
        
        assert order_page.is_order_cards_visible(), \
            "Карточки заказов не отображаются в ленте"
    
    @allure.title("Тест: Открытие и закрытие модального окна заказа")
    def test_order_modal(self, driver):
        """Проверка работы с модальным окном заказа"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_feed()
        
        # Линейный сценарий: проверяем карточки
        assert order_page.is_order_cards_visible(), \
            "Карточки заказов не отображаются в ленте"
        
        # Линейный сценарий: кликаем на первую карточку
        order_page.click_first_order_card()
        
        # Линейный сценарий: проверяем открытие модального окна
        assert order_page.is_order_modal_open(), \
            "Модальное окно заказа не открылось"
        
        # Линейный сценарий: закрываем модальное окно
        order_page.close_order_modal()
        
        # Линейный сценарий: проверяем закрытие
        assert not order_page.is_order_modal_open(), \
            "Модальное окно заказа не закрылось"
    
    @allure.title("Тест: Раздел 'В работе'")
    def test_in_progress_section(self, driver):
        """Проверка раздела 'В работе'"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_feed()
        
        # Линейный сценарий: проверяем раздел "В работе"
        # Если раздела нет - тест падает  
        assert order_page.is_in_progress_section_visible(), \
            "Раздел 'В работе' не отображается"
    
    @allure.title("Тест: Обновление страницы ленты заказов")
    def test_page_refresh(self, driver):
        """Проверка обновления страницы"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_feed()
        
        # Запомнить URL до обновления
        initial_url = main_page.get_current_url()
        assert "feed" in initial_url, f"Не на ленте заказов до обновления. URL: {initial_url}"
        
        # Обновить страницу
        driver.refresh()
        
        # Дать время на загрузку
        order_page.wait_for_page_load(timeout=10)
        
        # Проверить что остались на ленте заказов
        current_url = main_page.get_current_url()
        assert "feed" in current_url, f"После обновления не на ленте заказов. URL: {current_url}"