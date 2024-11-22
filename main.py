import math # Useful math functions provided by Python
import numbers # Useful if you need to check if your value is a real number
import sys # To read user input
import random
import time


def isNumber(toCheck):
    return isinstance(toCheck, numbers.Number)

def isNumber(toCheck):
    return isinstance(toCheck, numbers.Number)

# Inverse Cosine
def invCos(x, terms=20):
    # Validate and convert input
    try:
        x = float(x)  # Convert input to float if possible
    except (ValueError, TypeError, NameError):
        return "Input must be a number"
    
    # Check if input is within the valid range for arccosine
    if not -1 <= x <= 1:
        return "Input must be in the range -1 to 1"
    
    # Start calculating the inverse cosine using Taylor series
    pi = 3.141592653589793
    result = pi / 2
    sign = 1  # Alternating sign for each term
    
    for n in range(terms):
        # Calculate factorial terms manually
        numerator_factorial = 1
        for i in range(1, 2 * n + 1):
            numerator_factorial *= i
        
        denominator_factorial = 1
        for i in range(1, n + 1):
            denominator_factorial *= i
        
        # Calculate the current term of the Taylor series
        term = (numerator_factorial / ((2**n * denominator_factorial)**2 * (2 * n + 1))) * (x**(2 * n + 1))
        
        # Update result with alternating sign
        result -= sign * term
        sign = -sign
    
    return result

# Logarithmic that will
def log(argument, base):
    if (base == 2):
        return log_helper(argument)
    if (base < 0 or base == 1):
        print("Logarithmic function is neither defined for negative bases nor one.")
        exit()
    nominator = log_helper(argument)
    denominator = log_helper(base)
    result = nominator/denominator
    return result

#Define log function with base 2 for simplicity.
def log_helper(argument):
    if argument <= 0:
        print("Logarithmic function is neither defined for negative arguments nor zero.")
    
    if (argument == 1): #1 as an argument
        return 0
    
    #We will try to narrow down the answer using binary search.
    if argument > 1:
        low, high = 0, argument

    else: #If argument is lesser than 1, then the answer must be negative. Set the low bound to a sufficiently negative number.
        low, high = -20, 0

    
    while high - low > 1e-11:   #If interval of answer is higher than the precision, try to narrow again.
        mid = (low + high) / 2      #Find the middle ground of the interval
        power = 2 ** mid            #Find the result of 2^mid
        if power < argument:        #If the result of 2^mid is lower than argument given, mid will become new low.
            low = mid
        else:                       #Otherwise, if its higher than the argument given, mid will become new high.
            high = mid
    return (low + high) / 2         #Return middle of interval as the answer


# Mean absolute deviation
def meanAbsDev(data):
    try:
        # Error handling
        for data_point in data:
            # Ensure all data points are valid numbers
            if (not isNumber(data_point)):
                print(f"ERROR: '{data_point}' is not a valid number.")
                exit()

        # Calculate the mean of the dataset
        mean = sum(data) / len(data)
        total_deviation = 0

        # Calculate the absolute deviations from the mean
        for data_point in data:
            total_deviation += abs(data_point - mean)

        # Calculate and return the mean of the absolute deviations
        return total_deviation / len(data)
    except TypeError as e:
        print('An unhandled exception occurred. Please report this issue by sending us an email with the attempted parameters sent to the mean absolute deviation function.')
        print(f"Details: {e}")
        return None

# Standard deviation
def stdDev(data):
    try:
        # Error handling to ensure all data points are valid numbers
        for data_point in data:
            if not isNumber(data_point):
                print(f"ERROR: '{data_point}' is not a valid number.")
                return None

        # Calculate the mean of the dataset
        mean = sum(data) / len(data)
        # Calculate the variance
        variance = sum((data_point - mean) ** 2 for data_point in data) / len(data)
        # Return the square root of the variance, which is the standard deviation
        return math.sqrt(variance)
    except TypeError as e:
        print("An unhandled exception occurred. Please report this issue by sending us an email with the attempted parameters.")
        print(f"Details: {e}")
        return None

# Exponentiation
def exp(x, y):
    
    #Error handling for 2 cases
    if x == 0 and y == 0:
            return "ERROR x value cannot be 0 while y is 0"
    
    if x == 0 and y < 0:
        return "ERROR x value cannot be 0 while y is negative"
    
    if y == 0:
        return 1
    if y < 0:
        x = 1/x
        y = -y
    integerPart = int(y)
    decimalPart = y-integerPart

    answer = 1
    for _ in range(integerPart):
        answer *= x
    
    if decimalPart != 0:
        answer *= x**decimalPart

    return answer
    
