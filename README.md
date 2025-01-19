# Виджет банковских операций
___
## Описание:
 Виджет отображает несколько последних успешных банковских операций клиента.
___
## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Chocoeater/Skypro-Project.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
___
## Функционал:
- Модуль masks 
    - Маскировка номера карты
        ```
        get_mask_card_number(1234123412341234) -> '1234 12** **** 1234'
        ```
    - Маскировка номера счета
        ```
        get_mask_account(12341234123412341234) -> '**1234'
        ```
- Модуль widget
    - Принимает тип карты или счет, номер счета и маскирует при помощи функционала masks
      ```
      mask_account_card('Visa Platinum 8990922113665229') -> 'Visa Platinum 8990 92** **** 5229'
       ```
    - Изменяет формат даты
        ```
      get_date('2024-03-11T02:26:18.671407') -> '11.03.2024'
        ```
   
- Модуль processing
    - Фильтрация списка словарей по ключу state (*по умолчанию 'EXECUTED'*)
        ```
      input_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
      
      filter_by_state(input_data) -> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
                                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
      ```
    - Сортировка списка словарей по ключу date (*по умолчанию убывание*)
        ```
      sort_by_date(input_data) -> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
                                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
                                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
                                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
        ```
- Модуль generators
    + Фильтрация по валюте
    ```filter_by_currency(list_of_transactions, code_of_currency)```
    + Описание операций
    ```transaction_descriptions(list_of_transactions)```
    + Генератор номеров карты в заданном диапазоне
    ```card_number_generator(start, end)```

- Модуль decorators
    + Декоратор log записывает имя функции и результат выполнения при успешной операции или имя функции, тип 
    возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
___

## Тесты:
Для запуская тестов при активированном виртуальном окружении: 
```
    pytest
```
Для подробного отчета по покрытию тестов в формате HTML: 
```
    pytest --cov=src --cov-report=html
```
