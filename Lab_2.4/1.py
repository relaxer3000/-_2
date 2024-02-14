if __name__ == "__main__":
    class Car:
        def __init__(self, brand: str, cost: float):
            """
                   Создание и подготовка к работе объекта "Автомобиль"
                   :param brand: марка автомобиля
                   :param cost: стоимость автомобиля, тыс. $
                   Примеры:
                       >>> car = Car ('Volvo', 35000)  # инициализация экземпляра класса
                   """
            self.brand = None
            self.cost = None
            self.init_brand(brand)
            self.init_cost(cost)

        def init_brand(self, brand: str) -> None:
            if not isinstance(brand, str):
                raise TypeError('Марка автомобиля должна быть типа string')
            else:
                self.brand = brand

        def init_cost(self, cost: float) -> None:
            if isinstance(cost, int):
                cost = float(cost)
            if not isinstance(cost, float):
                raise TypeError('Cтоимость должна быть типа float')
            if cost <= 0:
                raise ValueError('Стоимость не может быть отрицательным числом')
            else:
                self.cost = cost

        def credit(self, percent) -> float:
            """
                   Функция которая считает ежемесячный платеж по кредиту
                   :param percent: Процент по кредиту
                   :return: Ежемесячный платеж по кредиту
                   Примеры:
                   >>> car = Car ('Volvo', 35000)
                   >>> car.percent(15.5)
                   """
            ...
        @staticmethod
        def concern() -> str:
            """
                   Функция которая определяет какому концерну принадлежит марка
                   :return: Название концерна
                   Примеры:
                   >>> car = Car ('Volvo', 35000)
                   >>> car.concern()
                   """
            ...

        def __str__(self):
            return f"Автомобиль марки {self.brand}. Стоимость: {self.cost} тыс. $"

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r}, cost={self.cost!r})"


    class Truck(Car):
        def __init__(self, brand: str, cost: float, load_capacity: float):
            """
                Создание и подготовка к работе объекта "Грузовой автомобиль"
                :param brand: марка автомобиля
                :param cost: стоимость автомобиля, тыс. $
                :param load_capacity: грузоподъемность автомобиля, тонн
                Примеры:
                    >>> truck = Truck ('Volvo', 100000, 20)  # инициализация экземпляра класса
                """
            super().__init__(brand, cost)
            self.load_capacity = None
            self.init_load_capacity(load_capacity)
        def init_load_capacity(self, load_capacity: float) -> None:
            if isinstance(load_capacity, int):
                load_capacity = float(load_capacity)
            if not isinstance(load_capacity, float):
                raise TypeError('Грузоподъемность должна быть типа float')
            if load_capacity <= 0:
                raise ValueError('Грузоподъемность не может быть отрицательным числом')
            else:
                self.load_capacity = load_capacity

        def concern(self):
            super().concern()

        def credit(self, percent: float, x: float):
            """
                Процент по грузовым автомобилям ниже в x раз.
                :param x: параметр, определяющий, во сколько раз процент по кредиту по грузовым автомобилям
                ниже стандартного процента по кредиту по автомобилям.
                """
            if isinstance(x, int):
                x = float(x)
            if not isinstance(x, float):
                raise TypeError('Параметр x должен быть типа float')
            if x < 1:
                raise ValueError('Параметр x должен быть больше или равен 1')
            percent_new = 1 / x
            super().credit(percent_new)

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r}, cost={self.cost!r}, load_capacity={self.load_capacity!r})"

    pass
