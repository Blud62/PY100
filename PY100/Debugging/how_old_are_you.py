# input:  ask the user to input his/her age
# output:  display whether the person is an infant, child, teenager or an adult
# definitions: between 0 and 1(inclusive) - infant
#   between 1(exclusive) and younger than 13 - a child
#   between 13(exclusive) and younger than 20 - teenager
#   20 and up - adult
age = int(input("Hold old are you? "))

if age <= 1:
    print("You are an infant! How are you even on this computer?")
elif age > 1 and age < 13:
    print("You are a child, my child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
else:
    print("You're an adult.")