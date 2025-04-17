def max_sum_window(nums: list[int], k: int) -> int:
    """
    Find the maximum sum of any contiguous subarray (window) of size k.

    Args:
        nums: List of integers.
        k: Size of the sliding window.

    Returns:
        The maximum sum of any window of size k.
    """
    # Calculate the sum of the first window (first k elements)
    current_sum = sum(nums[:k])
    max_sum = current_sum  # Initialize max_sum with the first window's sum

    # Slide the window from index k to the end of the list
    for i in range(k, len(nums)):
        # Slide the window forward by:
        # - Adding the next element (nums[i])
        # - Subtracting the element that just slid out of the window (nums[i - k])
        current_sum += nums[i] - nums[i - k]

        # Update max_sum if we found a larger sum
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example usage
print(max_sum_window([1, 2, 3, 4, 5], 3))  # Output: 12 (3+4+5)
