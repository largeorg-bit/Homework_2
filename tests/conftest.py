import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def clear_counts():
    # чтобы счетчики не копились между тестами
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
