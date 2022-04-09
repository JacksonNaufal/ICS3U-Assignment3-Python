#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: April 2022
# This is a average number calculator program


def main():

    # This is a average number calculator

    # input
    print("This calculator will calculate your three numbers!")
    print(
        "Note: this calculator rounds to 2 decimals, and will not calculate numbers greater than 100 or less than 0!"
    )
    number_one_string = input("What is your first number?: ")
    number_two_string = input("What is your second number?: ")
    number_three_string = input("What is your third number?: ")

    # process & output
    try:

            number_one = int(number_one_string)
            number_two = int(number_two_string)
            number_three = int(number_three_string)

            if number_one >= 0 and number_one >= 100:
                print(
                    "\nThe first number you inputted, which is {0} is too large, please try again!".format(
                        number_one
                    )
                )
                if number_two >= 0 and number_two >= 100:
                    print(
                        "\nThe second number you inputted, which is {0} is too large, please try again!".format(
                        number_two
                        )
                    )
                    if number_three >= 0 and number_three >= 100:
                        print(
                            "\nThe second number you inputted, which is {0} is too large, please try again!".format(
                                number_three
                            )
                        )
    
            else:
                print((number_one + number_two + number_three) / 3)
            
    except Exception:
        print("Invalid Input")
    print("\nDone.")


if __name__ == "__main__":
    main()
