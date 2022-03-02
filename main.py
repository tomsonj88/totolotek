"""
Ile wydać by wygrać w totolotka?
"""
import random

lottery_ticket_price = 3


def generate_numbers(start=1, stop=49, numbers_quantity=6):
    """
    Generate pseudorandom numbers from range <start,stop>
    Function generate by default 6 numbers from range 1,49
    """
    numbers = set(random.sample(range(start, stop), numbers_quantity))
    return numbers


def count_lottery_ticket_cost(number_of_lotteries, lottery_cost):
    """
    Count cost of lottery tickets
    :param number_of_lotteries: int
    :param lottery_cost: int
    :return: int
    """
    cost = number_of_lotteries * lottery_cost
    return cost


def count_lottery_until_you_win():
    """
    Count how many lotteries you have to play to win
    """
    counter = 0
    my_numbers = generate_numbers()
    lotto_draw = {}

    while lotto_draw != my_numbers:
        lotto_draw = generate_numbers()
        counter += 1

    print(my_numbers)
    print(lotto_draw)
    return counter


lottery_quantity = count_lottery_until_you_win()
total_cost = count_lottery_ticket_cost(lottery_quantity, lottery_ticket_price)

print(f"You need {lottery_quantity:,} lotteries to win")
print(f"You have to spend {total_cost:,} zloty to win")


