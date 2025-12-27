# Диплом
## Задание 3: Автотесты для UI (сервис https://stellarburgers.education-services.ru)

## Структура проекта
* locators/ - Локаторы элементов
* pages/ - Page Object классы
* tests/ - Наборы тестов
* generators.py - Генераторы тестовых данных
* urls.py - URL приложения
* allure-results

#### Установка

pip install -r requirements.txt

#### Тесты в Chrome
* pytest tests/ -v --browser=chrome

#### Тесты в Firefox
* pytest tests/ -v --browser=firefox

#### Allure отчет
* pytest tests/ -v --alluredir=allure-results

