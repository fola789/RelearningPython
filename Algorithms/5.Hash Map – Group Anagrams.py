"""
    Pseudocode:
        1. Create a dictionary to group words by their sorted version.
        2. For each word in the input list:
            a. Sort its letters → this is the 'anagram signature'
            b. Use the sorted word as the key in the dictionary
            c. Append the original word to the list at that key
        3. Return all the grouped values in the dictionary.
    """
from collections import defaultdict

def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Group words that are anagrams of each other using a hash map.
    Args:
            words (list of str): A list of words that may contain anagrams.

    Returns:
        list of a list of str: Groups of words where each group contains words that are anagrams.
    """
    # Use defaultdict so we don’t need to check if a key exists before appending
    anagram_groups: dict[str, list[str]] = defaultdict(list)

    # Loop over each word in the input list
    for word in words:
        # Sort the letters in the word to get the anagram signatureS
        sorted_word = ''.join(sorted(word))  # "bat" → "abt", "tab" → "abt"

        # Add the word to the corresponding anagram group in the dictionary
        anagram_groups[sorted_word].append(word)

    return list(anagram_groups.values())
print(group_anagrams(["bat", "tab", "tap", "pat", "cat"]))