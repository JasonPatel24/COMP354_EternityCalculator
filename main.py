import math # Useful math functions provided by Python
import numbers # Useful if you need to check if your value is a real number
import sys # To read user input
import random
import time
from tkinter import *  

def isNumber(toCheck):
    return isinstance(toCheck, numbers.Number)

def isNumber(toCheck):
    return isinstance(toCheck, numbers.Number)

# Inverse Cosine
def factorial(n):
    """Calculate factorial of n manually."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def invCos(x, terms=30):
    # Validate and convert input
    try:
        x = float(x)  # Convert input to float if possible
    except (ValueError, TypeError, NameError):
        return "Input must be a number"
    
    # Check if input is within the valid range for arccosine
    if not -1 <= x <= 1:
        return "Input must be in the range -1 to 1"
    
    # Approximation constants
    pi = 3.141592653589793  # Value of pi
    arcsin_result = 0
    sign = 1  # Alternating sign for each term
    
    # Taylor series approximation for arcsin(x)
    for n in range(terms):
        numerator = factorial(2 * n)  # (2n)!
        denominator = (4**n * (factorial(n)**2) * (2 * n + 1))  # Denominator terms
        term = (numerator / denominator) * (x**(2 * n + 1))
        arcsin_result += term  # Add term to the result
        
   # Calculate arccos(x) using the relationship with arcsin(x)
    arccos_result = (pi / 2) - arcsin_result
        
   # Convert result from radians to degrees manually
    result_degrees = arccos_result * (180 / pi)
    return result_degrees

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

import tkinter as tk
from tkinter import simpledialog, messagebox
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
            print("Thank you for using Eternity TUI. Exiting TUI now")
            break
        else:
            print("Invalid selection, please choose a number between 1 and 6.")
        time.sleep(0.5)




def clear_display():
    display.delete(0, END)

def btn_num(num):
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, num)

def btn_op(operator):
    current_text = display.get()
    if current_text and current_text[-1] in "+-*/":
        display.delete(len(current_text) - 1, tk.END)
    position = len(display.get())
    display.insert(position, operator)

def btn_stdev_mad_log(operator):
    if operator == "MAD":
        display.delete(0, tk.END)
        display.insert(0, "meanAbsDev(") 
    elif operator == "stdDev":
        display.delete(0, tk.END)
        display.insert(0, "stdDev(") 
    elif operator == "log":
        display.delete(0, tk.END)
        display.insert(0, "log(") 
    else:
        position = len(display.get())
        display.insert(position, operator)

def closing_paren():
    current_text = display.get()
    open_paren_count = current_text.count("(")
    close_paren_count = current_text.count(")")
    if open_paren_count > close_paren_count:
        display.insert(tk.END, ")")

def opening_paren():
    current_text = display.get()
    if current_text == "" or current_text[-1] in "+-*/":
        display.insert(tk.END, "(")  # Insert opening parenthesis

def calc_sqrt():
    try:
        expression = display.get()
        if expression != "0":
            result = math.sqrt(float(expression))  
            display.delete(0, END)  
            display.insert(0, str(result)) 
        else:
            messagebox.showerror("Input Error", "input must be greater than 0 and must have a number")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input for square root.")
    except Exception as e:
        messagebox.showerror("Error", "Error")

def calc_arccos():
    try:
        answer = float(display.get())
        answer = invCos(answer)
        display.delete(0, END)
        display.insert(0, str(answer))
    except Exception:
        messagebox.showerror("Error calculating the arccos.")

def btn_exp():
    current_text = display.get()
    if current_text and current_text[-1] in "+-*/^":
        display.delete(len(current_text) - 1, tk.END)
    display.insert(END, "^")  


def calc_equal():
    try:
        expression = display.get()
        if "meanAbsDev" in expression or "stdDev" in expression:
            if expression.count('(') != expression.count(')'):
                messagebox.showerror("Parenthesis Error", "Mismatched parentheses. Ensure you have a closing parenthesis.")
                return
            numbers_str = expression[expression.index('(')+1:expression.index(')')]
            numbers = list(map(float, numbers_str.split(',')))
            if "meanAbsDev" in expression:
                result = meanAbsDev(numbers)
            elif "stdDev" in expression:
                result = stdDev(numbers)
        elif "^" in expression:
            expression = re.sub(r'(\d+(\.\d+)?)\^(\d+(\.\d+)?)', r'exp(\1, \3)', expression) 
            result = eval(expression)
        else:
            result = eval(expression)  # Use eval to evaluate other expressions
        display.delete(0, END)
        display.insert(0, str(result))
    except:
        messagebox.showerror("Value Error", "Error")
        




  



while(True):
    print("\nWould you like to use our calculator as a: \n0. TUI (Textual User Interface)\n1. GUI (Graphical User Interface)\n2. To Exit the program")
    user_input = (input("Please enter 0 or 1: ")).strip()
    if (user_input == "0"):
        TUI_calculator()
        break
    elif (user_input == "1"):
        root = tk.Tk()
        root.geometry("1000x550")  # Setting the size
        root.title("Eternity")  # Setting the title

        # Create a display for the calculator
        display = tk.Entry(root, font="Verdana 20", fg="Black", bg="White", justify=RIGHT)
        display.pack(expand=TRUE, fill=BOTH)

        buttons = [
            ["7", "8", "9", "+", "-","C", "√"],
            ["4", "5", "6", "*", "(", ")", "MAD"],
            ["1", "2", "3", "/", "", "", "Stdev"],
            ["0", ".", "=", ",", "arccos", "log(x, base)", "x^y"]
        ]


        for row in buttons:
            row_frame = Frame(root, bg="#000000")
            row_frame.pack(expand=True, fill=tk.BOTH)  # expand 

            for button_text in row:
                if button_text.isdigit() or button_text == ".":  # Check if it's a number
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=lambda num=button_text: btn_num(num))
                elif button_text == "C": #Check if its clear button
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=clear_display)
                elif button_text == "MAD":
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=lambda: btn_stdev_mad_log("MAD"))
                elif button_text == "√":
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=calc_sqrt)
                elif button_text =="log(x, base)":
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=lambda: btn_stdev_mad_log("log")) 
                elif button_text == "Stdev":
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=lambda: btn_stdev_mad_log("stdDev"))
                elif button_text in "+-*/": #Check if its simple arithmetic op
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=lambda op=button_text: btn_op(op))
                elif button_text == "arccos":
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=calc_arccos)
                elif button_text == "x^y":
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=btn_exp)   
                elif button_text == "=":
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=calc_equal)   
                elif button_text == ",":
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=lambda op=button_text: btn_op(op))
                elif button_text == ")":
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=closing_paren)
                elif button_text == "(":
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5, command=opening_paren)
                else:
                    btn = Button(row_frame, text=button_text, font="segoe 18", relief="groove", bd=0, fg="White", bg="#333333", width=5)
                btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)  
        root.mainloop()
    elif user_input == "2":
        print("Thank you for using Eternity! Exiting!")
        break

    else:
        print("Invalid input, try again.")

