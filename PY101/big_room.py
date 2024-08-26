# Build a program that asks the user to enter the length and width 
# of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# - Input - ask user for length and width of room
# - calculate the area of the room in square feet and  square meters
# - Output - print area of room in square meters and square feet


length = int(input("Please enter the length of your room: "))
width = int(input("Please enter the width of your room: "))
question = (input("If your input was in feet, please type 'F', if your input was in meters, please type 'M': "))
question = question.lower()
if question == 'f':
    square_feet = length * width
    print(f'The area of your room is {square_feet: .2f} square feet.')

if question == 'm':
    square_meters = length * width
    print(f'The area of your room is {square_meters: .2f} square meters.')




