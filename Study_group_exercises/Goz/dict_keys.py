'''
https://launchschool.com/books/oo_python/read/object_model#classesdefineobjects

Important things to remember about dictionary.
- Key:Value pairs
- Keys are hasable (bettter to use immutable object)
- Values can be mutable or immutable objects
- Data date type.
'''

#[ART 1 - Acccessing dictionary keys 
my_dict = {
    'dog': 'bark',
    'cat': 'meow',
    'crow': 'caw',
    'lion': 'roar'
}
# Solution 1.
# Using a for loop to get the keys

for key in my_dict:
    print(key)

# Outputs the keys in my_dict

# Solution 2.
# Use the dict.keys() method.

print(my_dict.keys())
print(type(my_dict.keys()))

# Outputs the dictionary keys as dictionary view objects. 

# Solution 3.
# Use the dict.keys() method using a for loop.

for k in my_dict.keys():
    print(k)

# Outputs the keys in my_dict using the `keys` method.

# Solution 4.
# Use the dict.items() method using a for loop.

for keys , _ in my_dict.items():
    print(keys)

# Outputs the keys in my_dict using the `items` method.

# PART 2 - Acccessing dictionary values.

# Solution 1. 
# Using a for loop to get the values
for key in my_dict:
    # value = my_dict[key]
    # print(value)
    print(my_dict[key])

# Solution 2.
# Use a dict.values() to get the values
print(my_dict.values())

# Solution 3.
# Use the dict.values() and a forloop to get the values.
for value in my_dict.values():
    print(value)

# Solution 4.
# Use a dict.items() and a for loop to get the values

for _, value in my_dict.items():
    print(value)

for key in my_dict:
    # value = my_dict.get(key)
    # print(value)
    print(my_dict.get(key))

# # Question given a value, can you find all the keys for a dictionary:

# my_dict_new = { 'type':'sedan', 'color':'blue', 'mileage':8000, 'trim': 'blue'}

# def find_keys(dct,val):
#     found_keys = []
#     for k, v in dct.items():
#         # print(k, ":", v)
#         if v == val:
#             found_keys.append(k)
    
#     # print(found_keys)
#     return found_keys

# val_one = "blue"
# print(find_keys(my_dict_new, val_one))


# Question given a value, can you find all the keys for a dictionary:

my_dict_new = { 'type':'sedan', 'color':['blue', 
'yellow', 'indigo', 'purple', 'red'], 'mileage': '8000',
 'trim': 'blue', 'door spray' : ('white', 'yellow', 'indigo', 'purple', 'red')}

def find_keys(dct,val):
    found_keys = []
    for k, v in dct.items():
        print('Comparing value', v , 'with', val )
        print('This is the type of value', type(v))
        if val == v or val in v:
            found_keys.append(k)
    
    # print(found_keys)
    print('The found keys are', found_keys)
    return found_keys

val_one = "yellow"
print(find_keys(my_dict_new, val_one))