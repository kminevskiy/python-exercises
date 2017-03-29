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

