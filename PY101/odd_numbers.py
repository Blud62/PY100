# Print all odd numbers from 1 to 99, 
# inclusive, with each number on a separate line.

for odds in range(1, 100, 2):
    print(odds) 

##### Launch Solution #####
for number in range(1, 100):
    if number % 2 == 1:
        print(number)