from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки навигации в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    
    # Ингредиенты
    FLUORESCENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    
    # Зона для перетаскивания 
    BUN_DROP_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    
    # Счетчик ингредиента
    INGREDIENT_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::div[contains(@class, 'ingredient')]//p[contains(@class, 'counter')]")
    
    # Модальное окно ингредиента
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_header')]//h2")
    # Кнопка закрытия - крестик в правом верхнем углу
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal')]/button")
    # Альтернативная кнопка - клик по оверлею (вне модального окна)
    MODAL_CLOSE_BUTTON_ALT = (By.XPATH, "//div[contains(@class, 'Modal_overlay')]")
