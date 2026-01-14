import allure
from pages.base_page import BasePage
from locators.auth_page_locators import AuthPageLocators
from urls import Urls

class AuthPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.driver.get(Urls.LOGIN_URL)
        self.wait_for_visible(AuthPageLocators.LOGIN_TITLE)

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        self.send_keys(AuthPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password):
        self.send_keys(AuthPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click(AuthPageLocators.LOGIN_BUTTON)

    @allure.step("Выполнить авторизацию")
    def login(self, email, password):
        self.wait_for_visible(AuthPageLocators.EMAIL_INPUT)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
   

    @allure.step("Нажать на ссылку 'Зарегистрироваться'")
    def click_register_link(self):
        self.click(AuthPageLocators.REGISTER_BUTTON)

    @allure.step("Нажать на ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.click(AuthPageLocators.FORGOT_PASSWORD_BUTTON)
