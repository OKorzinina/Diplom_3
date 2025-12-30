  
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = None
    
    def open_url(self, url):
        """Открыть указанный URL"""
        with allure.step(f"Открыть URL: {url}"):
            self.driver.get(url)
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
    
    def find_element(self, locator, timeout=10):
        """Найти элемент с ожиданием"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            self.take_screenshot("element_not_found")
            raise
    
    def wait_for_visible(self, locator, timeout=10):
        """Ожидать видимости элемента"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            self.take_screenshot("element_not_visible")
            raise
    
    def wait_for_invisible(self, locator, timeout=10):
        """Ожидать исчезновения элемента"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            self.take_screenshot("element_still_visible")
            raise
    
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Ожидать кликабельности элемента"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            self.take_screenshot("element_not_clickable")
            raise
    
    def click(self, locator, timeout=10):
        """Кликнуть по элементу с ожиданием кликабельности"""
        with allure.step(f"Кликнуть на элемент: {locator}"):
            element = self.wait_for_element_to_be_clickable(locator, timeout)
            element.click()
    
    def get_text(self, locator, timeout=10):
        """Получить текст элемента"""
        element = self.wait_for_visible(locator, timeout)
        return element.text.strip()
    
    def is_element_present(self, locator, timeout=5):
        """Проверить наличие элемента"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def is_element_visible(self, locator, timeout=5):
        """Проверить видимость элемента"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def wait_for_page_load(self, timeout=10):
        """Ожидание полной загрузки страницы"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
    
    def take_screenshot(self, name="screenshot"):
        """Сделать скриншот и прикрепить к Allure отчету"""
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
        return screenshot
    
    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивание элемента из источника в цель"""
        with allure.step(f"Перетащить элемент {source_locator} на элемент {target_locator}"):
            source = self.wait_for_visible(source_locator)
            target = self.wait_for_visible(target_locator)
            ActionChains(self.driver).drag_and_drop(source, target).perform()
    
    def send_keys_escape(self):
        """Отправить клавишу ESCAPE"""
        with allure.step("Отправить клавишу ESCAPE"):
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
    
    def click_by_offset(self, x_offset=10, y_offset=10):
        """Кликнуть по координатам смещения"""
        with allure.step(f"Кликнуть по смещению ({x_offset}, {y_offset})"):
            ActionChains(self.driver).move_by_offset(x_offset, y_offset).click().perform()
    
    def wait_for_condition(self, condition, timeout=10, message=""):
        """Ожидание кастомного условия"""
        try:
            return WebDriverWait(self.driver, timeout).until(condition)
        except TimeoutException:
            self.take_screenshot("condition_timeout")
            if message:
                raise TimeoutException(message)
            raise