# When the user inputs 10, we expect the program to print 
# The result is 50!, but that's not the output we see. Why not?

# print("Hello! Which number would you like to multiply by 5?")
# number = int(input())

# def multiply_by_five(number):
#    return number * 5
   
# print(f"The result is {multiply_by_five(number)}!")

my_list = ['I', 'L', 'v', ' ', 'a', 'n', 'h', 'S', 'h', 'o', 'l', 'o', 'c', ' ', 'c', 'u', 'L', 'e', 'o', ' ']

new_list = []

# Loop through the first half of the list
for i in range(len(my_list) // 2):
    new_list.append(my_list[i])  # Append from the start
    new_list.append(my_list[-(i + 1)])  # Append from the end

# Since the list length is even, no need to add the middle elements separately.

# Join new_list into a single string
result = ''.join(new_list)
print(result)  # Output: "I Love Launch School"

# Ask user for a number in the range of 1 through 7.  Program
# should dispay corresponding day of the week to number entered by user.
# Days of week are assigned as follows:  1 - Monday, 2 - Tuesday...Sunday, 7
# display day of week for given number user entered

# Ask user for a number between 1 through 7.

# number = int(input("Enter a number between 1 and 7 "))
# # assign each weekday a number e.g, Monday - 1 
# if number == 1:
#     print('Monday')
# elif number == 2:
#     print('Tuesday')
# elif number == 3:
#     print('Wednesday')
# elif number == 4:
#     print('Thursday')
# elif number == 5:
#     print('Friday')
# elif number == 6:
#     print('Saturday')
# elif number == 7:
#     print('Sunday')
# else:
#     print('Please enter a valid number.')

# match number:
#     case 1: 
#         print('Monday') 
#     case 2: 
#         print('Tuesday')
#     case 3: 
#         print('Wednesday')
#     case 4: 
#         print('Thursday') 
#     case 5: 
#         print('Friday')
#     case 6:
#         print('Saturday')
#     case 7:
#         print('Sunday')
#     case _:
#         print("Please enter a valid number.")


