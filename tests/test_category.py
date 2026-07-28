from src.category import Category
from src.product import Product


def test_category_init(product, product2):
    category = Category("Смартфоны", "Описание смартфонов", [product, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert "Samsung Galaxy S23 Ultra" in category.products
    assert "Iphone 15" in category.products


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


def test_add_product(product, product2):
    category = Category("Смартфоны", "описание", [product])
    assert Category.product_count == 1

    category.add_product(product2)
    assert Category.product_count == 2
    assert "Iphone 15" in category.products
    assert category.add_product(Product("Test", "desc", 100.0, 1)) is None


def test_products_getter(product):
    category = Category("Смартфоны", "описание", [product])
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    assert category.products == expected


def test_category_str(product, product2):
    category = Category("Смартфоны", "описание", [product, product2])
    # 5 + 8 = 13
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."
