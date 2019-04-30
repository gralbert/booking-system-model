from classes import *


def main():
    fund = []
    options = []

    with open('fund.txt', encoding='utf8') as file:
        for room in file:
            fund.append(room.rstrip().split())
    # (убираем кодировку)
    fund[0][0] = fund[0][0][-1]

    food_options = {'без питания': 0, 'завтрак': 280, 'полупансион': 1000}
    for room in fund:
        for food in food_options:
            options.append(Option(int(room[0]), room[1], int(room[2]), room[3], food))
    print(options)

    return


if __name__ == '__main__':
    main()