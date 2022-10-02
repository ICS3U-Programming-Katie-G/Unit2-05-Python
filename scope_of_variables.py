#!/usr/bin/env python3

# Created by: Katie
# Created on: October 1st 2022
# This program shows the scope of variables
# with assignment statements.


def main():
    # variable definition
    number_of_students = 6
    width = 50.0
    length = 5.5
    some_words1 = "Hello"
    some_words2 = "World!"

    # using assignment statements
    number_of_students = number_of_students + 5
    area_of_rectangle = length * width
    hello_world = some_words1 + ", " + some_words2

    # output
    print("The number of students is: " + str(number_of_students))
    print("The area of a rectangle is: " + str(area_of_rectangle) + " cm²")
    print(hello_world)

    print("\nDone.")


if __name__ == "__main__":
    main()
