# 1
def shaker_sort(sortable_list):
    """
    Bidirectional bubble sort (Shaker Sort).
    This is an improved version of Bubble Sort that moves in both directions.
    """
    list_length = len(sortable_list)

    # indicator at least one exchange has taken place
    # if there were no swaps during the entire pass (up and down), the list is sorted
    was_swapped = True
    # indexes to limit the sorting range, which decreases with each iteration
    start_index = 0
    end_index = list_length - 1

    # Main loop  continues as long as exchanges take place
    while was_swapped:

        # Up: from left to right
        # assume that there will be no exchanges until proven otherwise
        was_swapped = False

        # review the list from the beginning (start_index) to the current end limit (end_index)
        for i in range(start_index, end_index):
            # Compare of neighbouring elements
            if sortable_list[i] > sortable_list[i + 1]:
                # swap: if the left is greater than the right, swap them
                sortable_list[i], sortable_list[i + 1] = sortable_list[i + 1], sortable_list[i]

                # swap took place
                was_swapped = True

        # after passing ‘up’, the largest element goes to the end_index position.
        # reduce the upper limit for the next pass.
        end_index = end_index - 1

        # If no swap in the ‘up’ passage, the list is completely sorted
        if not was_swapped:
            break

        # down: from right to left
        was_swapped = False

        # iterate through the list in reverse order: from (end_index - 1) to (start_index - 1).
        # it is necessary to capture the element at start_index.
        for i in range(end_index, start_index, -1):
            # compare of neighbouring elements
            if sortable_list[i] < sortable_list[i - 1]:
                # swap: if the right one is smaller than the left one, swap them around
                sortable_list[i], sortable_list[i - 1] = sortable_list[i - 1], sortable_list[i]

                # swap took place
                was_swapped = True

        #  аfter passing ‘down’, the smallest element goes to the start_index position.
        #  increase the lower limit for the next pass.
        start_index = start_index + 1

    return sortable_list


#----------------Example-----------------
initial_data = [5, 1, 4, 2, 8, 0, 9, 3]
print(f"Initial list : {initial_data}")
sorted_data = shaker_sort(initial_data)
print(f"Sorted list : {sorted_data}")
