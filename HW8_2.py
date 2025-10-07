# 1 Define the function
def make_country (country, capital) :
    # create a dict
    dict = { "country_name" : country, "capital_name" : capital}
    print( f" The capital of {dict ['country_name']} is {dict['capital_name']}")
# 2 Call the function
make_country("Ukraine", " Kyiv")
make_country("The USA", "Wasington DC")


