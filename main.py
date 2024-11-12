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
def meanAbsDev():
    print('Under construction!')
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

# Exponential Growth
def expGrowth(a, b, x):
    try:
        # Error handling
        if (not isNumber(a) or not isNumber(b) or not isNumber(x)):
            print('ERROR: At least one of \'a\', \'b\', or \'x\' is not a valid number.')
            exit()

        if (a <= 0):
            print('ERROR: Base \'a\' must be greater than 0.')
            exit()

        if (b > 1 or b < 0):
            print('ERROR: Growth/Decay rate \'b\' must be a real number between 0 and 1.')
            exit()

        if (x < 0):
            print('ERROR: exponent \'x\' cannot be negative.')
            exit()

        # Perform exponential growth/decay on provided values and return result
        return a * exp(b, x)
    except:
        print('An unhandled exception occurred. Please report this issue by sending us an email with the attempted parameters sent to the exponential growth/decay function.')

# FUNCTION TESTING
print(exp(2,0.8))
print(expGrowth(10, 0.6, 12))