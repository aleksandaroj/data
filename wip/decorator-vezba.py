# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:07:54 2021

@author: Aleksandar
"""

def my_decorator(my_function):
    print("USING DECORATOR")
    return my_function

@my_decorator
def some_function():
    print("Some function")
    
some_function()