"""
Pseudocode:
    1. Set left pointer to the beginning of the list
    2. Set right pointer to the end of the list
    3. While left < right:
        a. Add the values at left and right
        b. If the sum equals the target → return [left + 1, right + 1]
        c. If the sum is too small → move left pointer to the right
        d. If the sum is too large → move right pointer to the left
"""

def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """
    Return the 1-based indices of two numbers in a sorted list that add up to the target.

    Args:
        nums (list[int]): A list of integers in non-decreasing (sorted) order.
        target (int): The sum to find.

    Returns:
        list[int]: A list containing the 1-based indices of the two numbers that add up to the target.
                   If no solution is found, returns an empty list.
    """

    left = 0                      # Start of the list
    right = len(nums) - 1         # End of the list

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            # Add +1 to each pointer because the problem uses 1-based indexing
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1  # Move the left pointer right to increase the sum
        else:
            right -= 1  # Move the right pointer left to decrease the sum

    return []  # If no solution is found (though the problem may guarantee one)
print(two_sum_sorted([2, 7, 11, 15], 9))
# Output: [1, 2]
