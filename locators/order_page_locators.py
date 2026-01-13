from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Заголовок страницы
    PAGE_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Счетчики 
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(@class, 'digits')][contains(text(), '2')]")  
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(@class, 'digits')][contains(text(), '3')]")  
    
    # Раздел "В работе" 
    IN_PROGRESS_SECTION = (By.XPATH, "//*[contains(text(), 'В работе:')]")
    
    # Альтернативные локаторы для счетчиков
    
    ALL_DIGITS = (By.XPATH, "//p[contains(@class, 'digits')]")
    
    # Для теста "В работе" будем использовать родительский элемент
    IN_PROGRESS_CONTAINER = (By.XPATH, "//*[contains(text(), 'В работе:')]/..")

    # Доп локаторы:
    IN_WORK_LIST = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul[1]")
    IN_WORK_ORDER_ITEMS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul[1]/li")
