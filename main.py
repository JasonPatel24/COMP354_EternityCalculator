import math # Useful math functions provided by Python
import sys # To read user input

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
def exp():
    print('Under construction!')
    return None

# Exponential Growth
def expGrowth():
    print('Under construction!')
    return None

try:
    print(invCos(0.76)) 
except NameError: # Handles undefined variables that may be present before the function is called
    print("Input must be a number")
