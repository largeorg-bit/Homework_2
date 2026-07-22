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


def test_new_product():
    data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_setter_positive(product):
    product.price = 800
    assert product.price == 800


def test_price_setter_negative(product, capsys):
    product.price = -100
    assert product.price == 180000.0
    message = capsys.readouterr().out
    assert "Цена не должна быть нулевая или отрицательная" in message


def test_price_setter_zero(product, capsys):
    product.price = 0
    assert product.price == 180000.0
    message = capsys.readouterr().out
    assert "Цена не должна быть нулевая или отрицательная" in message


def test_product_str(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product, product2):
    # 180000 * 5 + 210000 * 8
    assert product + product2 == 2580000.0
