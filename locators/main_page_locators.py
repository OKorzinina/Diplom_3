
from selenium.webdriver.common.by import By


class MainPageLocators:
    # Навигация (используйте классы из вывода)
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Конструктор']]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Лента Заказов']]")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Войти в аккаунт')]")
    
    # Ингредиенты
    FLUORESCENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    
    # Локатор для счетчика - несколько вариантов
    INGREDIENT_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/../following-sibling::div[contains(@class, 'counter')]//p")
    INGREDIENT_COUNTER_ALT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/../../div[contains(@class, 'counter')]")
    
    # Модальное окно ингредиента
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h2[contains(@class, 'Modal_modal__title__2L34m')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_close__')]")
    
    # Конструктор
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]")
    BUN_DROP_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")
    
    # Альтернативные локаторы для области конструктора 
    CONSTRUCTOR_AREA_ALT = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    BUN_DROP_AREA_ALT = (By.XPATH, "//div[contains(@class, 'constructor-element')]")
    
    # Секция ингредиентов
    INGREDIENT_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]")
    
    # Простые варианты для навигации
    CONSTRUCTOR_BUTTON_SIMPLE = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON_SIMPLE = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    
    # Дополнительные локаторы для тестов
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
    
    # Альтернативные локаторы для модального окна
    MODAL_CLOSE_BUTTON_ALT = (By.XPATH, "//button[contains(@class, 'close')]")
    MODAL_TITLE_ALT = (By.XPATH, "//div[contains(@class, 'Modal')]//h2")
    
    # Локаторы для перетаскивания (текстовые подсказки)
    DROP_AREA_TEXT = (By.XPATH, "//div[contains(text(), 'Перетащите булку сюда') or contains(text(), 'булку')]")
    
    # Ингредиент-родитель для более точного поиска
    INGREDIENT_PARENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/..")