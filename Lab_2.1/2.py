# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union


import doctest


class Tree:
    def __init__(self, age: Union[int, float], height: Union[int, float]):
        """
               Создание и подготовка к работе объекта "Дерево"

               :param age: возраст дерева (лет)
               :param height: высота дерева (м)

               Примеры:
                   >>> tree = Tree (10, 25)  # инициализация экземпляра класса
               """
        if not isinstance(age, (int, float)):
            raise TypeError("Возраст дерева должен быть типа int или float")
        if age <= 0:
            raise ValueError("Возраст дерева должен быть положительным число")
        self.age = age

        if not isinstance(height, (int, float)):
            raise TypeError("Высота деревва должна быть int или float")
        if height <= 0:
            raise ValueError("Высота деревва должна быть положительным число")
        self.height = height

    def increase_height(self, h: Union[int, float]) -> None:
        """
        Увеличение высоты дерева.
        :param h: Значение, на которое увеличилась высота дерева (м)

        Примеры:
        >>> tree = Tree (10, 25)
        >>> tree.increase_height(2)
        """
        if not isinstance(h, (int, float)):
            raise TypeError("Значение 'h' должно быть типа int или float")
        if h < 0:
            raise ValueError("Значение 'h' не может быть отрицательным числом")
        ...

    def increase_age(self, time: Union[int, float]) -> None:
        """
        Изменение возраста дерева.
        :param time: Прошедшее время с момента предыдущего определения возраста (лет)

        Примеры:
        >>> tree = Tree (10, 25)
        >>> tree.increase_age(0.5)
        """
        if not isinstance(time, (int, float)):
            raise TypeError("Прошедшее время должно быть типа int или float")
        if time < 0:
            raise ValueError("Прошедшее время не может быть отрицательным числом")
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()
