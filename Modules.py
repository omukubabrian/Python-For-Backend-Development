#a module is just a .py file
#python ships many ready-made modules called the standard library:
#example

import math
print(math.sqrt(16))
print(math.pi)

#Three ways to import
import math

from math import sqrt

import math as m

import random

import datetime


#How to create your own module,example
#1.Create a file called helpers.py

def is_even(n):
    return n%2==0

def safe_average(numbers):
    if len(numbers) >0:
        return sum(numbers)/len(numbers)
    return 0

#2.Now create main.py in the same folder
import helpers
print(helpers.is_even(4))
print(helpers.safe_average([5,10,3]))