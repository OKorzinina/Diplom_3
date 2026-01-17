import pytest
from selenium import webdriver
import requests
import random

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Браузер для тестов")

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")

    
    driver_map = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
    }

   
    driver_class = driver_map[browser_name]

    driver_instance = driver_class()
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(10)

    yield driver_instance

    driver_instance.quit()

@pytest.fixture(scope="function")
def creating_user():
    """Создает реального пользователя через API"""

    unique_id = random.randint(1000, 9999)
    email = f"autotest{unique_id}@example.com"
    password = f"TestPass{unique_id}"

    # Регистрация
    payload = {
        "email": email,
        "password": password,
        "name": f"AutoTest {unique_id}"
    }

    response = requests.post(
        "https://stellarburgers.education-services.ru/api/auth/register",
        json=payload
    )
   
    token_data = response.json()
    access_token = token_data["accessToken"]

    yield access_token, email, password

    # Дополнительно: удаление пользователя после теста  
    requests.delete(
        "https://stellarburgers.education-services.ru/api/auth/user",
        headers={'Authorization': access_token}
    )