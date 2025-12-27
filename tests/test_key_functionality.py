import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.auth_page import AuthPage


@allure.feature("Ключевая функциональность")
@allure.story("Основные сценарии использования")
class TestKeyFunctionality:
    
    @allure.title("Тест 1: Переход по клику на 'Конструктор'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_constructor_navigation(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step("2. Перейти в ленту заказов"):
            main_page.click_order_feed()
            assert order_page.is_element_present(OrderPage.ORDER_FEED_TITLE), "Не перешли в ленту заказов"
        
        with allure.step("3. Вернуться в конструктор"):
            main_page.click_constructor()
            assert main_page.is_element_present(MainPage.CONSTRUCTOR_AREA), "Не вернулись в конструктор"
    
    @allure.title("Тест 2: Переход по клику на 'Лента заказов'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step("2. Перейти в ленту заказов"):
            main_page.click_order_feed()
        
        with allure.step("3. Проверить, что лента заказов открыта"):
            assert order_page.is_element_present(OrderPage.ORDER_FEED_TITLE), "Лента заказов не открылась"
            assert "feed" in driver.current_url, "URL не соответствует ленте заказов"
    
    @allure.title("Тест 3: Открытие модального окна с деталями ингредиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step("2. Кликнуть на ингредиент"):
            main_page.click_ingredient()
        
        with allure.step("3. Проверить открытие модального окна"):
            assert main_page.is_modal_open(), "Модальное окно не открылось"
            title = main_page.get_modal_title()
            assert "Флюоресцентная булка R2-D3" in title, f"Неправильный заголовок: {title}"
    
    @allure.title("Тест 4: Закрытие модального окна ингредиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step("2. Открыть модальное окно ингредиента"):
            main_page.click_ingredient()
            assert main_page.is_modal_open(), "Модальное окно не открылось"
        
        with allure.step("3. Закрыть модальное окно"):
            main_page.close_modal()
        
        with allure.step("4. Проверить, что окно закрыто"):
            assert not main_page.is_modal_open(), "Модальное окно не закрылось"
    
    @allure.title("Тест 5: Увеличение счетчика ингредиента при добавлении")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step("2. Получить начальное значение счетчика"):
            initial_counter = main_page.get_ingredient_counter()
        
        with allure.step("3. Добавить ингредиент в конструктор"):
            main_page.add_ingredient_to_constructor()
        
        with allure.step("4. Проверить увеличение счетчика"):
            new_counter = main_page.get_ingredient_counter()
            assert new_counter == initial_counter + 1, f"Счетчик не увеличился: {initial_counter} -> {new_counter}"
    
    @allure.title("Тест 6: Навигация через логотип")
    @allure.severity(allure.severity_level.MINOR)
    def test_logo_navigation(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)
        
        with allure.step("1. Открыть страницу авторизации"):
            auth_page.open()
        
        with allure.step("2. Кликнуть на логотип (через конструктор)"):
            main_page.click_constructor()
        
        with allure.step("3. Проверить возврат на главную"):
            assert main_page.is_element_present(MainPage.CONSTRUCTOR_AREA), "Не вернулись на главную страницу"
