#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a guess the random number program

import random


def main():

    # This is a random number guesser

    # input
    guess_Number = int(input("Enter your first guess here (0-9): "))

    random_Number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    if guess_Number == random_Number:
        print("\nGuess is correct!")
        print("\nDone!")
    else:
        print("\nYour guess is incorrect!")
        print("\nThe correct number is {0}.".format(random_Number))
        print("\nDone.")


if __name__ == "__main__":
    main()
