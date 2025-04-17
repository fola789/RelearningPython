def longest_unique_substring(Given_String: str) -> int:
    """
    Return the length of the longest substring without repeating characters,
    using the sliding window technique.

    A "sliding window" means we track a section of the string using two pointers
    (left and right), expanding and shrinking the section to maintain a valid window.

    We use a set to track the characters we've seen in the current window.
    """

    seen = set()          # This will store the unique characters in the current window
    left = 0              # This is the start index of the window
    max_length = 0        # This keeps track of the longest valid window seen so far

    # Move the right pointer from the beginning to the end of the string
    # Give me all the index positions of the string from 0 up to (but not including) the string’s length
    for right in range(len(Given_String)):
        # If the character at the right pointer is already in the set,
        # it means we have a duplicate in our window.
        while Given_String[right] in seen:
            # Remove the character at the left pointer from the set
            seen.remove(Given_String[left])

            # Move the left pointer one step forward to shrink the window
            left += 1

        # At this point, s[right] is not in the set anymore, so we can safely add it
        seen.add(Given_String[right])

        # Update the maximum length if the current window is longer than before
        # right - left + 1 is the current window size
        max_length = max(max_length, right - left + 1)

    # After the loop, return the length of the longest valid window
    return max_length

# Example usage:
print(longest_unique_substring("abcabcbb"))  # Output: 3  ("abc")
print(longest_unique_substring("bbbbb"))     # Output: 1  ("b")
print(longest_unique_substring("pwwkew"))    # Output: 3  ("wke")
print(longest_unique_substring(""))          # Output: 0