# def count_sheep(n):
#     result = ""  # Initialize an empty string to store the result
#     for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
#         result += f"{i} sheep..."  # Append each count with " sheep..."
#     return result  # Return the final string

# # Example usage:
# n = 7
# print(count_sheep(n))  # Output: "1 sheep...2 sheep...3 sheep..."

# Given a non-negative integer n, return a string that counts down from n to 1 
# and says "I will succeed!" after each number. For example, if n = 3, 
# the output should be "3: I will succeed! 2: I will succeed! 1: I will succeed!"
# def success(n):
#     result = ""
# n = 4
# for i in range(n,  -1):
#     print(i)

# # n = 3
# # for i in range(1, n + 1):
# #     print(i)

# Create a function that takes an integer as 
# an argument and returns "Even" for even numbers or 
# "Odd" for odd numbers.
def even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    elif number % 2 != 0:
        print ("Odd")
    else:
        print(None)
    
even_or_odd(None)
