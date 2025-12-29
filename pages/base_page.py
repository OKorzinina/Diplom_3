  
import allure
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

# Настройка логирования
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=15):
        """Найти элемент с ожиданием видимости"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            # Прикрепляем скриншот к отчету Allure в случае ошибки
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="element_not_found_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Элемент {locator} не найден за {timeout} секунд")

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        try:
            element.click()
        except Exception:
            # Если обычный клик не сработал (например, элемент перекрыт), пробуем JS-клик
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text.strip()

    @allure.step("Проверить наличие элемента {locator}")
    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидать видимости элемента {locator}")
    def wait_for_visible(self, locator, timeout=10):
        return self.find_element(locator, timeout)

    @allure.step("Найти список элементов {locator}")
    def find_elements(self, locator, timeout=10):
        """Найти все элементы по локатору"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        """Поиск и нажатие на кнопку закрытия в типичных модальных окнах"""
        close_selectors = [
            (By.XPATH, "//button[contains(@class, 'close')]"),
            (By.XPATH, "//button[text()='✕']"),
            (By.XPATH, "//button[text()='×']"),
        ]

        for selector in close_selectors:
            try:
                close_button = self.driver.find_element(*selector)
                if close_button.is_displayed():
                    close_button.click()
                    return True
            except NoSuchElementException:
                continue
        return False