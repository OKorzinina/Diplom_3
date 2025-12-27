import allure
from selenium.webdriver import ActionChains
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):
    
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(Urls.BASE_URL)
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Нажать 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_AREA)
    
    @allure.step("Нажать 'Лента заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Нажать 'Личный кабинет'")
    def click_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Кликнуть на ингредиент: {ingredient_name}")
    def click_ingredient(self, ingredient_name="Флюоресцентная булка R2-D3"):
        if ingredient_name == "Флюоресцентная булка R2-D3":
            self.click(MainPageLocators.FLUORESCENT_BUN)
        elif ingredient_name == "Соус Spicy-X":
            self.click(MainPageLocators.SPICY_SAUCE)
        elif ingredient_name == "Говяжий метеорит (отбивная)":
            self.click(MainPageLocators.BEEF_FILLING)
        self.wait_for_visible(MainPageLocators.INGREDIENT_MODAL)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL)
    
    @allure.step("Проверить открытие модального окна")
    def is_modal_open(self):
        return self.is_element_present(MainPageLocators.INGREDIENT_MODAL)
    
    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        return self.get_text(MainPageLocators.MODAL_TITLE)
    
    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_name="Флюоресцентная булка R2-D3"):
        source_element = None
        if ingredient_name == "Флюоресцентная булка R2-D3":
            source_element = self.find_element(MainPageLocators.FLUORESCENT_BUN)
        elif ingredient_name == "Соус Spicy-X":
            source_element = self.find_element(MainPageLocators.SPICY_SAUCE)
        
        target_element = self.find_element(MainPageLocators.CONSTRUCTOR_AREA)
        
        # Drag and drop
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
    
    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self, ingredient_name="Флюоресцентная булка R2-D3"):
        try:
            if ingredient_name == "Флюоресцентная булка R2-D3":
                ingredient = self.find_element(MainPageLocators.FLUORESCENT_BUN, timeout=3)
            elif ingredient_name == "Соус Spicy-X":
                ingredient = self.find_element(MainPageLocators.SPICY_SAUCE, timeout=3)
            
            counter = ingredient.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text)
        except:
            return 0
    
    @allure.step("Проверить активность кнопки 'Конструктор'")
    def is_constructor_active(self):
        element = self.find_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        return "constructor" in element.get_attribute("class")
