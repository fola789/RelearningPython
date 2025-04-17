"""
Pseudocode:
        1. Set left = 0 and right = n
        2. While left <= right:
            a. Find the middle number between left and right
            b. Square the middle number
            c. If it's equal to n → return it
            d. If it's less than n → move left pointer up (middle + 1)
            e. If it's more than n → move right pointer down (middle - 1)
        3. Return the right pointer (it will point to the largest integer where square ≤ n)

"""
def integer_sqrt(n: int) -> int:
    """
    Return the integer square root of n using binary search.

    For example:
        - integer_sqrt(10) => 3
        - integer_sqrt(25) => 5

    """
    if n < 0:
        raise ValueError("Cannot find square root of negative number")

    left, right = 0, n

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == n:
            return mid
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1

    return right  # right is the floor of sqrt(n)
print(integer_sqrt(10))