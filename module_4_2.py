from math import *; from datetime import *
a=5
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
locals()
print(sin(30))
print(datetime(2020,10,10))

