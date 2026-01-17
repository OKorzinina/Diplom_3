import allure
from pages.main_page import MainPage


class TestKeyFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigation_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_feed()
        main_page.click_constructor()
        button_text = main_page.get_constructor_button_text()
        assert "Конструктор" in button_text

    @allure.title("Переход по клику на раздел «Лента заказов»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigation_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_feed()
        button_text = main_page.get_order_feed_button_text()
        assert "Лента" in button_text

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        modal_visible = main_page.is_modal_visible()
        #assert modal_visible is True
        assert main_page.is_modal_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.close_modal()
        modal_closed = main_page.is_modal_not_displayed()
        assert modal_closed 

    @allure.title("Счетчик ингредиента увеличивается при добавлении в заказ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        # Получаем начальное значение (метод возвращает int)
        initial_counter = main_page.get_ingredient_counter()

        # Добавляем ингредиент
        main_page.drag_ingredient_to_constructor()

        # Получаем новое значение
        new_counter = main_page.get_ingredient_counter()

        # Точная проверка: счетчик увеличился ровно на 2 (так как булки добавляются по 2 шт сразу)
        assert new_counter == initial_counter + 2