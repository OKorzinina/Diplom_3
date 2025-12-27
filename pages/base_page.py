

import allure
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=15):
        """Найти элемент с возможностью альтернативного поиска"""
        try:
            print(f"Поиск элемента: {locator}")
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            
            print(f"Элемент не найден: {locator}, пробую альтернативы...")
            
            # Сохраняем скриншот 
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            self.driver.save_screenshot(f"debug_{timestamp}.png")
            
            
            if hasattr(self, 'locators_class'):
                locator_name = self._get_locator_name(locator)
                alt_locator_name = f"{locator_name}_ALT"
                
                if hasattr(self.locators_class, alt_locator_name):
                    alt_locator = getattr(self.locators_class, alt_locator_name)
                    print(f"альтернативный локатор: {alt_locator}")
                    try:
                        return WebDriverWait(self.driver, 5).until(
                            EC.visibility_of_element_located(alt_locator)
                        )
                    except TimeoutException:
                        print(f"Альтернативный локатор тоже не сработал")
            
            # Пробуем гибкий поиск по тексту
            if locator[0] == By.XPATH and "text()=" in locator[1]:
                # Извлекаем текст из локатора
                text = self._extract_text_from_xpath(locator[1])
                if text:
                    print(f"Пробую гибкий поиск по тексту: '{text}'")
                    flexible_locators = [
                        (By.XPATH, f"//*[contains(text(), '{text}')]"),
                        (By.XPATH, f"//*[text()='{text}']"),
                    ]
                    
                    for flex_loc in flexible_locators:
                        try:
                            elements = self.driver.find_elements(*flex_loc)
                            if elements:
                                print(f"Найдено {len(elements)} элементов по: {flex_loc}")
                                return elements[0]
                        except:
                            continue
            
         
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"element_not_found",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element {locator} not found after {timeout} seconds")
    
    def _get_locator_name(self, locator):
        """Получить имя локатора из объекта"""
        
        
        return "unknown"
    
    def _extract_text_from_xpath(self, xpath):
        """Извлечь текст из XPATH локатора"""
        import re
        
        match = re.search(r"text\(\)\s*=\s*['\"]([^'\"]+)['\"]", xpath)
        if match:
            return match.group(1)
        return None
    
    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        try:
            element.click()
        except:
            
            self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text.strip()
    
    @allure.step("Проверить наличие элемента {locator}")
    def is_element_present(self, locator, timeout=5):
        try:
            self.find_element(locator, timeout)
            return True
        except (TimeoutException, AssertionError):
            return False
    
    @allure.step("Ожидать видимости элемента {locator}")
    def wait_for_visible(self, locator, timeout=10):
        return self.find_element(locator, timeout)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        close_selectors = [
            (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_close__')]"),
            (By.XPATH, "//button[contains(@class, 'close')]"),
            (By.XPATH, "//button[text()='✕']"),
            (By.XPATH, "//button[text()='×']"),
        ]
        
        for selector in close_selectors:
            try:
                close_button = self.driver.find_element(*selector)
                close_button.click()
                time.sleep(0.5)
                return True
            except:
                continue
        return False
    
    @allure.step("Найти элементы {locator}")
    def find_elements(self, locator, timeout=10):
        """Найти все элементы по локатору"""
        try:
            print(f"Поиск элементов: {locator}")
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            print(f"Элементы не найдены: {locator}")
            return []
