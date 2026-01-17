from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    #ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    FLUORESCENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter')]")
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    #MODAL_TITLE = (By.XPATH, "//h2[contains(@class, 'Modal_title')]")
    #MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'close')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
   
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    
    # Локаторы для drag and drop
    BUN_DROP_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    CONSTRUCTOR_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients')]")
    
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name' and @type='text']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

    ##
    # Кнопка "Оформить заказ" 
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    # Номер заказа в модальном окне (после оформления)
    ORDER_ID_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]") 
    ORDER_NUMBER_DISPLAY = (By.CSS_SELECTOR, ".entities_main__m_e_D") 

   
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]/parent::a")
