import math # Useful math functions provided by Python
import sys # To read user input

# Inverse Cosine
def invCos(x, terms=20):
    try:
        # Handle string input
        if isinstance(x, str):
            try:
                x = float(x)
            except ValueError:
                return "Input must be a number"
        
        # Handle undefined variable names
        if not isinstance(x, (int, float)):
            return "Input must be a number"
        
        # Check if input is within the valid range for arccosine
        if not -1 <= x <= 1:
            return "Input must be in the range -1 to 1"
        
        # Start calculating the inverse cosine using Taylor series
        pi = 3.141592653589793
        result = pi / 2
        sign = 1  # Alternating sign for each term
        
        for n in range(terms):
            # Calculate the factorial terms manually
            numerator_factorial = 1
            for i in range(1, 2 * n + 1):
                numerator_factorial *= i
            
            denominator_factorial = 1
            for i in range(1, n + 1):
                denominator_factorial *= i
            
            term = (numerator_factorial / ((2**n * denominator_factorial)**2 * (2 * n + 1))) * (x**(2 * n + 1))
            
            result -= sign * term
            sign = -sign  # Alternate the sign for the next term
        
        return result
    
    except Exception:
        return "Input must be a number"

# testing
try:
    result = invCos(hi)  # undefined variable
    print(f"Result: {result}")
except NameError:
    print("Result: Input must be a number")

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
