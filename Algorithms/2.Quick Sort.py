
def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    pivot = nums[0] # Choose the first element as the pivot
    # Partition: all elements <= pivot go to the left list
    left = [n for n in nums[1:] if n <= pivot]
    # Partition: all elements > pivot go to the right list
    right = [n for n in nums[1:] if n > pivot]

    # Recursively sort the left and right parts, then combine them with the pivot in the middle
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
print(quick_sort([4, 2, 6, 1, 3]))  # Output: [1, 2, 3, 4, 6]

