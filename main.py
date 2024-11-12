import math # Useful math functions provided by Python
import numbers # Useful if you need to check if your value is a real number
import sys # To read user input
import random


def isNumber(toCheck):
    return isinstance(toCheck, numbers.Number)

def isNumber(toCheck):
    return isinstance(toCheck, numbers.Number)

# Inverse Cosine
def invCos():
    print('Under construction!')
    return None

# Logarithmic that will
def log(argument, base, precision = 1e-11):
    if (base == 2):
        return log_helper(argument, precision)
    if (base < 0 or base == 1):
        print("Logarithmic function is neither defined for negative bases nor one.")
        exit()
    nominator = log_helper(argument, precision)
    denominator = log_helper(base, precision)
    result = nominator/denominator
    return result

#Define log function with base 2 for simplicity.
def log_helper(argument, precision = 1e-11):
    if argument <= 0:
        print("Logarithmic function is neither defined for negative arguments nor zero.")
    
    if (argument == 1): #1 as an argument
        return 0
    
    #We will try to narrow down the answer using binary search.
    if argument > 1:
        low, high = 0, argument

    else: #If argument is lesser than 1, then the answer must be negative. Set the low bound to a sufficiently negative number.
        low, high = -20, 0

    
    while high - low > precision:   #If interval of answer is higher than the precision, try to narrow again.
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
        
def log_test_cases(precision=1e-8): 
    for test in range (1, 51):
        base = random.uniform(1.1, 10)
        argument = random.uniform(0.1, 350)

        expected_log = math.log(argument, base)

        # Compute the result using the custom log function
        result = log(argument, base)

        if abs(result - expected_log) < precision:
            print("Test case: " + str(test) + " success")
        else:
            print(f"Test case: {test} failed: log({argument}, {base}) = {result}, expected {expected_log}, precision {result - expected_log}")

log_test_cases()

# FUNCTION TESTING
print(exp(2,0.8))
print(expGrowth(10, 0, 2))
print(meanAbsDev([10, 12, 23, 23, 16, 23, 21, 16, 15]))
