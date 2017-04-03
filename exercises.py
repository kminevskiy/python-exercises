def minilang(commands):
    stack = []
    register = 0
    commands_array = commands.lower().split(" ")
    for command in commands_array:
        try:
            register = int(command)
        except ValueError:
            stack_command = command
            if command == "push":
                stack.append(register)
            elif command == "add":
                register += stack.pop()
            elif command == "sub":
                register -= stack.pop()
            elif command == "print":
                print(register)
            elif command == "mult":
                register *= stack.pop()
            elif command == "div":
                register /= stack.pop()
            elif command == "mod":
                register %= stack.pop()
            elif command == "pop":
                register = stack.pop()


def binary_search(array, element):
    high = len(array) - 1
    low = 0
    while low <= high:
        mid = low + int((high - low) / 2)
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            high = mid - 1
        else:
            low = mid + 1
    return -1

import string

def letter_percentages(input_string):
    percentages = {
            "lowercase": 0,
            "uppercase": 0,
            "neither": 0
            }

    for letter in input_string:
        if letter in string.ascii_lowercase:
            percentages["lowercase"] += 1
        elif letter in string.ascii_uppercase:
            percentages["uppercase"] += 1
        else:
            percentages["neither"] += 1

    return {
            "lowercase": percentages["lowercase"] / len(input_string) * 100,
            "uppercase": percentages["uppercase"] / len(input_string) * 100,
            "neither": percentages["neither"] / len(input_string) * 100
            }

import datetime

def friday_the_13ths(year):
    month, day = 1, 13
    friday = 5
    friday_counter = 0
    while month <= 12:
        if datetime.date(year, month, day).isoweekday() == friday:
            friday_counter += 1
        month += 1
    return friday_counter


def featured(number):
    current_featured = 7
    while current_featured <= number:
        current_featured += 14
    if unique_number(current_featured):
        return current_featured
    else:
        while not unique_number(current_featured):
            current_featured += 14
        return current_featured

def unique_number(number):
    stringified_number = str(number)
    result = {}
    for number in stringified_number:
        if result.get(number):
            return False
        else:
            result[number] = 1
    return True

def sum_square_difference(number):
    squared_total = 0
    squares_total = 0
    for n in range(1, number + 1):
        squared_total += n
        squares_total += n ** 2
    return squared_total ** 2 - squares_total

def bubble_sort(array):
    updated = True
    while updated:
        updated = False
        for index, element in enumerate(array):
            try:
                if element > array[index + 1]:
                    array[index] = array[index + 1]
                    array[index + 1] = element
                    updated = True
            except IndexError:
                pass
    return array

def copy_strings(string1, string2 = ""):
    if len(string1) == 0:
        return string2;
    else:
        string2 += string1[0];
        return copy_strings(string1[1:], string2)

def findLetter(string, letter = ""):
    if len(letter) > 0 and letter == letter.upper():
        return letter
    else:
        return findLetter(string[1:], letter = string[1:][0])


def binary_search_rec(array, number):
    midpoint = int(len(array) / 2)
    if array[midpoint] == number:
        return True
    if len(array) == 2 and array[midpoint] != number:
        return False
    else:
        if number > array[midpoint]:
            return binary_search_rec(array[midpoint + 1:], number)
        else:
            return binary_search_rec(array[:midpoint], number)


def is_sorted(array):
    if len(array) == 1:
        return True
    else:
        if array[-1] >= array[-2]:
            return is_sorted(array[0:-1])
        else:
            return False


def bunny_ears(bunnies_num):
    if bunnies_num == 0:
        return 0
    else:
        return bunny_ears(bunnies_num - 1) + 2


def count8(number):
    if number == 0:
        return 0
    else:
        right_digit = number % 10
        left_digits = int(number / 10)
        if right_digit == 8 and left_digits % 10 == 8:
            return count8(int(number / 10)) + 2
        elif right_digit == 8:
            return count8(int(number / 10)) + 1
        else:
            return count8(int(number / 10))


def all_star(string):
    if len(string) <= 1:
        return string
    else:
        return string[0] + "*" + all_star(string[1:])


def pair_star(string):
    if len(string) < 2:
        return string
    else:
        if string[0] == string[1]:
            return string[0] + "*" + pair_star(string[1:])
        else:
            return string[0] + pair_star(string[1:])


def end_x(string):
    if len(string) == 0:
        return string
    else:
        if string[0] == "x":
            return end_x(string[1:]) + string[0]
        else:
            return string[0] + end_x(string[1:])

def count_pairs(string):
    if len(string) <= 2:
        return 0
    if string[0] == string[2]:
        return count_pairs(string[1:]) + 1
    else:
        return count_pairs(string[1:])


