# letters = ['I', 'l', 'v', ' ', 'a', 'n', 'h', 'S', 'h', 'o', 'l', 'o', 'c', ' ', 'c', 'u', 'L',
# 'e', 'o', ' ']
# n = len(letters)
# result = ""
''' 
Front →    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 ]
           [ I, l, v, _  a, n, h, S, h, o, l, o, o, c, _  c, u, L, e, o, _   ]
Back  ←          (starts at index 20, then 19, 18, etc.)
    First iteration picks I (index 0) and space (index 20).
    Second iteration picks l (index 1) and o (index 19).
    Third iteration picks v (index 2) and space (index 18).
'''
# # Loop through the first half of list
# for i in range(n // 2):
#     result = result + letters[i]          # append letter from the front
#     result = result + letters[n - 1 - i] # append letter from the back

# # if n % 2 != 0:
# #     result += letters[n // 2]

# print(result)

# print('Welcome to Calculator!')


# number1 = input("What's the first number? ")
# print()

# number2 = input("What's the second number? ")

# print()
# operation = input('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide\n')
# match operation:

#     case '1': # '1' represents addition
#         return int(number1) + int(number2)
#     case '2':   # '' represents subtraction
#         return  int(number1) - int(number2)
# elif operation == '3':   # '3' represents multiplication
#     output = int(number1) * int(number2)
# elif operation == '4':   # '3' represents division
#     output = int(number1) / int(number2)


# print(f"The result is: {output}")
# nums = [1, 4, 7, 2, 5]
# result = []

# def every_other(lst):
#     for i in range(0,len(nums), 2):
#         #print(i) # --> This are your indicies for list `nums` = (0, 2, 4)
#         result.append(nums[i])
#     print(result)
        
  
        
# every_other(nums)
# # # every_other([1,4,7,2,5]) # => [1,7,5]
# string_a_ding = 'axbxcdxex'


# def third_occurrence(char, string):
#     count = 0  # Initialize a counter to keep track of occurrences
#     for index, current_char in enumerate(string):
#         if current_char == char:  # If the character matches
#             count += 1            # Increment the counter
#             if count == 3:        # Check if this is the 3rd occurrence
#                 return index      # Return the current index
#     return None  # If fewer than 3 occurrences, return None

# ''' Index: 0, Character: a
#             Index: 1, Character: x
#             Index: 2, Character: b
#             Index: 3, Character: x
#             Index: 4, Character: c
#             Index: 5, Character: d
#             Index: 6, Character: x
#             Index: 7, Character: e
#             Index: 8, Character: x
# '''
# print(third_occurrence('x', 'axbxcdxex'))  # Output: 6
# print(third_occurrence('a', 'banana'))     # Output: None (there's no 3rd occurrence of 'a')
def merge(list1, list2):
    merged_list = []  # Initialize an empty list for the result
    length = len(list1)  # We assume both lists are the same length

    for i in range(length):
        merged_list.append(list1[i])    # Add element from list1 at the even index
        merged_list.append(list2[i])    # Add element from list2 at the odd index

    return merged_list
print(merge([1, 2, 3], [4, 5, 6]))  # Output: [1, 4, 2, 5, 3, 6]






