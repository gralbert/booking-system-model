class Room:

    type_room = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
    koef_comfort = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}

    def __init__(self, number, room, max_people, comfort):
        self.number = number
        self.room = room
        self.max_people = max_people
        self.comfort = comfort
        self.price_room = self.type_room[room]*self.koef_comfort[comfort]

    def __str__(self):
        s = 'Номер: ' + self.number + '\n'
        s += 'Тип: ' + self.room + '\n'
        s += 'Вместимость: ' + self.max_people + '\n'
        s += 'Степерь комфортности: ' + self.comfort
        return s

    def __repr__(self):
        return self.__str__()

    #@property
    #def price(self):
    #    return self.price_room
    # Сеттер добавить?


class Option(Room):
    food_options = {'без питания': 0, 'завтрак': 280, 'полупансион': 1000}
    type_room = Room.type_room
    koef_comfort = Room.koef_comfort

    def __init__(self, number, room, max_people, comfort, food):
        super().__init__(number, room, max_people, comfort)
        self.food = food

    def __str__(self):
        s = ''
        for variant in self.__repr__():
            s += variant
        return s

    def __repr__(self):
        s = 'номер ' + str(self.number) + ' '
        s += self.room + ' '
        s += self.comfort + ' '
        s += 'раcсчитан на ' + str(self.max_people) + ' чел. '
        s += 'фактически ' + str(self.max_people) + ' чел. '
        self.price_room += self.food_options[self.food]
        s += self.food + ' стоимость ' + str(self.price_room) + ' руб./сутки'
        return s

    @property
    def price(self):
        return self.price_room

    #@price_food.setter
    #def price_food(self, type_food):
    #    self.price_room = self.food_options[type_food]
