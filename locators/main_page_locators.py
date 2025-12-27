from selenium.webdriver.common.by import By


class MainPageLocators:
    # Верхнее меню
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
    # Ингредиенты
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']/parent::div")
    
    # Конкретные ингредиенты
    FLUORESCENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::div")
    SPICY_SAUCE = (By.XPATH, "//p[text()='Соус Spicy-X']/parent::div")
    BEEF_FILLING = (By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']/parent::div")
    
    # Счетчики
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter__')]")
    
    # Модальное окно ингредиента
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button")
    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h2[contains(@class, 'text_type_main-large')]")
    MODAL_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//div[contains(@class, 'Modal_info__')]")
    
    # Конструктор заказа
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_TOTAL = (By.XPATH, "//p[contains(@class, 'OrderModal_total__')]")
    
    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__') and .//p[text()='идентификатор заказа']]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'OrderModal_number__')]")
    ORDER_SUCCESS = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
