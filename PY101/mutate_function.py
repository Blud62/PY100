def mutating_delete(lst):
    lst = lst[0:2]
    return lst
        
    

lst = [1, 2, 3]

print(mutating_delete(lst) == [1, 2]) #=> True
print(lst == [1, 2, 3]) #=> True