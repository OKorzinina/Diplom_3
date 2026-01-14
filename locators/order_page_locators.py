from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Весь список заказов (для проверки появления номера)
    ORDER_LIST_NUMBERS = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]//p[@class='text text_type_digits-default']")

    # Счетчик "Выполнено за все время"
    TOTAL_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    # Счетчик "Выполнено за сегодня"
    TODAY_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    # Список заказов "В работе" (In progress)
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/preceding-sibling::ul[contains(@class, 'OrderFeed_orderList')]")
    # Более точный путь для номеров в колонке "В работе" 
    READY_ORDERS_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]")

    PAGE_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    IN_WORK_ORDER_ITEMS = (By.XPATH, "//ul[not(contains(@class, 'orderListReady'))]/li[contains(@class, 'text_type_digits-default')]")
