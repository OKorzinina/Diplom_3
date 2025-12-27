
import allure
import time
import re
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):
    locators_class = MainPageLocators
    
    def open(self):
        self.driver.get(Urls.BASE_URL)
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BUTTON_SIMPLE)
    
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON_SIMPLE)
    
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON_SIMPLE)
    
    def click_ingredient(self):
        self.click(MainPageLocators.FLUORESCENT_BUN)
        time.sleep(1)
    
    def is_modal_open(self):
        return self.is_element_present(MainPageLocators.INGREDIENT_MODAL, timeout=2)
    
    def get_modal_title(self):
        return self.get_text(MainPageLocators.MODAL_TITLE)
    
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        time.sleep(0.5)
    
    def get_ingredient_counter(self):
        try:
            counter_text = self.get_text(MainPageLocators.INGREDIENT_COUNTER)
            numbers = re.findall(r'\d+', counter_text)
            return int(numbers[0]) if numbers else 0
        except:
            return 0
    
    def add_ingredient_to_constructor(self):
        
        ingredient = self.find_element(MainPageLocators.FLUORESCENT_BUN)
        time.sleep(1)