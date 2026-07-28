class Category:
    """Класс категории"""

    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        # считаем категории и товары
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product}\n"
        return result

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."
