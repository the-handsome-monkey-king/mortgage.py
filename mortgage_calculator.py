#!/usr/bin/env python
"""mortgage_calculator.py

Find the given periodical payments for a mortgage
over a set number of years with its principal, 
length of period, and interest rate."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

def main():
    principal = get_int("Please enter the principal: ")
    years = get_int("Please enter the years for the mortgage: ")
    interest = get_interest()
    period = get_period()

    total_payment = (
        (float)(principal) *
        (1.0 + interest / period)**(period * (float)(years)))
    periodic_payment = total_payment / period
    total_payment = round(total_payment, 2)
    periodic_payment = round(periodic_payment, 2)

    print("Final Loan Worth: {}".format(total_payment))
    print("Periodic Payment: {}".format(periodic_payment))

def get_int(msg):
    while(True):
        try:
            user_int = (int)(raw_input(msg))
            return user_int
        except(ValueError):
            print("That response is invalid. Please try again.")

def get_interest():
    while(True):
        try:
            interest = (float)(raw_input(
                "Please enter the interest as a decimal: "))
            return interest
        except(ValueError):
            print("That response is invalid. Please try again.")

def get_period():
    periods = {
        'months': 12.0,
        'weeks': 48.0,
        'days': 365.0}

    while(True):
        period = raw_input(
            "Please enter a period (months|weeks|days): ")
        if period in periods.keys():
            return periods[period]

if __name__ == "__main__":
    main()
