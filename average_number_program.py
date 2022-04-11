#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: April 2022
# This is a average number calculator program


def main():

    # This is a average number calculator

    # input
    print("This calculator will calculate your three numbers!")
    print("Note: this calculator will not round!")
    print("Note: Max number is 100, Min number is 0")
    number_one_string = input("What is your first number?: ")
    number_two_string = input("What is your second number?: ")
    number_three_string = input("What is your third number?: ")
    # process & output
    try:

        number_one = float(number_one_string)
        number_two = float(number_two_string)
        number_three = float(number_three_string)

        if number_one >= 100:
            print("\nInvalid Number, please try again!! (Number 1)")
        elif number_two >= 100:
            print("\nInvalid Number, please try again!(Number 2)")
        elif number_three >= 100:
            print("\nInvalid Number, please try again! (Number 3)")
        elif number_one < 0:
            print("\nInvalid Number, please try again! (Number 1)")
        elif number_two < 0:
            print("\nInvalid Number, please try again! (Number 2)")
        elif number_three < 0:
            print("\nInvalid Number, please try again! (Number 3)")

        else:
            average = (number_one + number_two + number_three) / 3
            actual = round(average, 2)
            print("Your average between the 3 numbers is {0}".format(actual))

    except Exception:
        print("Invalid Input")
    print("\nDone.")


if __name__ == "__main__":
    main()
