# using index method, the first occurence is returned:
# fruit = ['apple', 'banana', 'apple', 'kiwi', 'lychee']
# print("The first apple is at index:", fruit.index('apple'))
# print("The kiwi is at index:", fruit.index('kiwi'))

# # count method:
# print("There are", fruit.count('apple'), "apples in the list.")
# print("There are absolutely", fruit.count('Pear'), "pears in the list.")

# .keys method:
books = {'Emma': 1816, 'Atonement': 2001, 'Frankenstein': 1818, 'Misery': 1987}
# # access keys:
# print(books.keys()) # dict_keys(['Emma', 'Atonement', 'Frankenstein', 'Misery'])
#                     # Above is called a: 'dictionary view object'
# # access values:
# print(books.values())  #  dict_values([1816, 2001, 1818, 1987])  

# # access keys & values (k-v):
# print(books.items()) # dict_items([('Emma', 1816), 
#                      # ('Atonement', 2001), ('Frankenstein', 1818), ('Misery', 1987)])

# What are these 'dictionary view objects?'
books_keys = books.keys()
#print(books_keys) # dict_keys(['Emma', 'Atonement', 'Frankenstein', 'Misery'])
books['Neverwhere'] = 1996
print(books)
print(books.keys())



