# 1
def with_index(iterable, start=0):
    """
        Generate pairs (index, element), similar the built-in enumerate function.

        :param iterable: Any iterable object
        :param start: The initial index value (default is 0).
        :return: A generator that returns (index, element).
        """
    index = start            # Initialise the counter with the initial value
    for element in iterable: # Start iterating through the elements of the input object
        yield index, element # Generate a tuple: current index and element
        index += 1           # Increase the index for the next element

# ----------------- EXAMPLE OF USE -----------------

my_data = ['apple', 'banana', 'cherry']
for idx, item in with_index(my_data):
    print(f"Index: {idx}, Element: {item}")

for idx, item in with_index(my_data, start=10):
    print(f"Index: {idx}, Element: {item}")