#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        value = ""
        if (i % 3) == 0:
            value += "Fizz"
        if (i % 5) == 0:
            value += "Buzz"
        if value == "":
            value = i
        print(value, end=" ")
