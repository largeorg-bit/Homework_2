class CreationMixin:
    """Миксин: печатает информацию о созданном объекте"""

    def __init__(self):
        print(repr(self))
        super().__init__()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.name}', '{self.description}', "
            f"{self.price}, {self.quantity})"
        )
