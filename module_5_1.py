class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, number):
        if number == 0 or number > self.number_of_floors:
            print('Такого этажа не существует');
            return
        for flat in range(1, number+1):
            print(flat)

h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 5)

h1.go_to(5)

h2.go_to(10)