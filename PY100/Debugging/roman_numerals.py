# Prompt the user to enter a number with the range 1-10
# The entry should correspond to a Roman numeral based on supplied
# chart.  If the number is outside the range, display the 
# appropriate error message.
num = int(input("Please enter a number between 1 and 10. "))

match num:
    case 1: print("Your Roman numeral is - I")
    case 2: print("Your Roman numeral is - II")
    case 3: print("Your Roman numeral is - III")
    case 4: print("Your Roman numeral is - IV")
    case 5: print("Your Roman numeral is - V")
    case 6: print("Your Roman numeral is - VI")
    case 7: print("Your Roman numeral is - VII")
    case 8: print("Your Roman numeral is - VIII")
    case 9: print("Your Roman numeral is - IX")
    case 10: print("Your Roman numeral is - X")
    case _: print("Please enter a number between 1 and 10. Thanks!")
