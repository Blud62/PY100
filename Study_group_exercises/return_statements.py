# What is a return value?
# Is the final result from executing an expression.

# example
# result = 3 + 4  # the expression 3 + 4 returns a new int object 7 which is assigned to the variable `result``

# What is the return value of a function.
# This is the final value that is returned when a function is invoked and executed .
# The implicit return value of a function is ALWAY `None` unless a `return` statement is used at the end of the function to return an object. Then the returned value will be the explicitly returned object after the invocation and execution of the function


# example 
#1 implicit return value(or object) .

# def add(x, y):
#     num = x + y

# print(add(4, 3))


#2 explict return value(or object) .

# def add(x, y):
#     return x + y

# print(add(4, 3))

# Return Values:
    # If a function returns a object, the object can be assigned to a new variable  (e.g., the returned value of `get_input`is assigned to `user_answer`)
    # if a function returns a object, the object can be passed as an argument to another function. 
    # If a function has a return , if not used, python simply discards it!
    # The implicit return value for a function is always None type if not defined!

#3 assigning the return value(or object) of a function to a variable.
# def add(x, y):
#     return x + y

# num = add(4, 3)
# print(num)


num = 5

def increment_num():
    global num
    num += 5

print('Initial num: ', num) 
num = increment_num() # Returned value of function is None, so num is None
print('num after function call:', num)