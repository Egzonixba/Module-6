
#Task 1
import random

def roll_dice():
    return random.randint(1, 6)

def main():
    rolls = 0
    while True:
        result = roll_dice()
        rolls += 1
        print(f"Roll {rolls}: {result}")
        if result == 6:
            break

if __name__ == "__main__":
    main()


#Task 2

import random


def roll_dice(num_sides):
    return random.randint(1, num_sides)


def main():
    num_sides = int(input("Enter the number of sides on the dice: "))
    max_roll = num_sides
    rolls = 0

    while True:
        result = roll_dice(num_sides)
        rolls += 1
        print(f"Roll {rolls}: {result}")

        if result == max_roll:
            break

if __name__ == "__main__":
    main()


#Task 3
import math


def convert_gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters



def main():
    while True:
        gallons = float(input("Enter a quantity in American gallons (or a negative value to quit): "))

        if gallons < 0:
            break

        liters = convert_gallons_to_liters(gallons)
        print(f"{gallons} American gallons is equal to {liters:.2f} liters")


if __name__ == "__main__":
    main()


#Task 4
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():

    integer_list = [1, 2, 3, 4, 5]


    result = sum_of_list(integer_list)


    print("The sum of the list is:", result)

if __name__ == "__main__":
    main()

#Task 5

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def main():

    integer_list = [2, 4, 6, 8, 10]


    result = sum_of_list(integer_list)


    print("The sum of the list is:", result)

if __name__ == "__main__":
    main()

#Task 6
def calculate_unit_price(diameter, price):

    radius = diameter / 2

    area_square_meters = (3.14159 * radius ** 2) / 10000  # Convert from cm^2 to m^2


    unit_price = price / area_square_meters

    return unit_price


def main():

    diameter1 = float(input("Enter the diameter of the first pizza (in centimeters): "))
    price1 = float(input("Enter the price of the first pizza (in euros): "))


    diameter2 = float(input("Enter the diameter of the second pizza (in centimeters): "))
    price2 = float(input("Enter the price of the second pizza (in euros): "))


    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)


    if unit_price1 < unit_price2:
        print("The first pizza offers better value for money.")
    elif unit_price1 > unit_price2:
        print("The second pizza offers better value for money.")
    else:
        print("Both pizzas have the same unit price.")

if __name__ == "__main__":
    main()

#Task 7