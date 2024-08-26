# Ask the user for the length and width of two rectangles. Calculate the area
# of each rectangle, and tell the user which one has the greatest area, or if the
# areas are the same.

# Input: length and width of two rectangles
#   + ask user for the length and width of rectangle 1
#   + assign variables to length and width of rectangle 1
#   + ask user for the length and width of rectangle 2
#   + assign variables to length and width of rectangle 2
# Algorithm:  
#
#   - calculate area for rectangle 1
#   - calculate area for rectangle 2
#   - compare areas of rectangle 1 and rectangle 2 to determine which has greatest are
#       or if they are equal
#   - tell user which rectangle is greater or if they are equal

area_rect = 0

rec_len_1 = int(input(f'Enter the length for the first rectangle: '))
rec_wid_1 = int(input(f'Enter the width for the first rectangle: '))
rec_len_2 = int(input(f'Enter the length for the first rectangle: '))
rec_wid_2 = int(input(f'Enter the width for the first rectangle: '))

def area_rectangle(l, w):
    area_rect = l * w
    return area_rect

area_rect1 = area_rectangle(rec_len_1, rec_wid_1)
area_rect2 = area_rectangle(rec_len_2, rec_wid_2)

print("The area of rectangle 1:", area_rectangle(rec_len_1, rec_wid_1))
print("The area of rectangle 2:", area_rectangle(rec_len_2, rec_wid_2))

if area_rect1 > area_rect2:
    print(f'The area of rectangle 1 is larger than the area of rectangle 2.')
elif area_rect1 < area_rect2:
    print('The area of rectangle 2 is bigger than the are of rectangle 1.')
else:
    print('The areas of the two rectangles are the same.')


    