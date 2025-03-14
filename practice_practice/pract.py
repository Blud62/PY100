# for num in range(0, 11, 2): # 0, 2, 4, 6, 8, 10
#     print(num)
# for i in range(10, 0, -1):
#     print(i)
# print('Launch!')
# counter = 10
# while counter >= 0:
#     print(counter)
#     counter -= 1
# print('Launch!')

# greeting = 'Aloha!'
# counter = 0

# # for _ in range(3):
# #     print(greeting)
# while counter < 3:
#     print(greeting)
#     counter += 1

# for i in range(1, 101):
#     print(i * 2)
# counter = 1

# while counter <= 100:
#     print(counter * 2)
#     counter += 1
# lst = [1, 3, 7, 15]
# index = 0

# while index < len(lst):
#     print(lst[index])
#     index += 1

# friends = ['Sarah', 'John', 'Hannah', 'Dave']
# i = 0

# for name in friends:
#     print(f'Hello, {name}!')

# while i < len(friends):
#     print(f'Hello, {friends[i]}!')
#     i += 1
# cities = ['Istanbul', 'Los Angeles', 'Tokyo', None, 'Vienna', None, 'London', 'Bejing', None]
# index = 0
# for city in cities:
#     if city is None:
#         continue
#     print(len(city))
# while True:
#     print('and on')
#     break
# fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']
# index = 0
# for fish in fish_list:
#     print(fish)
#     if fish == 'Nemo':
#         break
# while index <= len(fish_list):
#     print(fish_list[index])
#     if fish_list[index] == 'Nemo':
#         break
#     index += 1

# while True:
#     print('Should I stop looping?')
#     answer = input()
#     if answer == 'yes':
#         break
#     print("Incorredt answer. Please answer 'yes' .")
# import random
# random_number = random.randint(0,1)
# if random_number:
#     print("Yes!")
# else:
#     print("No")
# print('Yes!' if random_number else 'No')

# weather = 'sunny'
# if weather == 'sunny':
#     print("It's a beautiful day!")
# elif weather == 'rainy':
#     print('Grab your umberlla')
# else:
#     print("Let's stay inside.")
# weather = 'snowy'

# match weather:
#     case 'rainy':
#         print('Grab you umbrella!')
#     case 'sunny':
#         print("It's a beautiful day in the neighborhood!")
#     case 'windy':
#         print('Might wanna wear a wind breaker.')
#     case 'snowy':
#         print('Wear your boots out there!')
#     case 'windy':
#         print('Maybe wear your hood or hat.')
#     case _:
#         print('''Check out a weather report before you go outside. 
#               Not sure what the weather is like.''')
        
# def multiply(num1, num2):
#     return num1 * num2
# print(multiply(12, 4))
# def bruce_eckel_quote(s):
#     return s
# print(bruce_eckel_quote("Python is executable pseudocode."))

# def cite(author, quote):
#     print(f'{author} said: {quote}')

# cite('Bruce Eckel', 'Python is executable pseudocode.')
# def squared_number(num):
#     return num **2

# print(squared_number(3))
# def multiples_of_three():
#     divisor = 1

#     for dividend in range(3, 31, 3):
#         print(f'{dividend} / {divisor} = 3')
#         divisor += 1

# multiples_of_three()
# def compare_by_length(s1, s2):
#     if len(s1) < len(s2):
#         return -1
#     elif len(s1) > len(s2):
#         return 1
#     else:
#         return 0
# print(compare_by_length('patience', 'perseverance')) # -1
# print(compare_by_length('strength', 'dignity'))      #  1
# print(compare_by_length('humor', 'grace'))           #  0   
# da_string = 'Captain Ruby'
# py_string = da_string.replace('Ruby', 'Python')
# print(py_string)
# py_string = da_string.split() # ['Captain', 'Ruby']
# py_string[1] = 'Python'
# py_string = ' '.join(py_string)
# print(py_string)

# Write a function 'local_greet' that takes locales as input, and returns a greeting.
# The locale lets us greet people from different countries appropriately, even when
# they share a common language, for example:
# print(local_greet('en_US.UTF-8')) # Hey!
# print(local_greet('en_GB.UTF-8')) # Hello!
# print(local_greet('en_AU.UTF-8')) # Howdy!

# def greet(language_code):

#     match language_code:
#         case 'en':
#             return ('Hi')
#         case 'fr':
#             return ('Salut!')
#         case 'pt':
#             return ('Olà!')
#         case 'de':
#             return ('Hallo!')
#         case 'sv':
#             return ('Hej!')
#         case 'af':
#             return ('Haai!')

# def extract_language(locale):
#     return locale.split('_')[0]

# def extract_region(locale):
#     region_code = locale.split('_') # ['en', 'US.UTF-8']
#     return region_code[1][:2]

# print(extract_region('en_US.UTF-8')) # US

# def local_greet(locale):
#     language = extract_language(locale)
#     region = extract_region(locale)

#     match (language, region):
#         case ('en', 'US'):
#             return 'Hey!'
#         case ('en', 'GB'):
#             return 'Hello'
#         case ('en', 'AU'):
#             return 'Howdy!'
#         case _:
#             return greet(language)

#     return greet(language)

# print(local_greet('en_US.UTF-8'))
# print(local_greet('en_GB.UTF-8'))
# print(local_greet('en_AU.UTF-8'))

# Distinguish greetings for English speaking countries like the US, UK, 
# Canada, or Australia in your implementation, and feel free to fall back
# on the language-specific greeting in all other cases, for example:
# Note: 1 square meter == 10.7639 square feet
# width = (float(input("What is the width of your room in meters? ")))
# length = (float(input("What is the length of your room in meters? ")))

# area_room_meters = width * length
# area_room_feet = area_room_meters * 10.7639

# print(f"The area of the room in meters is:  {area_room_meters:.2f}.")
# print(f"The area of the room in feet is:  {area_room_feet:.2f}.")
# '''Create a simple tip calculator. The program should prompt for a bill amount 
# and a tip rate. The program must compute the tip, then print both the tip and 
# the total amount of the bill. You can ignore input validation and assume that 
# the user will enter valid numbers.

# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00'''
# bill_amount = int(input("How much was the total of the bill? "))
# tip_percentage = int(input("What percentage would you like to tip?  "))

# tip_percentage = tip_percentage * (1 / 100)

# tip_amount = tip_percentage * bill_amount
# total = tip_amount + bill_amount

# print(f'The tip is ${tip_amount} ')
# print(f'The total is ${total}')

# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to 
# determine the sum or the product of all numbers between 1 and the entered integer, inclusive.
'''Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.''' 
def compute_sum(num):
    result = sum(range(1, num + 1))
    return result

def compute_product(num):
    result = 1
    for num in range(1, num + 1):
        result *= num
    return result

prompt1 = "Please enter an integer greater than 0: " # prompt - number to be entered
prompt2 = 'Enter "s" to compute the sum, or "p" to compute the product. ' # prompt - operation to execute

number = int(input(prompt1))
operation = input(prompt2)

if operation == "s":
    print(f'The sum of the integers between 1 and {number} is {compute_sum(number)}.')
elif operation == "p":
    print(f'The product of the integers between 1 and {number} is {compute_product(number)}.')








