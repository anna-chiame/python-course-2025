# 2
def merge_sort(ex_list):
    """
    Implementation of merge sort without using slices.
    Returns a new sorted list.
    """

    #  Base case: if the list contains 0 or 1 element, it is already sorted.
    if len(ex_list) <= 1:
        return ex_list

    # Find the middle
    mid = len(ex_list) // 2

    # Create two new lists
    left = []
    right = []

    # Fill in left — elements from indices 0 to mid-1
    for i in range(mid):
        left.append(ex_list[i])

    # Fill in right — elements from indices mid to end
    for i in range(mid, len(ex_list)):
        right.append(ex_list[i])

    # Recursively sort the halves
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Return the result of the merge
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Merges two sorted lists into one
    """
    result = []
    ind_left = 0
    ind_right = 0

    #  As long as both lists contain elements
    while ind_left < len(left) and ind_right < len(right):
        if left[ind_left] <= right[ind_right]:
            result.append(left[ind_left])
            ind_left += 1
        else:
            result.append(right[ind_right])
            ind_right += 1

    # Add the leftovers
    while ind_left < len(left):
        result.append(left[ind_left])
        ind_left += 1

    # Add the remaining right
    while ind_right < len(right):
        result.append(right[ind_right])
        ind_right += 1

    return result


#----------------Example-----------------
numbers = [5, 2, 9, 1, 7, 3]
print(merge_sort(numbers))
