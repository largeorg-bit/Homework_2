from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_init2():
    p = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert p.name == "Xiaomi Redmi Note 11"
    assert p.description == "1024GB, Синий"
    assert p.price == 31000.0
    assert p.quantity == 14
