print("Welcome to Calculator!")

print("Enter your first number: ")
number1 = input()

print("Enter your second number: ")
number2 = input()

print("What operation would you like to perform?\n" 
      "1) addition 2) subtraction 3) multiplication 4) division")

operation = input()

match operation:

    case '1':
        output = int(number1) + int(number2) # result of invoking int and passing in num1
        #and invoking int and passing in number2

    case '2':
        output = int(number1) - int(number2)

    case '3':
        output = int(number1) * int(number2)

    case '4':
        output = int(number1) / int(number2)

print(f'Answer: {output}')



        


