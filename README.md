# Домашнее задание — интернет-магазин

## Что сделано

Созданы классы Product и Category для интернет-магазина.

У Product: name, description, price (приватный атрибут с геттером и сеттером), quantity.
Класс-метод new_product создает продукт из словаря.
Сеттер цены не принимает нулевые и отрицательные значения.

У Category: name, description, приватный список products.
Метод add_product добавляет товар в категорию.
Геттер products возвращает строку со списком товаров.
Также есть атрибуты класса category_count и product_count.

Добавлены магические методы:
- `__str__` у Product и Category
- `__add__` у Product (сумма price * quantity)

Наследование:
- классы Smartphone и LawnGrass — наследники Product
- складывать можно только товары одного класса (иначе TypeError)
- в категорию можно добавить только Product и его наследников

Абстракция и миксины:
- BaseProduct — абстрактный базовый класс для продуктов
- CreationMixin — при создании объекта печатает класс и параметры
- Product наследуется от CreationMixin и BaseProduct

## Как запустить

```bash
poetry install
poetry run python main.py
```

## Тесты

```bash
poetry run pytest --cov=src --cov-report=html
```

Отчет о покрытии лежит в папке htmlcov.

## Проверка кода

```bash
poetry run flake8
```
