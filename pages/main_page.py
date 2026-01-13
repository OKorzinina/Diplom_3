import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):
    locators_class = MainPageLocators

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(Urls.BASE_URL)
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
    
    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        return self.get_text(MainPageLocators.MODAL_TITLE)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
    
    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)
    
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.FLUORESCENT_BUN,
            MainPageLocators.BUN_DROP_AREA
        )
    
    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=10)
    
    @allure.step("Кликнуть на личный кабинет")
    def click_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Ввести email")
    def enter_email(self, email):
        self.input_text(MainPageLocators.EMAIL_FIELD, email)
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.input_text(MainPageLocators.PASSWORD_FIELD, password)
    
    @allure.step("Нажать кнопку входа")
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)
    
    @allure.step("Получить текст кнопки конструктора")
    def get_constructor_button_text(self):
        return self.get_text(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Получить текст кнопки ленты заказов")
    def get_order_feed_button_text(self):
        return self.get_text(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        element = self.find_element(MainPageLocators.INGREDIENT_MODAL)
        return element.is_displayed()