# Exponential Growth (for decay, provide a value for b such that 0 < b < 1)
def expGrowth(a, b, x):
    try:
        # Error handling
        if (not isNumber(a) or not isNumber(b) or not isNumber(x)): # Ensure all parameters are valid real numbers
            print('ERROR: At least one of \'a\', \'b\', or \'x\' is not a valid number.')
            exit()

        if (a <= 0): # base value must be positive
            print('ERROR: Base \'a\' must be greater than 0.')
            exit()

        if (b < 0): # growth/decay rate cannot be negative
            print('ERROR: Growth/Decay rate \'b\' must be a real number greater than 0.')
            exit()

        if (x < 0): # exponent cannot be negative
            print('ERROR: exponent \'x\' cannot be negative.')
            exit()

        # Perform exponential growth/decay on provided values and return result
        return a * exp(b, x)
    except:
        print('An unhandled exception occurred. Please report this issue by sending us an email with the attempted parameters sent to the exponential growth/decay function.')
        
def log_test_cases(): 
    for test in range (1, 51):
        base = random.uniform(1.1, 10)
        argument = random.uniform(0.1, 350)

        expected_log = math.log(argument, base)

        # Compute the result using the custom log function
        result = log(argument, base)

        if abs(result - expected_log) < 1e-9:
            print("Test case: " + str(test) + " success")
        else:
            print(f"Test case: {test} failed: log({argument}, {base}) = {result}, expected {expected_log}, precision {result - expected_log}")



# FUNCTION TESTING
"""
log_test_cases()
print(exp(2,0.8))
print(expGrowth(10, 0, 2))
print(meanAbsDev([10, 12, 23, 23, 16, 23, 21, 16, 15]))
print(stdDev([10, 12, 23, 23, 16, 23, 21, 16, 15]))

try: # Handles undefined variables that may be present before the function is called
    print(invCos(0.76)) 
except NameError: 
    print("Input must be a number")

"""
import tkinter as tk
import re
import math

def TUI_calculator():
    main_functions = ["arccos(x)", "ab^x", "log_b(x)", "MAD", "σ", "x^y"]

    print("Welcome to Eternity TUI Calculator!\n")
    
    while(True):
        print("\nPlease choose one of the following functions to perform: ")
        index = 1
        for element in main_functions:
            print(f"{index}. {element}")
            index += 1
        print("0. Exit")
        while(True):
            try:
                user_input = int(input("Please enter a valid index (0 to 6): "))
                if 0 <= user_input <= 6:
                    break
                else:
                    print("Input out of range. Please enter a number between 0 and 6.")
            except ValueError:
                print("Input must be an integer!")
    
        if user_input == 1:
            print("You selected arccos(x)")
            try:
                x = float(eval(input("Please enter the value of x: ")))
                print(invCos(x))
            except ValueError:
                print("Invalid input! Please enter numeric values.")

        elif user_input == 2:
            print("You selected ab^x")
            try:
                a = float(eval(input("Please enter the value of a: ")))
                b = float(eval(input("Please enter the value of b: ")))
                x = float(eval(input("Please enter the value of x: ")))
                print("The result: " + str(expGrowth(a, b, x)))
            except ValueError:
                print("Invalid input! Please enter numeric values.")

        elif user_input == 3:
            print("You selected log_b(x)")
            try:
                b = float(eval(input("Please enter the value of b: ")))
                if b == 0:
                    raise Exception("B cannot be zero.")
                x = float(eval(input("Please enter the value of x: ")))
                print("The result: " + str(log(x, b)))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
            except Exception as exc:
                print(exc) 

        elif user_input == 4:
            print("You selected MAD")
            input_list = input("Please enter the values you wish to calculate the MAD of separated by commas (,).")
            input_list = input_list.split(',')
            input_list = [x for x in input_list if x.strip()] #To remove empty strings
            try:
                numbers = [float(x.strip()) for x in input_list]  
            except ValueError:
                return
            print("The result: " + str(meanAbsDev(numbers)))

        elif user_input == 5:
            print("You selected σ")
            input_list = input("Please enter the values you wish to calculate the stdev of separated by commas (,).")
            input_list = input_list.split(',')
            input_list = [x for x in input_list if x.strip()] #To remove empty strings
            try:
                numbers = [float(x.strip()) for x in input_list]  
            except ValueError:
                return
            print("The result: " + str(stdDev(numbers)))   

        elif user_input == 6:
            print("You selected x^y")
            try:
                x = float(eval(input("Please enter the value of x: ")))
                y = float(eval(input("Please enter the value of y: ")))
                print("The result: " + str(exp(x, y)))
            except ValueError:
                print("Error: Please enter valid numeric values for x and y.")

        elif user_input == 0:
            print("Thank you for using Eternity. Exiting program now")
            break
        else:
            print("Invalid selection, please choose a number between 1 and 6.")
        time.sleep(0.5)

        
def GUI_calculator():
    None

print("\nWould you like to use our calculator as a: \n0. TUI (Textual User Interface)\n1. GUI (Graphical User Interface) *NOT AVAILABLE YET*\n")
while(True):
    user_input = (input("Please enter 0 or 1: ")).strip()
    if (user_input == "0"):
        TUI_calculator()
        break
    elif (user_input == "1"):
        GUI_calculator()
        break
    else:
        print("Invalid input, try again.")




    

