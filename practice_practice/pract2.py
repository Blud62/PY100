# illustrate various methods to print values, key-value pairs, etc.

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

def prompt(message):
    print(f'==> {message}')

prompt("Welcome to:  'Choose Your Method!")
print()

prompt("Enter 1 to access the key-value pairs, 2 to access just keys, or 3 to access the values. \n1) .items() method 2) .keys() method or 3) .values() method")
print()
operation = input()
print()

while operation not in ['1', '2', '3']:
    prompt('You must choose 1, 2, or 3')
    operation = input()

match operation:
    case '1':
        output = print("""Fantastic!  The .items() method gives you everything:  
keys and values. (Note:  I added the colon ;)""")
        print()
        for key, value in car.items():

            print(key, ':', value)
    case '2':
        output = print("Cool! With the .keys() method, you're accessing the keys!")
        print()
        for key in car.keys():
            print(key)
    case '3':
        output = print("With the .values() method, you've chosen to access the values!")
        print() 
        for value in car.values():
            print(value)
