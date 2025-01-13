
class House:
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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
