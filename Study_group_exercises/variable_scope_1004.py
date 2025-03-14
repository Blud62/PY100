foo0 = 0
# print(foo0) # Where is this initialized -> on line 1

def bar1():
    foo1 = 1
    # print('This is foo0 from bar1', foo0)  # Where is this initialized -> on line 1
    # print('This is foo1 from bar1', foo1)  # Where is this initialized -> on line 5
    # # print(foo2)  # Where is this initialized -> on line 12 Not acccessible in this scope
    # # print(foo3)  # Where is this initialized -> on line 21 Not acccessible at this scope
    # print('Print scope of bar1 \n')

    def bar2():
        foo2 = 2
        # print('This is foo0 from bar2', foo0) # Where is this initialized -> on line 1
        # print('This is foo1 from bar2', foo1) # Where is this initialized -> on line 5
        # print('This is foo2 from bar2', foo2) # Where is this initialized -> on line 113 
        # print(foo3) # Where is this initialized -> on line 20 Not acccessible at this scope
        # print('Print scope of bar2 \n')

        def bar3():
            foo3 = 3
            print('This is foo0 from bar3', foo0) # Where is this initialized -> on line 1
            print('This is foo1 from bar3', foo1) # Where is this initialized -> on line 5
            print('This is foo2 from bar3', foo2) # Where is this initialized -> on line 12 
            print('This is foo3 from bar3', foo3) # Where is this initialized -> on line 20
            print('Print scope of bar3 \n')

        bar3()

    bar2()

bar1()

'''
- Breifly talk about what you know on variable scope
- What would this code print and why?
'''

# https://launchschool.com/exercise_sets/7f3d1745?track=python

# Oscar
# In Python inner functions can access variables initialized the outter scope but outer functions can not access variables initialized in the inner scope
# 



# In this code we initialize a global variable `foo0` to zero. We then call the print functon on the variable to print '0'. We also define three functions which print a series of variables.  The function `bar1` , when invoked,  assigns the local variable `foo1` and assigns it to the value `1`. The function `def bar1()` also prints `foo0`, which is the value `0`. It also prints foo1 which is the value 1.