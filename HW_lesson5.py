# Task 1
# The Guessing Game
import random
random_number = random.randint(1, 10) # random number from 1 to 10
user_input = int(input("Enter number from 1 to 10:\n")) # input number from user convert str to int
if user_input == random_number :                        # check the user number
        print("YOU WIN!")
else :  print(f"YOU LOSE! THE SECRET NUMBER IS {random_number}\n")


# Task 2
# The birthday greeting program
name = input("Hello, input your name, please: ") #ask user name
while True:
    years_old = input( "How old are you?\n")     # check in loop that a number has been entered
    if years_old.isdigit():
       age = int(years_old)
       break                                     # correct input — exit the loop
    else :
       print(f" Please {name}, give me your correct age, only numbers") # if incorrect print the massage
print(f'Hello {name},  on your next birthday you’ll be {age+1} years\n') # greeting massage


#Task 3
#Words combination
import random
input_word = input("Please input word:\n") # get word from user
for i in range(5) :                        # create a 5-step cycle
    chars = list(input_word)               # convert the word to a list of characters
    random.shuffle(chars)                  # shuffle the characters randomly
    random_word = ''.join(chars)           # merge characters back into a string
    print(random_word)                     # output random word













