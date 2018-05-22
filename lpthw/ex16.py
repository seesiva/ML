#!/bin/python

import sys

"""
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!
"""



def main():
    meal_cost = float(raw_input().strip())
    tip_percent = int(raw_input().strip())
    tax_percent = int(raw_input().strip())
    tip = meal_cost * (float(tip_percent)/100)
    tax = meal_cost * (float(tax_percent)/100)
    meal_total_cost=meal_cost + tip + tax
    print "The total meal cost is "+str(int(round(meal_total_cost)))+" dollars."
    
if __name__=="__main__":
    main() # output 10