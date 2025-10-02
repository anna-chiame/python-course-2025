# Task 1 String manipulation
def pairs_of_letters (text: str) : # name of function, set the variable and variable type
    if len(text) >= 2 :            # check text by number of letters if > 2
        first_pairs = text[:2]
        last_pairs = text[-2:]
        result = first_pairs + last_pairs
        print("Result:", result, sep=" ", end="\n")
    else :                         # if letters <2 in word
        print(" ")

pairs_of_letters("Helloworld")     # Result: held
pairs_of_letters("my")             # Result: mymy
pairs_of_letters("x")              # Result: nothing


 # Task 2 The valid phone number program.
def check_number (number: str) :  # name of function, set the variable and variable type
    if number.isdigit() :         # check if variable contains only digits
        if len(number) == 10 :    # check len of variable
            print(f"Number {number} is correct !")
        else :
            print (f"Too short! Number {number} must to include 10 digits!")
    else :
        print ("Number must to include only digits!")

number = input("Input your phone number: \n") # ask to enter user phone number
check_number(number)                          # call the function to check the entered number



# Task 3 The math quiz program
import random                           # Import the random module to generate random numbers and select random elements
number_1 = random.randint(1, 10)  # Generate the first random number from 1 to 10
number_2 = random.randint (1, 10) # Generate the second random number from 1 to 10
operation = ["+", "-", "*"]             # List of available arithmetic operations
sing = random.choice (operation)        # Select a random operation from the operation list
example = f"{number_1}{sing}{number_2}" # Forming a mathematical example as a string
result = eval(example)                  # Use eval() to calculate the value of the math expression
user_input = input (f" Calculate the example {example}\n") #Ask the user for the answer
user_answer = int(user_input)           # Convert the user's answer from string to integer
    if user_answer == result :              # Compare the user's answer with the correct result
        print (f"Correct!!! The answer is {result}") # If correct, print success message
    else :
        print(f"Wrong, the answer is {result}")      # If wrong, show the correct answer

# Task 4  The name check
name = "anna"  # name stored in lower case
user_input = input("Please, input your name\n")  # ask name from user
    if user_input.lower() == name:  # Compare the user's answer with the stored name
        print("Yes! Name is correct!")  # if correct
    else:
        print("Input the correct name!")  # if wrong















