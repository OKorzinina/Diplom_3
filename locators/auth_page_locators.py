from selenium.webdriver.common.by import By

class AuthPageLocators:
    # Заголовок "Вход"
    LOGIN_TITLE = (By.XPATH, ".//h2[text()='Вход']")

    # Поля ввода 
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")

    # Кнопка Войти
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # Кнопки-ссылки
    REGISTER_BUTTON = (By.XPATH, ".//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")

