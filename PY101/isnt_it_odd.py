# Write a function that takes one integer argument and returns 
# True when the number's absolute value is odd, False otherwise.

def is_odd(num):
    if abs(num) % 2 != 0:
        return True
    else:
        return False
    
print(is_odd(-2)) # False
print(is_odd(-3)) # True
print(is_odd(5)) # True
print(is_odd(-5)) # True

####### Launch Solution ######

def is_odd(number):
    return abs(number) % 2 == 1