# write a function that takes a string as input
# string returns new string with all vowels removed
# - define a function that takes a string as a parameter
# - use .find() method to find vowels
# - assign a new string to the string with vowels removed
'''	1.	We define vowels as a string containing all vowels.
	2.	We create an empty new_string to store the result.
	3.	We iterate through each character in input_string.
	4.	We use .find() to check if the character is in vowels.
	•	If .find() doesn’t return -1, that means the character is a vowel, so we skip it.
	•	Otherwise, we add the character to new_string.
	5.	Finally, return new_string without vowels.'''

'''DEFINE function remove_vowels(input_string)
    SET vowels to "aeiouAEIOU"
    SET new_string to an empty string
    
    FOR each character in input_string
        IF character is found in vowels using .find()
            SKIP adding the character to new_string
        ELSE
            ADD character to new_string
    
    RETURN new_string'''
# rando_string = input('Plese enter a string: ')


# def vowel_chopper(rando_string):
#     vowels = 'AEIOUaeiou'
#     new_string = ''
#     for char in rando_string:
#         if char not in vowels:
#             new_string += char
#     return new_string
    
# print(vowel_chopper(rando_string))

# word = "railroad"
# vowels = "aeiou"
# vowel_count = 0  # Initialize a counter
# vowels_found = ''


# for char in word:
#     if char in vowels:
#         vowels_found = vowels_found + char  # add each vowel found

# print(vowels_found)  # Output all the vowels





# counter = 10

# while counter >= 0:
#     print(counter)
#     counter -= 1
# print('Blast Off!')

# for counter in range(10, 0, -1):
#     print(counter)
# print ('Blast Off!')

# text = "python"
# print(text[1:4]) # "ytho"
# print(text[-2:]) # "on"
# print(text[::2])  # "pto"

# Example: Remove "GPA" and print "Removed GPA: 3.8".



student = {"name": "Jordan", "grade": 9}

student["age"] = 14
student.update({"city": "Chicago", "country": "USA",
                 "hobby" : "basketball", "GPA": 3.8})
student["grade"] = 10
student.pop("hobby")
removed_gpa = student.pop("GPA")
removed_height = student.pop("height", "no such field")
if "country" in student:
    removed_country = student.pop("country")
else:
    removed_country = "not found"
removed_city = student.pop("city", "not found")
new_key = input("Please enter a key: ")
new_value = input("Please enter a value: ")
if new_value.isdigit():
    new_value = int(new_value)
elif new_value.replace('.', '', 1).isdigit():
    new_value = float(new_value)
student[new_key] = new_value
print(f'Removed city: {removed_city}')
print(f'Removed country: {removed_country}')
print(f'Removed GPA: {removed_gpa}')
print(f'Removed height: {removed_height}')
print(f'Updated dictionary: {student}')

