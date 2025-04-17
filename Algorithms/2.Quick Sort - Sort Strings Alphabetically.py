"""
     Pseudocode:
        1. If the list has 0 or 1 items, return it (base case).
        2. Choose a pivot (usually the first element).
        3. Partition the list into:
            a. All items less than or equal to the pivot
            b. All items greater than the pivot
        4. Recursively quick sort both partitions.
        5. Combine and return: left + pivot + right
"""

def quick_sort(words: list[str]) -> list[str]:
    """
    Sort a list of strings using quick sort.
    """
    if len(words) <= 1:
        return words

    pivot = words[0]
    left = [w for w in words[1:] if w <= pivot]
    right = [w for w in words[1:] if w <= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# Example usage:
print(quick_sort(["banana", "apple", "cherry"]))  # Expected: ['apple', 'banana', 'cherry']