import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
   
    def find_elements(self, locator, timeout=10):
        """Найти все элементы с ожиданием"""
        with allure.step(f"Найти все элементы по локатору: {locator}"):
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
   
    def wait_for_visible(self, locator, timeout=10):
        """Ожидать видимости элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
   
    def wait_for_invisible(self, locator, timeout=10):
        """Ожидать исчезновения элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
   
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Ожидать кликабельности элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
   
    def click(self, locator, timeout=10):
        """Кликнуть по элементу с ожиданием кликабельности"""
        with allure.step(f"Кликнуть на элемент: {locator}"):
            element = self.wait_for_element_to_be_clickable(locator, timeout)
            element.click()
   
    def get_text(self, locator, timeout=10):
        """Получить текст элемента"""
        element = self.wait_for_visible(locator, timeout)
        return element.text.strip()
   
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
        return WebDriverWait(self.driver, timeout).until(condition)
   
    def send_keys(self, locator, text, timeout=10):
        """Ввести текст в элемент"""
        with allure.step(f"Ввести текст в элемент {locator}: {text}"):
            element = self.wait_for_visible(locator, timeout)
            element.clear()
            element.send_keys(text)
   
    # Метод wait_for_presence добавлен для совместимости
    def wait_for_presence(self, locator, timeout=10):
        """Ожидать появления элемента в DOM"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )