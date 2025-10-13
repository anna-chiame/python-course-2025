#Task 2
def user_div() :
    try :
        num_a = int( input("Please input number a: "))
        num_b = int (input("Please input number b: "))
        res = (num_a **2) / num_b
        print("Result is: ", res)
    except ValueError : # could not convert string to int
        print("Error! You must input only numbers!")
    except ZeroDivisionError :
        print("Error: Cannot divide by zero!")

user_div()









