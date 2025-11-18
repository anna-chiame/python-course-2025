#2
def in_range (start, end=None, step=1) :
    """
         Generate a sequence of numbers, imitates the built-in range function,

        :param start: Initial value or final value (if 'end' is not specified).
        :param end: Final value (exclusive).
        :param step: Iteration step (cannot be 0).
        :return: Generator that outputs the numbers in the sequence.
        """
    #  Processing case: in_range(stop)
    if end is None :
        end = start
        start = 0

    #  Processing case: step == 0
    if step == 0 :
        raise ValueError ("in_range() step must not be zero")

    #  Logic for a positive step (upward iteration)
    elif step > 0 :
        current = start
        while current < end :
            yield current
            current += step

    #  Logic for negative step (downward iteration)
    else : # step < 0
        current = start
        while current > end :
            yield current
            current +=step

# ----------------- EXAMPLES OF USE -----------------
print(list(in_range(7)))
print(list(in_range(10, 2, -2)))
print(list(in_range(2, 12, 3)))
print(list(in_range(2, 12, 0)))
