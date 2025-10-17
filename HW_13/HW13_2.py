'''Task 2
Write a Python program to access a function inside a function
(Tips: use function, which returns another function)'''

# ex_1
def my_func_1():
    x = 5
    def inner_func():
        y = 10
        return x + y
    return inner_func()
print("1. The result is: ", my_func_1())

# ex_2
def my_func_2():
    x = 5
    def inner():
        print(f"2. Data from my func_2 is:  ", x)
    return inner

func = my_func_2()
func()

# ex_3 closure
def my_func_3(name):
    def greet():
        return f"Hello, {name}!"
    return greet

anna_hi = my_func_3("Anna")
oleg_hi = my_func_3("Oleh")

print(anna_hi())
print(oleg_hi())

# ex_4 closure
def make_tax_calculator(rate):
    def calculate_tax(amount):
        return amount * rate
    return calculate_tax

vat_20 = make_tax_calculator(0.2)
vat_10 = make_tax_calculator(0.1)

print(vat_20(1000))
print(vat_10(1000))


