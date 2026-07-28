from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс продукта"""

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
