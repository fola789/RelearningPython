def binary_search(nums: list[int], target: int) -> int:
    """
    Return index of target in sorted list, or -1 if not found.

    Args:
        nums: A sorted list of integers.
        target: The integer value to search for.

    Returns:
        The index of target if found, otherwise -1.
    """
    # Initialize the search window with left and right pointers
    left, right = 0, len(nums) - 1

    # Continue searching while the window is valid
    while left <= right:
        # Find the middle index of the current window
        mid = (left + right) // 2

        # If the middle element is the target, return its index
        if nums[mid] == target:
            return mid
        # If the middle element is less than target, discard left half
        elif nums[mid] < target:
            left = mid + 1
        # If the middle element is greater than target, discard right half
        else:
            right = mid - 1

    # Target was not found in the list
    return -1

# Example usage
print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3

