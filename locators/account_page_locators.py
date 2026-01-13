from selenium.webdriver.common.by import By


class AccountPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@type='text' and contains(@name, 'email')]")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    REGISTER_BUTTON = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")