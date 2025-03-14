'''Florence created a dictionary to link each month name with its number. 
Unfortunately, her parrot kept pressing the Caps Lock and messed with the 
stored data. She then created the cap_values function to create a new dictionary 
with all the month names capitalized. However, after invoking cap_values as shown 
below, she noticed that the original dictionary, as 
well as the month_names object had been fixed. 
How did that happen, and what concept does it demonstrate?'''


MONTHS = {
    1: 'JaNuArY',
    2: 'february',
    3: 'MaRch',
    4: 'ApriL',
    5: 'mAY',
    6: 'jUne',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'oCTOber',
    11: 'november',
    12: 'deCember'
}

month_names = MONTHS.values()

def cap_values(d):
    for key, value in d.items():
        d[key] = value.capitalize()

    return d

capitalized_months = cap_values(MONTHS)
print(list(month_names))

# # Step 1: Create a dictionary
# fruits = {1: "apple", 2: "banana", 3: "cherry"}

# # Step 2: Get a dictionary view object
# fruit_view = fruits.values()  # This is a live view of the dictionary's values

# # Step 3: Print the original dictionary and view
# print("Original dictionary:", fruits)
# print("Dictionary view:", list(fruit_view))  # Convert view to a list for display

# # Step 4: Modify the dictionary
# fruits[2] = "grape"  # Change "banana" to "grape"
# fruits[4] = "mango"  # Add a new key-value pair

# # Step 5: Print again to see the changes reflected in the view
# print("\nUpdated dictionary:", fruits)
# print("Updated dictionary view:", list(fruit_view))  # View reflects changes!