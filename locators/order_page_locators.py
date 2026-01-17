
from selenium.webdriver.common.by import By

class OrderPageLocators:
    """Локаторы для страницы ленты заказов (Order Feed)"""

    
    # Для ожидания загрузки страницы
    ORDER_FEED_SECTION = (By.XPATH, "//section[contains(@class, 'OrderFeed') or contains(@class, 'orderFeed')]")

    #  заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # просто h1 с любым текстом
    ANY_H1 = (By.XPATH, "//h1")

    # Счетчик "Выполнено за все время" - ищем рядом с текстом
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(., 'Выполнено за все время')]/following-sibling::p")
    #TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время']/following-sibling::p[1]")
    
    # Счетчик "Выполнено за сегодня"
    #TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p[1]")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(., 'Выполнено за сегодня')]/following-sibling::p")

    
    # Список заказов "В работе"
    IN_WORK_ORDER_ITEMS = (By.XPATH, "//*[contains(text(), 'В работе')]/following-sibling::ul/li")

    # Список готовых заказов
    READY_ORDERS_LIST = (By.XPATH, "//*[contains(text(), 'Готовы')]/following-sibling::ul")

    # Номера заказов в ленте (карточки)
    ORDER_LIST_NUMBERS = (By.XPATH, "//p[contains(@class, 'digits-default')]")

    # В order_page_locators.py
    TOTAL_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'digits')])[1]")
    TODAY_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'digits')])[2]")



    #СТАРЫЕ 
    # Весь список заказов (для проверки появления номера)
    #ORDER_LIST_NUMBERS = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]//p[@class='text text_type_digits-default']")

    # Счетчик "Выполнено за все время"
    #TOTAL_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    # Счетчик "Выполнено за сегодня"
    #TODAY_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    # Список заказов "В работе" (In progress)
    #ORDERS_IN_PROGRESS_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/preceding-sibling::ul[contains(@class, 'OrderFeed_orderList')]")
    # Более точный путь для номеров в колонке "В работе" 
    #READY_ORDERS_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]")

    #PAGE_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    #IN_WORK_ORDER_ITEMS = (By.XPATH, "//ul[not(contains(@class, 'orderListReady'))]/li[contains(@class, 'text_type_digits-default')]")