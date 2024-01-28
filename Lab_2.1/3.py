from typing import Union


import doctest

class Pipe:
    def __init__(self, radius: Union[int, float], lenght: Union[int, float]):
        """
               Создание и подготовка к работе объекта "Труба"

               :param radius: радиус трубы (м)
               :param lenght: длина трубы (м)

               Примеры:
                   >>> pipe = Pipe (0.3, 10)  # инициализация экземпляра класса
               """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус трубы должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус трубы должен быть положительным числом")
        self.radius = radius

        if not isinstance(lenght, (int, float)):
            raise TypeError("Длина трубы должна быть типа int или float")
        if lenght <= 0:
            raise ValueError("Длина трубы должна быть положительным число")
        self.lenght = lenght

    def cross_sectional_area_pipe(self) -> float:
        """
        Функция которая высчитывает площадь поперечного сечения трубы

        :return: Площадь поперечного сечения трубы

        Примеры:
        >>> pipe = Pipe (0.3, 10)
        >>> pipe.cross_sectional_area_pipe()
        """
        ...

    def volume_pipe(self) -> float:
        """
        Функция которая высчитывает объем трубы

        :return: Объем трубы

        Примеры:
        >>> pipe = Pipe (0.3, 10)
        >>> pipe.volume_pipe()
        """
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()
