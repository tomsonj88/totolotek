"""
ToDo dopisac doscrstringa
"""
import random

win = False


def generate_numbers(start=1, stop=49, numbers_quantity=6):
    numbers = set(random.sample(range(start, stop), numbers_quantity))
    return numbers

generate_numbers()
