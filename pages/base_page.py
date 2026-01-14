from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15) 

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def send_keys(self, locator, text):
        self.input_text(locator, text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator):
        return self.find_element(locator).is_displayed()

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def refresh_page(self):
        self.driver.refresh()