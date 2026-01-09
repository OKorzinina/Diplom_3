import allure
from .base_page import BasePage
from locators.auth_page_locators import AuthPageLocators
from urls import Urls


class AuthPage(BasePage):
    
    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.driver.get(Urls.LOGIN_URL)
        self.wait_for_visible(AuthPageLocators.HEADER)
    
    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        self.send_keys(AuthPageLocators.EMAIL_INPUT, email)
    
    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password):
        self.send_keys(AuthPageLocators.PASSWORD_INPUT, password)
    
    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click(AuthPageLocators.LOGIN_BUTTON)
    
    @allure.step("Выполнить авторизацию с email: {email} и паролем: {password}")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
    
    @allure.step("Нажать 'Зарегистрироваться'")
    def click_register_link(self):
        self.click(AuthPageLocators.REGISTER_LINK)
    
    @allure.step("Нажать 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.click(AuthPageLocators.FORGOT_PASSWORD_BUTTON)
    
    @allure.step("Проверить отображение ошибки")
    def is_error_displayed(self):
        return self.is_element_present(AuthPageLocators.ERROR_MESSAGE)
    
    @allure.step("Получить текст ошибки")
    def get_error_text(self):
        if self.is_error_displayed():
            return self.get_text(AuthPageLocators.ERROR_MESSAGE)
        return ""
    
    