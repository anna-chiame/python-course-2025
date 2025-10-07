# Data
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# a new dictionary for total prices
total_prices = {}

# calculate total price for each product
for item in stock:
    total_prices[item] = stock[item] * prices[item]

# print the result
print(total_prices)

