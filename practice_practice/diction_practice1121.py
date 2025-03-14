##  Question 1

#Examine the code below Explain your answer in detail and identify the underlying concept. Why does the code behave the way it does.

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_func():
    my_number = [10, 12, 8, 14, 6, 18, 4, 20, 2]
    for value in my_numbers:
        if value % 2 == 1:
            print(value)

my_func() 

'''The variable my_numbers is assinged to a list.  `my func`is defined  and when it is called we see `my_number` assigned to a list of even numbers.  Then we iterate through m`my_numbers` dividing each value with the modulus operator which results in each odd value being printed. 

# Feedback
# Missing the underlying concept

# Perhaps break the quetion down to ensure you've answered all of the items
# - Examine the code below 
# - Explain your answer in detail and identify the underlying concept. (Explain your answer in detail as it relates to the underlying concept(s))
# - Why does the code behave the way it does.'''

## Question 2
# Could you explain variable scope in your own words. Can you give an eexample to demonstrate this?

'''Local variable scope occurs when a variable is defined within a function and unavailble outside that function.
Global variable scope occurs when a variable is defined outside a function and is available throughout a program.
Example:'''

x = 5

def add_nums():
    y = 3
    print(x, y) # 6
    
add_nums()

'''x is assigned the value of 5 and the function `add_nums` is defined with 2 parameters, `num1`, and `num2`. The variable `x` is assinged the value of 3, and the the print functon outputs the value of adding `x's`.  When the function `add_nums` is called, `8` and`9` are passed to the `add_nums`function.  But because `x = 3` is locally scoped, the output is 6 since `x = 5 ` is not accessible.


Vari'''

## Question 3
# While trying to run this code, Oscar got into a problem. Can you identify the problem?

'''The arguments were passed in the reversed order. '''

# How would you fix this code to correct the problem

'''Swapping the arguments fixes the code.'''


def squared_greet(num, name):
    squared_num = num * num
    print(f"Hello {name}, your number squared is {squared_num}.")


squared_greet("Srdjan", 5)


## Question 4
# What will this code output? What concepts explain the reason for your answer

outer_vars = 'Greetings'

def outer():
    outer_var = 'Hello'
    def inner():
        inner_var = 'World'
        print(outer_vars, inner_var)
        
    inner()

outer()


'''The code outpus "Greetings World" when the `outer()` function is called.  
The variable `outer_vars` is assigned to the string `'Greetings'`.  We define  the 
`'outer()`function and assign the variable `outer_var` to the string `Hello`. Within the 
`inner()` function which assigns `World` to the variable `inner_var` and we pass the variable 
`'outer_vars'` and `'inner_var'` to the print function and output `Greetings World`. 
This example illustrates that the `'outer vars'` is globally scoped and accessible to the 
`inner()` function.'''
