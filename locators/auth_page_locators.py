
from selenium.webdriver.common.by import By


class AuthPageLocators:
    # Поля ввода
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    
    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    
    # Заголовок
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    
    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class, 'logo')]")