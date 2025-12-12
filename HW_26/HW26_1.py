def binary_search_recursive(arr, target, left=0, right=None):
    """
    Perform binary search using recursion.

    Requirements:
    - The input list must be sorted in ascending order.
    - Uses recursion (no loops).

    Args:
        arr: Sorted list of comparable elements.
        target: Value to find.
        left: Left boundary index (inclusive).
        right: Right boundary index (inclusive). If None, set to last index.

    Returns:
        Index of target if found, otherwise -1.
    """
    # Initialize right boundary on the first call
    if right is None:
        right = len(arr) - 1

    # Base case: search range is empty
    if left > right:
        return -1

    # Middle index
    mid = (left + right) // 2

    # Found target
    if arr[mid] == target:
        return mid

    # Recurse into the left half
    if target < arr[mid]:
        return binary_search_recursive(arr, target, left, mid - 1)

    # Recurse into the right half
    return binary_search_recursive(arr, target, mid + 1, right)


# --- Example usage  ---
sorted_numbers = [1, 3, 5, 7, 9, 11, 15]
print(binary_search_recursive(sorted_numbers, 7))   # 3
print(binary_search_recursive(sorted_numbers, 2))   # -1