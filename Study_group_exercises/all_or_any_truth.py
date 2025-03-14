# Exclusive Or

# The or operator returns a truthy value if either or both 
# of its operands are truthy, a falsy value if both operands are falsy. 
# The and operator returns a truthy value if both of its operands are 
# truthy, and a falsy value if either operand is falsy. This works great 
# until you need only one of two conditions to be truthy, the so-called 
# exclusive or, also known as xor (pronounced "ECKS-or").

# In this exercise, you will write an xor function that takes two arguments, 
# and returns True if exactly one of its arguments is truthy, False otherwise.
  

# def xor(x, y):
#     if x == True and y == True:
#         return False 
    
#     if x == False and y == False:
#         return False 

#     return True    

# print(xor(0, 0))
# 5 is Truthy, and 0 is Falsey

# print(xor(5, 0) == True)   # True
# print(xor(False, True) == True) #True
# print(xor(1, 1) == False)    # True
# print(xor(True, True) == False)  # True 


# def xor2(arg1, arg2):
#     if all([arg1, arg2]):   # ALL values must be the same (all True)
#         print('all handles this')
#         return False

######## => returns True if exactly one of its arguments is truthy <= ################

#     elif any([arg1, arg2]):  # ANY value True or False (at least one value is truthy)
#         print('any handled this')
#         return True



# print(xor2(5, 0) == True)   # True
# # print(xor2(False, True) == True) #True
# # print(xor2(1, 1) == False)    # True
# # print(xor2(True, True) == False)  # True 


# print(any([0, 0]))  # False
# print(any([0, 5])) # True
# print(any([5, 0])) # True
# print(any([5, 5])) # True


# print(all([0, 0])) # False
# print(all([0, 5])) # False
# print(all([5, 0])) # False
# print(all([5, 5])) # True



print(any('Hello'))  # True
print(any(''))  # False
print(any(' '))  # True

print(all('Hello'))  # True
print(all(''))  # True  - because ALL False is True
print(all(' '))  # True