import allure
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    locators_class = MainPageLocators

    @allure.step("Открыть главную страницу")
    def open(self):
        self.go_to_url(Urls.BASE_URL)
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=15)

    @allure.step("Нажать на 'Лента заказов'")
    def click_order_feed(self):
        # 1. Ждем закрытия модального окна 
        WebDriverWait(self.driver, 25).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY)
        )
        # 2. Ждем кликабельности элемента
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        )
        # 3. JavaScript клик 
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Нажать на 'Конструктор'")
    def click_constructor(self):
        element = self.find_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        element.click()

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click(MainPageLocators.FLUORESCENT_BUN)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        # Ожидание кнопки закрытия
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(MainPageLocators.CLOSE_MODAL_BUTTON)
        )
        # JavaScript клик
        self.driver.execute_script("arguments[0].click();", element)
        # Ожидание исчезновения оверлея
        WebDriverWait(self.driver, 25).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY)
        )

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
        self.driver.refresh()
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=15)

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

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_make_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Ожидание появления номера заказа")
    def wait_for_order_id_visible(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_ID_IN_MODAL),
            message="Модальное окно с номером заказа не появилось"
        )

    @allure.step("Получить номер заказа из модального окна")
    def get_order_id_from_modal(self):
        # Сначала дожидаемся видимости
        self.wait_for_order_id_visible()
        # Ждем, пока текст станет отличным от "9999" 
        WebDriverWait(self.driver, 15).until_not(
            EC.text_to_be_present_in_element(MainPageLocators.ORDER_ID_IN_MODAL, "9999")
        )
        return self.find_element(MainPageLocators.ORDER_ID_IN_MODAL).text.strip()

    @allure.step("Ожидание закрытия модального окна")
    def wait_for_modal_closed(self):
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY),
            message="Модальное окно не закрылось"
        )

