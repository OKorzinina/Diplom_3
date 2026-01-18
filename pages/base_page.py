import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    @allure.step("Инициализация драйвера и ожиданий")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Переход по URL: {url}")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Ожидание, что URL содержит: {text}")
    def wait_for_url_contains(self, text, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    @allure.step("Поиск элемента по локатору: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Поиск списка элементов по локатору: {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание присутствия элемента в DOM: {locator}")
    def wait_for_presence(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_for_invisibility(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Ожидание изменения состояния (custom condition)")
    def wait_until_condition(self, condition, timeout=30):
        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Ожидание изменения текста в элементе: {locator}")
    def wait_until_text_not_present(self, locator, text, timeout=15):
        return WebDriverWait(self.driver, timeout).until_not(
            EC.text_to_be_present_in_element(locator, text)
        )

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("JS Клик по элементу: {locator}")
    def click_js(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Отправка клавиш/текста в элемент: {locator}")
    def send_keys(self, locator, text):
        self.input_text(locator, text)

    @allure.step("Получение текста из элемента: {locator}")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step("Проверка наличия элемента на странице: {locator}")
    def is_element_present(self, locator):
        return self.find_element(locator).is_displayed()

    @allure.step("Перетаскивание элемента {source_locator} к {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step("Обновление страницы")
    def refresh_page(self):
        self.driver.refresh()