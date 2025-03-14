# numbers = [1, 2, 2, 3]
# seen_numbers = {}

# for number in numbers:
#     if number not in seen_numbers:
#         print(f"Before: {seen_numbers}")
#         print(f"Adding {number} to seen_numbers")
#         seen_numbers[number] = "I see you, number!"
#         print(f"After: {seen_numbers}")
#     else:
#         print(f"{number} is already in seen_numbers")

'''	1.	Start with an empty dictionary: my_dict = {}.
	2.	Create a list: my_list = ["apple", "banana", "apple", "cherry"].
	3.	Loop through my_list, and for each item:
	•	If the item isn’t in my_dict, add it with a value of 1.
	•	If the item is already in my_dict, increment its value by 1.
	4.	Print the dictionary at the end.'''
my_dict = {}

# my_list = ["apple", "banana", "apple", "cherry"]
# for fruit in my_list:
#     if fruit not in my_dict:
#         my_dict[fruit] = 1
#     else:
#         my_dict[fruit] += 1
# print(my_dict)
# words = ["apple", "banana", "apple", "cherry", "banana", "banana"]
# occurences = {}
# for fruit in words:
#     if fruit not in occurences:
#         occurences[fruit] = 1
#     else:
#         occurences[fruit] += 1
# print(occurences)
# def greet(name):
#     return f"Hello, {name}!"

# result = greet("Alice")
# print(result)
# result = greet()
# print(result)

# evens = []

# def sum_evens(a_list):
#     for nums in a_list:
#         if nums % 2 == 0:
#             evens.append(nums)
#     total_evens = sum(evens)
#     print(total_evens)

# sum_evens([1, 2, 3, 4, 10])
# x = 10
# def modify_x():
#     # accesses 10 so x = 10 + 5
#     x += 5

# modify_x()
# print(x)
# text = "banana"
# char_counts = {}
# for char in text:
#     if char in char_counts:
#         char_counts[char] += 1
#     else:
#         char_counts[char] = 1 
# print(char_counts) # {'b': 1, 'a': 3, 'n': 2}
# grades = {
#     "Chris": [100, 70],
#     "Angela": [90, 100],
#     "Bruce": [80, 40],
#     "Stacey": [70, 70],
#     }
# # grades["Chris"] = [100, 70]
# # grades["Angela"] = [90, 100]
# # grades["Bruce"] = [80, 40]
# # grades["Stacey"] = [70, 70]

# # for student in grades.keys():
# #     print(student)

# # for quizzes in grades.values():
# #     print(sum(quizzes) / 2)

# for student in grades.keys():
#     scores = grades[student]
# print(grades[student].append(sum(scores) / 2))
# #     grades[student].append(sum(scores) / 2)
# # print(grades)

# my_list = [30, 10, 20]

# # Use .sort()
# my_list.sort()
# print(my_list)  # What will this print? => [10, 20, 30]

# # Use sorted()
# new_list = sorted(my_list)
# print(new_list)  # What will this print? => [10, 20, 30]
# print(my_list)   # What will this print now?=> [30, 20, 10]


# for i in range(1, 4):
#     print(i)
#     for j in range(1, 4):
#         print(i * j, end=' ')

# Create a nested for loop that generates a list of all possible coordinate 
# pairs (x, y) where x and y are integers from 0 to 2, inclusive.
 # What is the output of the following code?
# a_list = []
# for x in range(0, 3):
#     for y in range(0, 3):
#         a_list.append((x,y))

# print(a_list)

# for i in range(3):
#     for j in range(3):
#         if i == j:
#             continue
#         print(i, j)
def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize()
            new_words.append(word)

    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))
