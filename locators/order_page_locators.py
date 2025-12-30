from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Заголовок
    ORDER_FEED_TITLE = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and text()='Лента заказов']")
    
    # Счетчики 
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'digits-large')]")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'digits-large')]")
    
    # Секции заказов
    IN_PROGRESS_SECTION = (By.XPATH, "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//p[text()='В работе:']/following-sibling::ul")
    DONE_SECTION = (By.XPATH, "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//p[text()='Готовы:']/following-sibling::ul")
    
    # Номера заказов "В работе" (для метода get_in_progress_order_numbers)
    IN_PROGRESS_ORDER_NUMBERS = (By.XPATH, "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//p[text()='В работе:']/following-sibling::ul//li")
    
    # Заказы в работе 
    ORDERS_IN_PROGRESS = (By.XPATH, "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//p[text()='В работе:']/following-sibling::ul//li")
    ORDERS_DONE = (By.XPATH, "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//p[text()='Готовы:']/following-sibling::ul//li")
    
    # Карточки заказов в ленте
    ORDER_CARDS = (By.XPATH, "//div[contains(@class, 'OrderHistory_link__')]")
    ORDER_NUMBER_IN_CARD = (By.XPATH, ".//p[contains(@class, 'digits-default')]")
    ORDER_STATUS_IN_CARD = (By.XPATH, ".//p[contains(@class, 'text_type_main-default')]")
    
    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h2[contains(@class, 'digits-large')]")
    MODAL_ORDER_STATUS = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//p[contains(@class, 'text_type_main-default')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_close__')]")
    
    # Альтернативные локаторы 
    ORDER_FEED_TITLE_ALT = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5']")
    TOTAL_ORDERS_ALT = (By.XPATH, "//p[@class='text text_type_main-medium' and text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_ALT = (By.XPATH, "//p[@class='text text_type_main-medium' and text()='Выполнено за сегодня:']/following-sibling::p")

