# 1 Function
def make_operation(operator, *numbers) :
    if operator == '+' :
        # start from 0 - neutral starting element for addition
        result = 0
        for num in numbers :
            result +=num
        print (f" Result of addition = {result}")
        return result
    elif operator == '-' :
        # start from the 1st element in numbers
        result = numbers[0]
        # skip the first number
        for num in numbers[1:] :
        # always subtract positive value
            result -= abs(num)
        print(f"Result of subtraction = {result}")
        return result
    elif operator == '*' :
        # start from 1 -neutral starting element for multiplication
        result = 1
        for num in numbers :
            result *= num
        print (f"Result of multiplication = {result}")
        return result


make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)



