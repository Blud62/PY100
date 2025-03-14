'''
https://launchschool.com/exercises/9db45ac4?track=python

Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.

Example
print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
'''

# def union(lst1, lst2):
#     lst_union = set(lst1 + lst2)
#     return lst_union 


# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9})

# Python is checking if the return value of the expression on the right is equal to the expression  on the left. N.B. - remember right to left evaluation!

## LS ##
# def copy_non_dups_to(result_set, lst):
#     for value in lst:
#         result_set.add(value) 

# def union(list1, list2):
#     result_set = set()
#     print(result_set)
#     copy_non_dups_to(result_set, list1)
#     print(result_set)
#     copy_non_dups_to(result_set, list2)
#     print(result_set)
#     return result_set

# Solution 2
# def union(list1, list2):
#     return set(list1).union(set(list2))

# def union(lst1, lst2):
#     result = set()
#     for num in lst1:
#         result.add(num)
#     for num in lst2:
#         result.add(num)

#     return result

# def union(lst1, lst2):
    #return set(lst1 + lst2)
    

# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9})


# Look up method that you can use with sets 
# - add
# - remove
# - discard
# - pop
# - clear
# - union
# - intersection
# - difference