import random  # import the random module to generate random numbers

# create an empty list to store random numbers
numbers = []

#  generate 10 random numbers and append them to the list
i = 0
while i < 10:
    num = random.randint(1, 100)  # generate a random integer between 1 and 100
    numbers.append(num)            # add the generated number to the list
    i += 1

print("Our random numbers are:\n", numbers)  # print the generated list

# find the greatest number
max_num = numbers[0]  # initialize max_num with the first element of the list
i = 1                 # start checking from the second element

while i < 10:
    if numbers[i] > max_num:  # if current element is greater than max_num
        max_num = numbers[i]  # update max_num
    i += 1                     # increment index to move to the next element

print("The greatest number is:", max_num)


