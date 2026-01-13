import pytest
from selenium import webdriver
import requests
import random
import allure


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Браузер для тестов")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    
    # Создаем драйвер (без ветвлений)
    driver_map = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
    }
    
    # Выбираем класс драйвера
    driver_class = driver_map[browser_name] if browser_name in driver_map else driver_map["chrome"]
    
    # Создаем и настраиваем драйвер
    driver_instance = driver_class()
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(10)
    
    yield driver_instance
    
    driver_instance.quit()


@pytest.fixture(scope="function")
def creating_user():
    """Создает реального пользователя с валидным токеном"""
    
    # Генерируем уникальные данные
    unique_id = random.randint(1000, 9999)
    email = f"autotest{unique_id}@example.com"
    password = f"TestPass{unique_id}"
    
    # Регистрируем пользователя
    response = requests.post(
        "https://stellarburgers.education-services.ru/api/auth/register",
        json={
            "email": email,
            "password": password,
            "name": f"AutoTest {unique_id}"
        }
    )
    
    # Получаем токен
    token_data = response.json()
    access_token = token_data["accessToken"]
    
    # Возвращаем токен без лишнего "Bearer" (API добавляет его сам)
    return access_token, email, password
