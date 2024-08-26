# What errors does it raise for the given 
# examples and what exactly do the error messages mean?

def find_first_nonzero_among(numbers): # should accept list as argument
    for n in numbers:
        if n != 0:
            return n
        

print(find_first_nonzero_among([0, 0, 1, 0, 2, 0])) # ints changed to list
print(find_first_nonzero_among([1])) # int changed to list