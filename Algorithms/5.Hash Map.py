"""
Pseudocode:
1. Initialize an empty set called `seen` to track numbers we've encountered.
2. Loop through each number `num` in the list `nums`:
    a. If `num` is already in `seen`, return `num` as the first duplicate.
    b. Otherwise, add `num` to `seen`.
3. If loop completes with no duplicates found, return None.
"""

def first_duplicate(nums: list[int]) -> int | None:
    """
    Return the first duplicate number in the list.
    Args:
        nums: A list of integers.
    Returns:
        The first integer that appears more than once in the list.
        If no duplicates are found, returns None.
    """
    # Create an empty set to keep track of numbers we've already seen
    seen: set[int] = set()

    # Go through each number in the input list
    for num in nums:
        # If the number is already in the set, it means it's a duplicate
        if num in seen:
            return num  # Return the first duplicate found

        # Otherwise, add the number to the set and keep going
        seen.add(num)

    # If no duplicates were found, return None
    return None
# Example usage
print(first_duplicate([3, 1, 4, 3, 2]))  # Output: 3
