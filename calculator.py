import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a+b

def sub(a, b):
    return a - b
def mul(a, b):
    return a*b
def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a
    except ZeroDivisionError as e:
        print("Caught Zero Division Error:", str((e)))

def log(a, b):
    try:
        # use math library + raise ValueError a>1 b>0
        if a<0:
            raise ValueError("Invalid arguments")
        if a ==1:
            raise ValueError("Invalid arguments")
        if b<0:
            raise ValueError("Invalid arguments")
        return math.log(b, a)
    except ValueError as f:
        print("Caught ValueError Error:", str((f)))



def exp(a, b):
    return a**b

def square_root(a):
    try:
        if a<0:
            raise ZeroDivisionError
        math.sqrt(a)
    except ZeroDivisionError as e:
        print("Caught Zero Division Error:", str(e))

def hypotenuse(a, b):
    math.hypot(a,b)