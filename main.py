import math # Useful math functions provided by Python
import sys # To read user input

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
    print('Under construction!')
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
def expGrowth():
    print('Under construction!')
    return None

print(exp(2,0.8))