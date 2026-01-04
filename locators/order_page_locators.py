
from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Основные элементы ленты заказов
    ORDER_FEED_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    
    # Карточки заказов
    ORDER_CARDS = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')] | //div[contains(@class, 'OrderCard_container')]")
    
    # Раздел "В работе"
    IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(text(), 'В работе:')] | //div[contains(text(), 'В работе:')]")
    
    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    # Кнопка закрытия модального окна заказа
    ORDER_MODAL_CLOSE = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]/button | //div[contains(@class, 'Modal_modal')]/button")
