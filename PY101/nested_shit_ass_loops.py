# string1 = "HelloWorld"
# string2 = "12345"
# string3 = "Hello World"

# result1 = string1.isalpha()
# result2 = string2.isalpha()
# result3 = string3.isalpha()
 
# print("Is '{}' alphabetic?".format(string1), result1)
# print("Is '{}' alphabetic?".format(string2), result2)
# print("Is '{}' alphabetic?".format(string3), result3)

# Replace the comment in the following code with a while loop

# num_x = int(input('How many times should I print the letter X? '))
# to_print = ''
# count = 0
# while count < num_x:
#     to_print += 'X'
#     count += 1
# print(to_print)

# Initialize largest_odd to None, as we don't know if there will be any odd numbers
# largest_odd = None

# # Loop to get 10 numbers from the user
# for _ in range(10):
#     num = int(input("Enter a number greater than 0: "))
#     if num % 2 != 0:  # Check if the number is odd
#         # If largest_odd is None (no odd found yet) or num is greater than largest_odd
#         if largest_odd is None or num > largest_odd:
#             largest_odd = num  # Update largest_odd to this new, larger odd number

# # After the loop, check if we found any odd numbers
# if largest_odd is not None:
#     print(f"The largest odd number entered is: {largest_odd}")
# else:
#     print("No odd numbers were entered.")

def func_a(x):
    y = x + 1 #6
    result = func_b(y) # go to func_b(z)
    return result * 2

def func_b(z): # z is a placeholder
    return z + 3

print(func_a(5))

    