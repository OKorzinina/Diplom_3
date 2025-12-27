
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"element_not_found_{locator}",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element {locator} not found")
    
    @allure.step("Найти элементы {locator}")
    def find_elements(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Elements {locator} not found")
    
    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()
    
    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text
    
    @allure.step("Ожидать видимость элемента {locator}")
    def wait_for_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element {locator} not visible")
    
    @allure.step("Ожидать исчезновение элемента {locator}")
    def wait_for_invisible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element {locator} still visible")
    
    @allure.step("Проверить наличие элемента {locator}")
    def is_element_present(self, locator, timeout=5):
        try:
            self.find_element(locator, timeout)
            return True
        except:
            return False
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Обновить страницу")
    def refresh(self):
        self.driver.refresh()
