class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        if args:
            cls.houses_history.append(args[0])
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        self.number_of_floors
        self.new_floor = int(new_floor)
        if self.new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(self.new_floor):
                print(i)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


    #def __str__(self):
        #return f'Название:{self.name}, кол-во этажей:{self.number_of_floors}'


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.value = value
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
    def __radd__(self, value):
        self.value = value
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
    def __iadd__(self, value):
        self.value = value
        if isinstance(value, int):
            return House(self.name, value + self.number_of_floors)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

input()
