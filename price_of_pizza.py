#!/usr/bin/env python3

# Created by Sean McLeod
# Created on November 2020
# This program can calculate the cost of a pizza when the user enters
#    the diameter of their pizza

import constants


def main():
    # This function calculates the cost of a pizza

    # input
    diameter = int(input("Enter the diameter of the pizza (inch):"))

    # process
    sub_total = constants.LABOR + constants.RENT + \
        (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("The total price of a {0} inch pizza is ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
