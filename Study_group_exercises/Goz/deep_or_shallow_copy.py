import copy
# main_list = ['Python', 'is', 'better', 'than', 'Ruby' ]

# # Part 1
# lst_1 = main_list # variable as pointer, both variables point to same object
# lst_2 = list(main_list) # list constructor/function creates a shallow copy 
# lst_3 = main_list[ : ] # slicing creates a new list object - N.B. - slicing always creates and returns a new object
# lst_4 = main_list.copy() # main_list.copy creates a shallow - N.B. - copy method called on main_list
# lst_5 = copy.copy(main_list) # copy called from copy library to create a shallow copy
# lst_6 = copy.deepcopy(main_list) # copy.deepcopy from copy library to create a deep copy

# # Part 2
# # print(lst_1) # ['Python', 'is', 'better', 'than', 'Ruby' ] 
# # print(lst_2) # ['Python', 'is', 'better', 'than', 'Ruby' ]
# # print(lst_3) # ['Python', 'is', 'better', 'than', 'Ruby' ]
# # print(lst_4) # ['Python', 'is', 'better', 'than', 'Ruby' ]
# # print(lst_5) # ['Python', 'is', 'better', 'than', 'Ruby' ]
# # print(lst_6) # ['Python', 'is', 'better', 'than', 'Ruby' ]

# # # Part 3 (except for first one - ALL new addresses!)
# # # Although they all have the same outputs, are they the same objects?
# # print(lst_1 is main_list) # True (variable as pointer, both variables point to same object)
# # print(lst_2 is main_list) # False (list constructor/function creates a shallow copy )
# # print(lst_3 is main_list) # False (slicing creates a new list object - N.B. - slicing always creates and returns a new object)
# # print(lst_4 is main_list) # False (main_list.copy creates a shallow - N.B. - copy method called on main_list)
# # print(lst_5 is main_list) # False (copy called from copy library to create a shallow copy)
# # print(lst_6 is main_list) # False (copy.deepcopy from copy library to create a deep copy)

# # Part 4 (INTERNING)
# # What is going on? Are the `Python`(s) related
# # print(lst_1[0] is main_list[0]) # True 
# # print(lst_2[0] is main_list[0]) # True
# # print(lst_3[0] is main_list[0]) # True
# # print(lst_4[0] is main_list[0]) # True
# # print(lst_5[0] is main_list[0]) # True
# # print(lst_6[0] is main_list[0]) # True

# # Part 5 
# # What really going on? Does the function return a new list or not?
# def what_is_going_on(lst):

#     # initialization and assignment.
#     first = lst[0] #'Python'
#     second = lst[1] # 'is'

#     # index reassignment 
#     lst[0] = second # 'is' repalces 'Python' 
#     lst[1] = first # 'Python' repalces 'is'

#     return lst

# what_is_going_on(main_list)

# # Part 6
# # Thats whats going on! A combination of several important python concepts such as List mutability, variable assignment and reassignment, variables as pointers, shallow and deep copies, identity, interning, slicing, method call, function definition and function call, side effects, global and local variables, statement and expression and perhaps, maybe 'Python is better than Ruby after all' 

# print('This is main_list' ,main_list) # ['is','Python', 'better', 'than', 'Ruby' ]
# print('This is lst_1' ,lst_1)  # ['is','Python', 'better', 'than', 'Ruby' ]
# print('This is lst_2' ,lst_2)  # ['Python', 'is', 'better', 'than', 'Ruby' ]
# print('This is lst_3' ,lst_3) # ['Python', 'is', 'better', 'than', 'Ruby' ]
# print('This is lst_4' ,lst_4) # ['Python', 'is', 'better', 'than', 'Ruby' ]
# print('This is lst_5' ,lst_5) # ['Python', 'is', 'better', 'than', 'Ruby' ]
# print('This is lst_6' ,lst_6) # ['Python', 'is', 'better', 'than', 'Ruby' ]