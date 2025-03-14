print("Welcome to Largest Number Finder!")

numbers = []

def get_numbers_from_user(num_entries):    
    for i in range(num_entries):
        number = int(input(f"Enter number {i + 1}: "))  
        # 1st number ---> i=0 + 1 for "Enter number 1:"
        numbers.append(number)
    return numbers

# Example usage:
num_entries = 7  # Adjust this to change the number of inputs
numbers = get_numbers_from_user(num_entries)
print("You entered:", numbers)

largest_number = numbers[0]

for number in numbers:
  if number > largest_number:
    largest_number = number

print(f'The largest number is: {largest_number}')