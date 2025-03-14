# a = ["jeff"]
# b = ["phil"]
# print(id(b))

# def joiner(name1, name2):
#     name1 = ["bob"]
#     name2 += name2
#     print(id(name2))
#     name2 = name2 + name2
#     print(id(name2))

# joiner(a, b)
# print(a)
# print(b)
# print(id(b))


# a = "a"
# b = "b"

# def joiner(string1, string2):
#     string1 += string1
#     string2 += string2
#     return string1, string2


# a,b = joiner(a, b)

# print(a)  # a
# print(b)  # b

s = "hello"

def change_string(my_str):
    my_str += " world"  # Creates a new string, does NOT modify original
    return my_str

s = change_string(s)

print(s)  # Output: "hello" (unchanged!)