from selenium.webdriver.common.by import By


class AuthPageLocators:
    # Поля ввода
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    
    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    
    # Текст/ошибки
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")
    HEADER = (By.XPATH, "//h2[text()='Вход']")
    
    # Ссылки
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
