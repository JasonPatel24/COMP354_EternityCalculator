import math # Useful math functions provided by Python
import numbers # Useful if you need to check if your value is a real number
import sys # To read user input

def isNumber(toCheck):
    return isinstance(toCheck, numbers.Number)

# Inverse Cosine
def invCos():
    print('Under construction!')
    return None

# Logarithmic
def log():
    print('Under construction!')
    return None

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
def stdDev():
    print('Under construction!')
    return None

# Exponentiation
def exp(x, y):
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

# FUNCTION TESTING
print(exp(2,0.8))
print(expGrowth(10, 0, 2))
print(meanAbsDev([10, 12, 23, 23, 16, 23, 21, 16, 15]))