# def titlize(sentence):
#     words = sentence.split()
#     new_words = []

#     for word in words:
#         if len(word) > 2:
#             word = word.capitalize()
#         new_words.append(word)
           

#     return ' '.join(new_words)

# title = 'hello world of programming'
# print(titlize(title))
# titlize(title)

# Try rewriting this simple add_to_list function without global:
# Hint: The function should take both the current list and the new item as 
# arguments, and return the updated list. 
# Let me know how you do or if you’d like me to walk through it! 😊
# my_list = []

# def add_to_list(a_list, item1, item2):
#     my_list.append(item2)
#     my_list.append(item1)
#     return my_list

# my_list = add_to_list(my_list, "apple", "cherry")
# print(my_list)

data = [1, 2, 3, 4, 5]
removed_item = data.pop()
print(f"Removed item: {removed_item}") # 5
print(f"Remaining list: {data}") # [1, 2, 3, 4]