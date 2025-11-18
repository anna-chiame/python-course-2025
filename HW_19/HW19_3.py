# 3


class SimleForIttteration() :
    """
        A class that supports:
        1. Iteration (for for-in loops) via the __iter__ method.
        2. Indexed access (via square brackets) via the __getitem__ method.
        """
    def __init__(self, data):
        self._item = list(data)

    def __iter__(self):
        """
                Returns an iterator. This is a mandatory method for any iterable object.
                We return an iterator for the built-in list.
                """
        return iter(self._item)

    def __getitem__(self, index):
        """
                Allows to retrieve elements using square bracket syntax.
                Also supports slicing and negative indices.
                """
        return self._item[index]

    def __len__(self):
        """
                Allows the use of the len() function.
                """
        return len (self._item)

# ----------------- EXAMPLES OF USE -----------------

my_data = SimleForIttteration(['Python', 'Java', 'C++', 'Go', 'Rust'])

print(f"Number of elements: {len(my_data)}\n")
print("-"*20)
print("Use for-in loop:")
for languages in my_data :
    print(f"Iterate {languages}")
print("-"*20)
print( f"Element with index 0: {my_data[0]}")
