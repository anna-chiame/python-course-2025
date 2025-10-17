'''Task 1
Write a Python program to detect the number of local variables declared in a function.'''

def my_function():
    a = 10
    b = 20
    c = a + b
    message = "Hello"
# with local()
    return print ("Number of local variables: ",len(locals()),
                  "\nDictionary of local variables:", locals())
my_function()

print("\nAnother method with  a special attribute __code__")
# co_nlocals shows number of local variable
num_locals = my_function.__code__.co_nlocals
#co_varnames shows names of all local variables and arguments
local_names = my_function.__code__.co_varnames

print("Names of all local variables: ", local_names)
print("Number of local variables: ", num_locals)

