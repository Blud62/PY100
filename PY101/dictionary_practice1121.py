words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']


def count_occurrences(fruits_list):
    letter_count = {}  # Create an empty dictionary to letter counts
    for word in words:  # Loop through each word in the list
        if word[0] in letter_count:  # If the word is already in the dictionary
            letter_count.append(word)  # Increment its count
        else:
            word[0] = 1  # Otherwise, add it with a count of 1
    return letter_count  # Return the dictionary of word counts


result = count_occurrences(words)
print(result)  # Output: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

