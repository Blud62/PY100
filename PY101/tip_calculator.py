# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. 
# The program must compute the tip, then print both the tip and the total 
# amount of the bill. You can ignore input validation and assume that the 
# user will enter valid numbers.
# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00



cost = float(input("Please enter the total cost of your meal: "))
tip_percent = float(input("What percentage would you like to tip? 10, 15, or 20 percent? "))
tip_percent = tip_percent / 100
tip_paid = cost * tip_percent
total_cost = cost + tip_paid
print(f'The tip is {tip_paid:.2f}')
print(f'The total is {total_cost:.2f}')


