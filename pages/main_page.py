import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls

class MainPage(BasePage):
    locators_class = MainPageLocators

    @allure.step("Открыть главную страницу")
    def open(self):
        self.go_to_url(Urls.BASE_URL)
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=15)

    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click(MainPageLocators.FLUORESCENT_BUN)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        return int(self.get_text(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.FLUORESCENT_BUN,
            MainPageLocators.BUN_DROP_AREA
        )

    @allure.step("Обновить страницу")
    def refresh_page(self):
        super().refresh_page()
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=10)

    @allure.step("Получить текст кнопки конструктора")
    def get_constructor_button_text(self):
        return self.get_text(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Получить текст кнопки ленты заказов")
    def get_order_feed_button_text(self):
        return self.get_text(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.is_element_present(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Проверить, что модальное окно отсутствует")
    def is_modal_not_displayed(self):
        return self.wait_for_invisibility(MainPageLocators.INGREDIENT_MODAL)