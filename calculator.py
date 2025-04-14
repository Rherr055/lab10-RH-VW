import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a+b
def sub(a, b):
    return a - b
def mul(a, b):
    return a*b
def div(a, b):
    assert b != 0, ZeroDivisionError
    return a/b
def logarithm(a, b):
    assert a >0, ValueError
    assert a != 1, ValueError
    assert b > 0, ValueError
    return math.log(b,a)

def exp(a, b):
    return a**b