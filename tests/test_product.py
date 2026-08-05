from src.base_product import BaseProduct
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


def test_smartphone_init():
    phone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    assert phone.name == "Samsung Galaxy S23 Ultra"
    assert phone.efficiency == 95.5
    assert phone.model == "S23 Ultra"
    assert phone.memory == 256
    assert phone.color == "Серый"
    assert isinstance(phone, Product)


def test_lawn_grass_init():
    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"
    assert isinstance(grass, Product)


def test_add_same_class():
    phone1 = Smartphone("Phone1", "desc", 100.0, 2, 90.0, "m1", 64, "black")
    phone2 = Smartphone("Phone2", "desc", 200.0, 3, 91.0, "m2", 128, "white")
    assert phone1 + phone2 == 100.0 * 2 + 200.0 * 3


def test_add_different_class():
    phone = Smartphone("Phone1", "desc", 100.0, 2, 90.0, "m1", 64, "black")
    grass = LawnGrass("Grass", "desc", 50.0, 10, "Россия", "7 дней", "green")
    try:
        phone + grass
        assert False
    except TypeError:
        assert True


def test_product_inherits_base_product():
    product = Product("Test", "desc", 100.0, 1)
    assert isinstance(product, BaseProduct)
    assert issubclass(Product, BaseProduct)
    assert Smartphone.__bases__ == (Product,)
    assert LawnGrass.__bases__ == (Product,)


def test_cannot_create_base_product():
    try:
        BaseProduct()
        assert False
    except TypeError:
        assert True


def test_creation_mixin_print(capsys):
    Product("Продукт1", "Описание продукта", 1200, 10)
    message = capsys.readouterr().out
    assert "Product('Продукт1', 'Описание продукта', 1200, 10)" in message


def test_product_zero_quantity():
    try:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
        assert False
    except ValueError as e:
        assert str(e) == "Товар с нулевым количеством не может быть добавлен"
