# x = 5

# def func():
#     x = 3
#     print(x)

# func()
# print(x)

# x = [1, 2, 3]

# def modify():
#     x = [1]
#     x += [4, 5]  # ✅ Modifies `x` in place (no new object created)
#     print(x)

# modify()

# debug the following code:

# def appending(lst):
#     lst.append(4)
#     return lst

# my_list = [1, 2, 3]

# print(appending(my_list)) # None


'''
def appending(lst):
    lst.append(4)
    return my_list
'''
# my_list = [1, 2, 3]
# popped_value = my_list.pop(1)  # Modifies my_list in place and returns the popped value
# print(popped_value)  # Output: 2
# print(my_list)  # Output: [1, 3]

# def find_element(lst, target):
#     for item in lst:
#         if item == target:
#             return item
#     return None  # Explicitly return None if target not found

# print(find_element([1, 2, 3], 7))  

# x = [1, 2, 3]

# def tricky(lst):
#     lst = lst + [4]
#     lst.append(5)
#     print("Inside function:", lst)

# tricky(x)
# print("Outside function:", x)
# x = 10  # Global variable

# def my_function():
#     x = x + 5  # ❌ Python treats `x` as local due to reassignment
#     print(x)  # ❌ UnboundLocalError: local variable 'x' referenced before assignment

# my_function()