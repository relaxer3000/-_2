# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union


import doctest

class Product:
    def __init__(self, quantity: int, cost: Union[int, float]):
        """
               Создание и подготовка к работе объекта "Товар"

               :param quantity: количество товара
               :param cost: стоимость товара

               Примеры:
                   >>> product = Product (20, 100)  # инициализация экземпляра класса
               """
        if not isinstance(quantity, int):
            raise TypeError("Количество товара должно быть типа int")
        if quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным числом")
        self.quantity = quantity

        if not isinstance(cost, (int, float)):
            raise TypeError("Стоимость товара должна быть int или float")
        if cost <= 0:
            raise ValueError("Стоимость товара должна быть положительным число")
        self.cost = cost

    def is_available_product(self) -> bool:
        """
        Функция которая проверяет есть ли товар в наличии

        :return: Есть ли товар в наличии

        Примеры:
        >>> product = Product (20, 100)
        >>> product.is_available_product()
        """
        ...

    def change_product_cost(self, price: float) -> None:
        """
        Изменение стоимости товара.
        :param price: Новая стоимость товара

        Примеры:
        >>> product = Product (20, 100)
        >>> product.change_product_cost(150)
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Новая стоимость товара должна быть типа int или float")
        if price < 0:
            raise ValueError("Новая стоимость товара должна быть положительным числом")
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()
