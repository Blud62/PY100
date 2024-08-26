# PEDAC process (know for PY 119 !!!)
# P - understand the problem
# E - Examples and Test Cases/Edge cases
# D - Data Structure
# A - algorithm (coding agnostic)
# C - code with Intent
'''
P:
Input: string 
Output: string
create a function that accepts a string as an argument
output should be a new string that eliminates duplicate letters
consecutive duplicate characters:  is the next char. same as the current char?
collapsed into a single char:  keep just one of consecutive duplicate characters
RESTATE SOLUTION:
--  find consecutive duplicate values and remove all but 1 of them, return the remaing
    values as a string
E
Rules:
      - do not remove non-consecutive repeated characters
      - same rules apply regardless of type of character, e.g., digits and letters
      - if the input is an empty string, return an empty string
      - strings must be ordered
D
      - list of char. from input string
      - another list to store the characters for the output string
A
High-level:
      - iterate over the input string, and if it doesn't match the previous char, then keep it

Step-by-step:
      - initialize and empty list, output/return
      - iterate over the input string, current_char is same as last item in ouptut
      - if different, append current_char to output(empty list)
      - convert the output to a string and return it.

'''
# code
# initialize and empty list, output/return
def crunch(my_string):
    output = []
# iterate over the input string, current_char is same as last item in ouptut
    for char in my_string:
        if len(output) == 0:
            output.append(char)
# if different, append current_char to output(empty list)
        elif char != output[-1]:
            output.append(char)
#convert the output to a string and return it.
    return ''.join(output)
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

# greeting = "Blow me!"

# for _ in range(0,3):
#     print(greeting)