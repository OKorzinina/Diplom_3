from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Заголовок
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Счетчики
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за всё время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    # Секции заказов
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__')]//li")
    ORDERS_DONE = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList__')]//li")
    
    # Карточки заказов
    ORDER_CARDS = (By.XPATH, "//div[contains(@class, 'OrderHistory_card__') or contains(@class, 'OrderFeed_order__')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'OrderHistory_number__')]")
    ORDER_STATUS = (By.XPATH, ".//p[contains(@class, 'OrderHistory_status__')]")
    
    # Модальное окно заказа в ленте
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_title__')]")
    MODAL_ORDER_STATUS = (By.XPATH, "//p[contains(@class, 'Modal_status__')]")
    
    # Статистика
    IN_PROGRESS_SECTION = (By.XPATH, "//div[contains(@class, 'OrderFeed_inProgress__')]")
    DONE_SECTION = (By.XPATH, "//div[contains(@class, 'OrderFeed_done__')]")
