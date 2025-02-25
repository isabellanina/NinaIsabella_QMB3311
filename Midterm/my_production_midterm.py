# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Isabella Nina
#
# Date: February 25, 2025
# 
##################################################
#
# Sample Script for Midterm Examination: 
# Function Definitions
#
##################################################
"""
import doctest
import math

"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for another script that would
# execute the scripts (to run the doctests)
# and imports the modules to test the functions.
##################################################
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module


##################################################
# Function Definitions
##################################################


# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------

def total_revenue(units_sold: float, price: float) -> float:
    """
    Calculates total revenue from selling a product at a fixed price.

    Parameters
    ----------
    units_sold : float
        Number of units sold.
    price : float
        Price per unit in dollars.

    Returns
    -------
    total_revenue : float
        The total revenue earned, or None if invalid input is detected.

    Examples
    --------
    >>> total_revenue(1000, 1000)
    1000000

    >>> total_revenue(2000, 2000)
    4000000

    >>> total_revenue(500, 456)
    228000
    """
    if units_sold < 0 or price < 0:
        print("Invalid input: Negative values are not allowed.")
        return None

    return units_sold * price


def total_cost(units_produced: float, constant: float, fixed_costs: float) -> float:
    """
    Calculates the total cost incurred to produce a product.

    Parameters
    ----------
    units_produced : float
        Number of units produced.
    constant : float
        A constant multiplied by the square of the number of units produced.
    fixed_costs : float
        Fixed costs in dollars.

    Returns
    -------
    total_cost : float
        The total cost incurred, or None if invalid input is detected.

    Examples
    --------
    >>> total_cost(100, 50, 100)
    50100

    >>> total_cost(200, 100, 70)
    40070

    >>> total_cost(70, 120, 50)
    58850
    """
    if units_produced < 0 or constant < 0 or fixed_costs < 0:
        print("Invalid input: Negative values detected. Returning None.")
        return None
    total_cost = constant * (units_produced ** 2) + fixed_costs
    return total_cost


#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

def total_profit(num_units: float, unit_price: float, multiplier: float, fixed_cost: float) -> float:
    """
    Calculates the profit earned by the company when they produce and sell q units

    Parameters
    ----------
    num_units : float
        number of units.
    unit_price : float
        DESCROPTION. 
    multiplier : float
        .
    fixed_cost : float
        DESCRIPTION.

    Returns
    -------
    float
        Represents the expected profit.

    """
    
    expected_profit = unit_price * num_units - total_cost 
    return expected_profit



def max_profit_calc(unit_price: float, multiplier: float, fixed_cost: float) -> float:
     """
     Calculates the company's optimal production level

     Parameters
     ----------
     num_units : float
         DESCRIPTION.
     unit_price : float
         DESCRIPTION.
     multiplier : float
         DESCRIPTION.
     fixed_cost : float
         DESCRIPTION.

     Returns
     -------
     float
         DESCRIPTION.

     """

    q_star = unit_price / (2*multiplier)
 
    total_profit = expected_profit
    if expected_profit < 0:
        q_star = 0
    return q_star 
    
    
def profit_max_q(q_max:float, step:float, unit_price:float, 
                 multiplier:float, fixed_cost:float) -> float:
    """
    Calculates the company's profit max q

    Parameters
    ----------
    q_max : float
        DESCRIPTION.
    step : float
        DESCRIPTION.
    unit_price : float
        DESCRIPTION.
    multiplier : float
        DESCRIPTION.
    fixed_cost : float
    

    Returns
    -------
    float
        DESCRIPTION.

    """
    
    q_list = np.arange(0, q_max, step)
    
    max_profit = 0
    i_max = 0
    
    for i in range(len(q_list)):
        q_i = q_list[i]
        profit_i = total_profit(q_i, unit_price, multiplier, fixed_cost)
        if (profit_i > max_profit):
            i_max = i
            max_profit = profit_i
            
    if (max_profit < 0):
        return 0
    else:
        return q_list[i_max]
        
   
# Exercise 1


# Exercise 2



# Exercise 3




# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include examples in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 

    
    
 
if __name__ == "__main__":
    doctest.testmod()


##################################################
# End
##################################################
