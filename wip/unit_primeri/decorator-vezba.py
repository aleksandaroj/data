
def my_decorator(my_function):
    print("USING DECORATOR")
    return my_function

@my_decorator
def some_function():
    print("Some function")
    
some_function()
