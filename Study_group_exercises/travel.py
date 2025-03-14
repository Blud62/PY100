# Write a function that, without using the built-in in operator, 
# checks whether a specific destination is included within destinations. 
# For example: When checking whether 'Barcelona' is contained in 
# destinations, the expected output is True, whereas the expected output for 
# 'Nashville' is False.
# 1 - as for loop
# destinations = ['Prague', 'London', 'Sydney', 'Belfast',
#                 'Rome', 'Aruba', 'Paris', 'Bora Bora',
#                 'Barcelona', 'Rio de Janeiro', 'Marrakesh',
#                 'New York City']

# def contains(city, lst):
#     count = 0
#     while count < len(destinations):
#         if city == destinations[count]:
#             return True
#         count += 1
#     return False

# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False

# def contains(city, lst):
#     for destination in destinations:
#         if destination == city:
#             return True # Immediately exits the function if a match is found
        
#     return False # Only runs after the entire loop finishes without finding the city


# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False

# 2 - as while loop

# 3 - using in operator

# def contains(city, lst):
#     return city in lst

# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False

# find the max number in a list

numbers_list = [3, 5, 1, 8, 2] 
max_num = numbers_list[0]

for number in numbers_list:
    if number > max_num:
        max_num = number
print(max_num)

