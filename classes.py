import random
import datetime


class Room:
    type_room = {'одноместный': 2900,
                 'двухместный': 2300,
                 'полулюкс': 3200,
                 'люкс': 4100}

    koef_comfort = {'стандарт': 1,
                    'стандарт_улучшенный': 1.2,
                    'апартамент': 1.5}

    def __init__(self, number, room, max_people, comfort):
        self.number = number
        self.room = room
        self.max_people = max_people
        self.comfort = comfort
        self.price_room = self.type_room[room]\
                          *self.koef_comfort[comfort]

    def __str__(self):
        s = 'Номер: ' + self.number + '\n'
        s += 'Тип: ' + self.room + '\n'
        s += 'Вместимость: ' + self.max_people + '\n'
        s += 'Степерь комфортности: ' + self.comfort
        return s

    def __repr__(self):
        return self.__str__()


class Option(Room):
    food_options = {'без питания': 0,
                    'завтрак': 280,
                    'полупансион': 1000}
    type_room = Room.type_room
    koef_comfort = Room.koef_comfort

    def __init__(self, number, room, max_people, comfort, food, people):
        super().__init__(number, room, max_people, comfort)
        self.food = food
        self.people = people
        self.price_room1 = (self.price_room
                            + self.food_options[self.food]) * self.max_people

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        s = 'номер ' + str(self.number) + ' '
        s += self.room + ' '
        s += self.comfort + ' '
        s += 'расcчитан на ' + str(self.max_people) + ' чел. '
        s += 'фактически ' + str(self.people) + ' чел. '
        s += self.food + ' стоимость ' + str(self.price_room1) + ' руб./сутки'
        return s

    @property
    def price(self):
        return self.price_room1

    @price.setter
    def price(self, percent):
        self.price_room1 = round((self.price_room * percent) * self.max_people
                                 + (self.food_options[self.food]) * self.people, 2)

    @property
    def get_number(self):
        return self.number

    @property
    def get_food(self):
        return self.food_options

    @property
    def get_people(self):
        return self.people

    @property
    def get_type(self):
        return self.room

    @property
    def capacity(self):
        return self.max_people


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


class Report:
    def __init__(self, date, rooms):
        self.date = date
        self.rooms = rooms
        self.busy = 0

        self.single_room = 0
        self.double_room = 0
        self.half_lux = 0
        self.lux = 0

        self.income = 0
        self.lose = 0

    def __str__(self):
        self.free = len(self.rooms) - self.busy
        self.load = round((self.busy / len(self.rooms)) * 100, 2)
        s = 'Итог за ' + self.date + '\n'
        s += 'Количество занятых номеров: ' + str(self.busy) + '\n'
        s += 'Количество свободных номеров: ' + str(self.free) + '\n'
        s += 'Занятость по категориям:' + '\n'
        s += 'Одноместных: ' + str(self.single_room) + '\n'
        s += 'Двухместных: ' + str(self.double_room) + '\n'
        s += 'Полулюкс: ' + str(self.half_lux) + '\n'
        s += 'Люкс: ' + str(self.lux) + '\n'
        s += 'Процент загруженности гостиницы: ' + str(self.load) + '%\n'
        s += 'Доход за день: ' + str(self.income) + '\n'
        s += 'Упущенный доход: ' + str(self.lose) + '\n'
        s += '-----------------'
        return s

    def __repr__(self):
        return self.__str__()

    def inc_busy(self):
        self.busy += 1

    def add_income(self, value):
        self.income += value

    def add_single(self):
        self.single_room += 1

    def add_double(self):
        self.double_room += 1

    def add_half_lux(self):
        self.half_lux += 1

    def add_lux(self):
        self.lux += 1

    def add_lose(self, value):
        self.lose += value
