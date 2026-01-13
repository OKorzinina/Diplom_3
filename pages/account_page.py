import allure
from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    locators_class = AccountPageLocators
    
    @allure.step("Ввести email")
    def enter_email(self, email):
        self.input_text(AccountPageLocators.EMAIL_FIELD, email)
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.input_text(AccountPageLocators.PASSWORD_FIELD, password)
    
    @allure.step("Нажать кнопку входа")
    def click_login_button(self):
        self.click(AccountPageLocators.LOGIN_BUTTON)