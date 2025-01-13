class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(" Такого этажа не существует")
        else:
            i = 1
            while i <= new_floor:
                print(i)
                i += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(self, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print("Некорректное сравнение")

    def __lt__(self, other):
        if isinstance(self, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print("Некорректное сравнение")

    def __le__(self, other):
        if isinstance(self, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print("Некорректное сравнение")

    def __gt__(self, other):
        if isinstance(self, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print("Некорректное сравнение")

    def __ge__(self, other):
        if isinstance(self, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print("Некорректное сравнение")

    def __ne__(self, other):
        if isinstance(self, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print("Некорректное сравнение")

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            print("Некорректное действие")

# Описал методы __radd__ и __iadd__ для уяснения по отраженным операторам и составным присваиваниям
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self
        else:
            print("Некорректное действие")

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print("Некорректное действие")

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)