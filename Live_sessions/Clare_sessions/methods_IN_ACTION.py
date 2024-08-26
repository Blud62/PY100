# # ye olde .append method (N.B. - can't use add on a list!):
fruit = ['apple', 'banana', 'apple', 'kiwi', 'lychee']
# fruit.append('pear')
# print(fruit)

# # .add method for sets:
# creatures = {'unicorn', 'goblin', 'fairy', 'mogwai'}
# creatures.add('troll')
# print(creatures)

# # to remove from a list use .remove (1st instance only at a time!)
# fruit.remove('apple')
# print(fruit)

# deleting keys from a dict with 'del':
# books = {'Emma': 1816, 'Atonement': 2001, 'Frankenstein': 1818, 'Misery': 1987}
# del(books['Emma'])
# print(books)
fruit.sort()
print(fruit)
fruit.reverse()
print(fruit)