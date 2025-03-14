x = 10  # Global variable
y = 5
def my_func():
    x = 20  # Local variable
    print(x)  # Accesses local variable x - 20
    print(y)  # Accesses global variable y - 5

    print(x) # prints 20

print(x) # prints 10

my_func()
print(x)  # Accesses global variable x - 10
print(y)  # Acesses global variable y - 5
# print order ==> 10, 20, 5, 20, 10, 5
