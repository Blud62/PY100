# a = "a"
# b = "b"

# def joiner(string1, string2):
#     string1 += string1
#     string2 += string2
#     # return string1, string2

# joiner(a, b)


# print(a)  # a
# print(b)  # b

# m = [1, 2]
# n = "hi"

# def boss_mode(lst, txt):
#     lst.append(3)  
#     lst = lst + [4]  
#     txt += "!"  
#     return txt  

# new_txt = boss_mode(m, n)

# print(m)  # [1, 2, 3]
# print(n)  # hi
# print(new_txt)  # hi!

# a = "a"
# b = "b"

# def joiner(string1, string2):
#     string1 += string1
#     string2 += string2
#     return string1, string2
    

# print(joiner(a, b))

# # print(a)  # a
# # print(b)  # b

# a = [[1, 2], [3, 4]]
# b = a[:]  # Shallow copy (new outer list, same inner lists)
# b[1].append(99)

# print(a[0])
# print(f' Shallow copy id of a[0]: ', id(a[0]))
# print(b[0])
# print(f' Shallow copy id of b[0]: ', id(b[0]))

# import copy
# a = [[1, 2], [3, 4]]
# b = copy.deepcopy(a)  # Deep copy (new outer list, new inner lists)
# b[1].append(99)

# print(a[0])
# print(f' Deep copy id of a[0]: ', id(a[0]))
# print(b[0])
# print(f' Deep copy id of b[0]: ', id(b[0]))

# ''' Write a function that takes a list of 
# integers and returns a new list with only 
# the even numbers from the original list.'''

# my_list = [1, 2, 3, 4]

# def even_list(lst):
#     new_list = []
#     for num in lst:
#         if num % 2 == 0:
#             new_list.append(num)
#     return new_list

# a = even_list(my_list)

# print(a)
# def mystery_function(a, b):
#     a = 10
#     b.append(5)
   
# x = 5
# y = [1, 2, 3]
# mystery_function(x, y)
# print(x, y) # 5, [1, 2, 3, 5]

# def add_element(my_list):
#     my_list.append([4])

# my_list = [1, 2, 3]
# add_element(my_list)
# print(my_list)        # => [1, 2, 3, [4]]

# def add_element(my_list):
#     print(id(my_list))
#     my_list = my_list + [4]
#     print(id(my_list))

# my_list = [1, 2, 3]
# add_element(my_list)
# print(id(my_list))        # => [1, 2, 3]

# import copy
# orig = [[1,2], 3, 4]
# dupe = copy.deepcopy(orig)

# print(id(orig[0]))
# print(id(dupe[0]))
# print(orig[0] is dupe[0])
# print(id(orig[2]))
# print(id(dupe[2]))
# print(orig[2] is dupe[2])

# everest = "Everest"
# kilimanjaro = "Kilimanjaro"
# fuji = "Fuji"

# mountain_list = [everest, kilimanjaro, fuji]

# for idx in range(len(mountain_list)):
#     mountain_list[idx] += " " + str(len(mountain_list[idx])) 

# print(mountain_list)  # ['Everest 7', 'Kilimanjaro 11', 'Fuji 4']
#
# words = [["hi"], ["bye"], ["ok"]]

# for word in words:
#     word.append("!")  # Modifies the inner lists in place

# print(words)  # [['hi', '!'], ['bye', '!'], ['ok', '!']]


# def modify_list(my_list):
#     my_list.append(4)  # Modifies the original list
#     my_list = [1, 2, 3] # Reassigns the local variable, 
#                         # does not affect the original list outside the function
#     return my_list

# my_list = [1, 2, 3]
# print(modify_list(my_list))
# print(my_list)  # Output: [1, 2, 3, 4]

# def modify_string(my_string):
#   my_string += "d" # Modifies the local variable, does not affect the original string outside the function
#   return my_string

# my_string = "abc"
# print(modify_string(my_string))
# print(my_string)  # Output: abc

# a = ["jeff"]
# print(f"a's original assigment 'Jeff's' id:  ", id(a))
# b = ["phil"]
# print(f"b's original assignement 'Phil's' id: ", id(b))
# print()
# def joiner(name1, name2):
#     # name1 = ["bob"] # RE-ASSIGNMENT:  name1 now points to an NEW list ["bob"]
#     name1 += name1
#     print(f'This is the id for Jeff(name1(a))after AUGMENTED assignment (SAME Jeffs ID) =>', id(name1))
#     print()
#     name2 += name2
#     print(f'This is the id for Phil(name2(b))after AUGMENTED assignment (SAME ID) =>', id(name2))
#     name2 = name2 + name2
#     print()
#     print(f'This is the id for Phil(name2(b)) after reassignment (DIFFERENT ID) =>', id(name2))
#     return name2
# print()


# print(joiner(a, b))
# print(f'Augmented assignment for a: ', id(a))
# print(f'This is the id for Phil(name2(b)): ', id(b))

# #outputs:
# 4347207168
# 4347207168
# 4347408576
# ['jeff']
# 4347207168

# def modify_list(lst):
#     # lst = [1, 2, 3]
#     lst.append(4)
#     return lst
#     print(f"Inside function: {lst}") # [1, 2, 3, 4]

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(f"Outside function: {my_list}") # [1, 2, 3, 4]

# numbers = [1, 2, 3, 4, 5]
# target = 3
# found = False

# for num in numbers:
#     if num == target:
#         found = True
#         break
#     print(f"Checking {num}") # Checking 1, Checking 2

# if found:
#     print(f"Found {target}") # Found 3
# else:
#     print(f"{target} not found")

# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# print(greet("Alice")) # Hello, Alice!
# print(greet("Bob", "Hi")) # Hi, Bob!
# print(greet(greeting="Hey", name="Charlie")) # Hey, Charlie!

def hello(greet1, greet2):
    print('Hello')
    return True

hello('hello', 'goodbye')         # invoking function; ignore return value
print(hello('hello', 'goodbye'))  # using return value in a `print` call