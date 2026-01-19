
from selenium.webdriver.common.by import By

class OrderPageLocators:
        
    # Для ожидания загрузки страницы
    ORDER_FEED_SECTION = (By.XPATH, "//section[contains(@class, 'OrderFeed') or contains(@class, 'orderFeed')]")

    #  заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Счетчик "Выполнено за все время" - ищем рядом с текстом
    TOTAL_ORDERS_COUNTER_FEED = (By.XPATH, "//p[contains(., 'Выполнено за все время')]/following-sibling::p")  
        
    # Счетчик "Выполнено за сегодня"
    TODAY_ORDERS_COUNTER_FEED = (By.XPATH, "//p[contains(., 'Выполнено за сегодня')]/following-sibling::p") 
    
    # Список заказов "В работе"
    IN_WORK_ORDER_ITEMS = (By.XPATH, "//*[contains(text(), 'В работе')]/following-sibling::ul/li")

    # Список готовых заказов
    READY_ORDERS_LIST = (By.XPATH, "//*[contains(text(), 'Готовы')]/following-sibling::ul")

    # Номера заказов в ленте (карточки)
    ORDER_LIST_NUMBERS = (By.XPATH, "//p[contains(@class, 'digits-default')]")

    # В order_page_locators.py
    TOTAL_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'digits')])[1]")
    TODAY_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'digits')])[2]")

