# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product 
# of all numbers between 1 and the entered integer, inclusive.
# Please enter an integer greater than 0: 5
num = int(input("Please enter an integer greater than 0: "))
# Enter "s" to compute the sum, or "p" to compute the product.
choice = input('Enter "s" to compute the sum, or "p" to compute the product. ')
choice = choice.lower()
if choice == 's':
    sum = sum(range(1, (num + 1)))
    print(sum)
else:
    result = 1
    for num in range(1, num + 1):
        result = result * num
        print(result)


