#!/usr/bin/env python3
# Created by: Brandon
# Created on: December 10th, 2025
# This program calculates the mark for a given level using functions


def calc_mark(level):

    # Default return value
    percentage = -1

    # Determine the middle percentage based on the level
    if level == "4++":
        percentage = 98
    elif level == "4+":
        percentage = 95
    elif level == "4":
        percentage = 90.5
    elif level == "4-":
        percentage = 83
    elif level == "3+":
        percentage = 78
    elif level == "3":
        percentage = 74.5
    elif level == "3-":
        percentage = 71
    elif level == "2+":
        percentage = 68
    elif level == "2":
        percentage = 64.5
    elif level == "2-":
        percentage = 61
    elif level == "1+":
        percentage = 58
    elif level == "1":
        percentage = 54.5
    elif level == "1-":
        percentage = 51
    elif level == "R":
        percentage = 24.5

    # Return statement
    return percentage


def main():
    # Get level from user
    level = input("Enter Your Level: ")

    # Calculate the middle percentage and display it
    percentage = calc_mark(level)
    if percentage != -1:
        print(f"The middle percentage for level {level} is: {percentage}%")
    else:
        print("Invalid level entered.")


if __name__ == "__main__":
    main()
