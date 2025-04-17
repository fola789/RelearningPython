def first_unique_char(given_string: str) -> int:
    """
    Return the index of the first non-repeating character in the string.
    If there is no such character, return -1.
    """

    # Step 1: Count how many times each character appears in the string
    char_count: dict[str, int] = {}  # Create an empty dictionary to store character counts

    # Loop through each character in the string
    for character in given_string:
        # If the character is already in the dictionary, increment its count
        if character in char_count:
            char_count[character] += 1
        else:
            # If it's not in the dictionary, add it with a count of 1
            char_count[character] = 1

    # Step 2: Loop through the string again to find the first unique character
    for index, character in enumerate(given_string):
        # Check if this character has a count of exactly 1
        if char_count[character] == 1:
            return index  # This is the first unique character

    # If no character was unique, return -1
    return -1
print(first_unique_char("leetcode"))   # Output: 0  ("l")
print(first_unique_char("loveleetcode"))  # Output: 2  ("v")
print(first_unique_char("aabbcc"))     # Output: -1  (no unique character)