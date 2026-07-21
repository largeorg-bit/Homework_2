# Домашнее задание 14.1 — интернет-магазин

## Что сделано

Созданы классы Product и Category для интернет-магазина.

У Product: name, description, price, quantity.
У Category: name, description, products.
Также у Category есть атрибуты класса category_count и product_count — они считаются автоматически при создании категорий.

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
