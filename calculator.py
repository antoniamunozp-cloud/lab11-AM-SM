#https://github.com/antoniamunozp-cloud/lab11-AM-SM.git
#Partner 1: Antonia Munoz Paez
#Partner 2: Saisha Mahindroo
import math


# First example
def add(a, b):
    return a + b

def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def exp (a,b):
    return math.exp(a)

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    math.hypot(a, b)

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b, a)


