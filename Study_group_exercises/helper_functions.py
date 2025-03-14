# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to 
# determine the sum or the product of all numbers between 1 and the entered integer, inclusive.
'''Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.''' 


##########


# step 1 get the user input, and convert it into a function
def get_input():
    number = int(input("Please enter an integer greater than 0: "))
    return number


# # step 2 Get the all values between 1 and the input
def get_all_values(user_input):
    all_values = list(range(1, user_input + 1))
    print('These are all the values between' ,user_input,'and 1 ==', all_values)
    return all_values


# # Step 3 get the sum of the all the values.

def sum_total(lst_of_values):
    sum_of_values = 0
    for value in lst_of_values:
        sum_of_values += value
    return sum_of_values

    print('This is the sum of all the values ', sum_of_values)

# Step 4 get the product of the all the values.
def product_total(lst_of_values):
    product_of_value = 1
    for nums in lst_of_values:
        product_of_value *= nums
    return product_of_value


# 5 getting all the function to choose product or sum.
def operation(nums_in_list, user_input):
    operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')
    if operation == "s":
        result = sum_total(nums_in_list)
        print(f'The sum of the integers between 1 and {user_input} is {result}')
    elif operation == "p":
        result = product_total(nums_in_list)
        print(f'The sum of the integers between 1 and {user_input} is {result}')

# calling all functions
        
def main():
    user_answer = get_input() 
    nums_in_list = get_all_values(user_answer)
    sum_total(nums_in_list)
    product_total(nums_in_list)
    operation(nums_in_list, user_answer)

main()   
    
# Return Values:
    # If a function returns a value, the value can be assigned to a new variable  (e.g., the returned value of `get_input`is assigned to `user_answer`)
    # if a function returns a value, the value can be passed as an argument to another function.
    # If a function has a return value, if not used, python simply discards it!
    # The implicit return value for a function is always None type if not defined!

# def add(num1, num2):
#     print(num1 + num2)

    
# print(add(1, 3)) ## 4

