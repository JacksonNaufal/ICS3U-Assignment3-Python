#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a integer, positive, negative, or zero program


def main():

    # This i

    # input
    user_number = int(input("Enter your number here! : "))

    # process & output
    if user_number > 0:
        print("\nyour number  is positive!")
    elif user_number < 0:
        print("\nYour number is negative!")
    else:
        print("\nYour number is zero!")
    print("\nDone!")


if __name__ == "__main__":
    main()
