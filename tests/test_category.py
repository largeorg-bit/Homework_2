from src.category import Category
from src.product import Product


def test_category_init(product, product2):
    category = Category("Смартфоны", "Описание смартфонов", [product, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert len(category.products) == 2
    assert category.products[0] == product
    assert category.products[1] == product2


def test_category_count(product, product2):
    assert Category.category_count == 0

    Category("Смартфоны", "описание", [product])
    assert Category.category_count == 1

    Category("Телевизоры", "описание", [product2])
    assert Category.category_count == 2


def test_product_count(product, product2):
    assert Category.product_count == 0

    Category("Смартфоны", "описание", [product, product2])
    assert Category.product_count == 2

    p3 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    Category("Телевизоры", "описание", [p3])
    assert Category.product_count == 3
