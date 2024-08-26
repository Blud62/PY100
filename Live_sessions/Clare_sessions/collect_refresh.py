
# key-based access for dicts:
books = {'Emma': 1816, 'Atonement': 2001, 'Frankenstein': 1818, 'Misery': 1987}

# access VALUE:
print(books['Emma']) # 1816

# get VALUE:
print(books.get('Emma')) # 1816

# change existing value:
books['Emma'] = 2024 # 'Emma': 2024

# add new k-v pair:
books['Dracula'] = 1897 # 'Dracula': 1897
print(books)

# stuff = ('hello', 'world', 'bye', 'now')
# stuff_list = list(stuff)
#print(stuff_list) # ['hello', 'world', 'bye', 'now']
# get_bye = stuff_list.pop(2)
# good_bye = 'good' + get_bye
# stuff_list.append(good_bye)
# tupe = tuple(stuff_list)
# print(tupe)
# stuff_list = list(stuff[2])

# stuff = list(stuff)
# stuff[2] = 'goodbye'
# stuff = tuple(stuff)
# print(stuff)

# print(stuff == tupe)
# print(tupe)