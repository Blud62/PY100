# Use a for loop to iterate over the numbers dictionary and 
# return a list containing each number divided by 2 as an 
# integer. The result should be truncated to an integer. 
# Assign the returned list to a variable named half_numbers 
# and print its value using print.
half_numbers = []

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
for values in numbers.values():
    values = values // 2
    half_numbers.append(values)
print(half_numbers)