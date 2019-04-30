import random
import datetime

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


class Booking:

    def __init__(self, number, date, days):
        self._status = self.status_choice()
        self.date = date
        self.days = days
        self.set_days = self.set_days()
        self.number = number

    def __str__(self):
        if self._status:
            return 'Клиент согласен. Номер забронирован.'
        return 'Клиент отказался от варианта.'

    def __repr__(self):
        return self.__str__()

    def set_days(self):
        self.set_days = set()
        days = self.days - 1
        day = int(self.date.split('.')[0]) + days
        month = self.date.split('.')[1]
        year = self.date.split('.')[2]
        base = datetime.date(int(year), int(month), day)
        date_list = [base - datetime.timedelta(days=x) for x in range(0, days)]
        self.set_days.add(self.date)
        for date in date_list:
            self.set_days.add(date.strftime("%d.%m.%Y"))
        return self.set_days

    @staticmethod
    def status_choice():
        lst = [True, True, True, False]
        return random.choice(lst)

    @property
    def get_set(self):
        return self.set_days

    @property
    def get_number(self):
        return self.number

    @property
    def get_status(self):
        return self._status