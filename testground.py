

def func1(num):
    print(num)

def func2(str):
    print(str)

def func3(arr):
    print(arr)

def create_function_with_value(func,*args):
    def new_function(index):
        return func(index,*args)
    return new_function

def helloWorld(str):
    print(str)
    print("hello")

my_functions = [
    lambda: helloWorld(3)
]

my_functions[0]()