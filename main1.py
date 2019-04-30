from classes import *


def delete_utf(string):
    """ Deletes the encoding service characters."""
    return string.replace('\ufeff', '').rstrip()


def get_price(option):
    """ Get price for key in sort method."""
    return option.price


def check_free(number, date, days, lst):
    """ Determines whether the room is free."""
    test_book = Booking(number, date, days)
    count = 0
    for book in lst:
        if int(number) == int(book.get_number):
            count += 1
    if not count:
        return True

    for book in lst:
        if not(test_book.get_set & book.get_set) \
                and int(number) == int(book.get_number):
            return True
    return False


def check_price(user_price, hotel_price, people):
    """ Checking whether the price is right. """
    return user_price >= hotel_price // people


def check_capacity(user_capacity, hotel_capacity):
    """ Checking whether the price is right. """
    return user_capacity <= hotel_capacity


def check_tenants_number(user_tenants, hotel_tenants):
    """ Checking whether the tenants number is right. """
    return user_tenants == hotel_tenants


def main():
    """ Main function. """
    fund = []
    options_a = []
    options_b = []
    options = []
    food_options = {'без питания', 'завтрак', 'полупансион'}

    # Formed list of rooms.
    with open('fund.txt', encoding='utf8') as file:
        for room in file:
            fund.append(room.rstrip().split())
    fund[0][0] = delete_utf(fund[0][0])

    # Make list of options, plan A.
    for room in fund:
        for food in food_options:
            options_a.append(Option(
                int(room[0]), room[1],
                int(room[2]), room[3],
                food, int(room[2])))
    options_a.sort(key=get_price, reverse=True)

    # Make list of options, plan B.
    for room in fund:
        for people in range(1, int(room[2])+1):
            for food in food_options:
                if int(room[2]) > 1:
                    options_b.append(Option(
                        int(room[0]), room[1],
                        int(room[2]), room[3],
                        food, people))
    options_b.sort(key=get_price, reverse=True)

    for option in options_b:
        option.price = 0.7

    # Make list of all options.
    options.extend(options_a)
    options.extend(options_b)

    lst_booking = []
    report_date = ''
    today_report = ''
    with open('booking.txt', encoding='utf8') as file:
        for request in file:
            lst_req = request.split()

            # Make daily report.
            if lst_req[0] != report_date:
                print(today_report)
                today_report = Report(delete_utf(lst_req[0]), fund)
            report_date = delete_utf(lst_req[0])

            # Modeling process of the booking.
            print('Поступила заявка на бронирование:')
            print(delete_utf(request), '\n')

            for option in options:

                # Make boolean vars.
                free = check_free(option.get_number, lst_req[5],
                                  int(lst_req[6]), lst_booking)
                good_price = check_price(int(lst_req[7]), get_price(option), int(lst_req[4]))
                good_capacity = check_capacity(int(lst_req[4]), option.capacity)
                right_tenants_num = check_tenants_number(int(lst_req[4]), option.get_people)

                if good_price and good_capacity and right_tenants_num and free:
                    print('Найден:')
                    print(option, '\n')

                    booking = Booking(option.get_number, lst_req[5], int(lst_req[6]))
                    lst_booking.append(booking)
                    print(booking)

                    # Change daily report.
                    if booking.get_status:
                        today_report.inc_busy()
                        today_report.add_income(get_price(option))
                        if option.get_type == 'одноместный':
                            today_report.add_single()
                        elif option.get_type == 'двухместный':
                            today_report.add_double()
                        elif option.get_type == 'полулюкс':
                            today_report.add_half_lux()
                        else:
                            today_report.add_lux()
                    else:
                        today_report.add_lose(get_price(option))
                    break
            else:
                print('Предложений по данному запросу нет. В бронировании отказано.')
            print('-----------------')
    print(today_report)
    return


if __name__ == '__main__':
    main()
