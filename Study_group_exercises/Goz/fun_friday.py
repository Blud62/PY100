#Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

#Examples
# def square(num):
#     result = num * num
#     return result

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

'''
Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

Example 1
What is your name? Sue
Hello Sue.


Example:
What is your name? Bob!
HELLO BOB! WHY ARE WE YELLING?
'''
# user_name = input("Hello!  What is your first name? ").strip()
# if user_name[-1] == '!':
#     print(f'HELLO {user_name}! WHY ARE WE YELLING?, user_name.upper()')
# else:
#     print(f'Hello {user_name}.')


# username  =  input("Hello!  What is your first name? ").strip()

# if username.endswith('!'):
#     print(f"HELLO {username.upper()}! WHY ARE WE YELLING?")
# else:
#     print(f"Hello  {username}.")



'''The End Is Near But Not Here
Write a function that returns the next to last word in the string argument.

Words are any sequence of non-blank characters.

You may assume that the input string will always contain at least two words.
'''

# Examples
# These examples should print True

def penultimate(string):
    string = string.split()
    string = string[-2]
    return string

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")