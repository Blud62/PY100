def how_soon(fire_number, balance, rate, deposit):
    """Calculates how many years until retirement based on FIRE number."""
    years = 0
    while balance < fire_number:
        balance *= (1 + rate)  # Apply interest
        balance += deposit  # Add yearly contributions
        years += 1
    return years


def how_much(years, balance, rate, deposit):
    """Calculates total savings after a given number of years."""
    for _ in range(years):
        balance *= (1 + rate)  # Apply interest
        balance += deposit  # Add yearly contributions
    return balance


if __name__ == "__main__":
    print("Welcome to the Retirement Calculator!")
    
    choice = input("Would you like to calculate (1) Years until retirement or (2) Future savings amount? Enter 1 or 2: ")
    
    if choice == "1":
        fire_number = float(input("Enter your FIRE number (target savings for retirement): "))
        balance = float(input("Enter your current savings balance: "))
        rate = float(input("Enter your expected annual return rate (as a decimal, e.g., 0.055 for 5.5%): "))
        deposit = float(input("Enter your annual contribution amount: "))
        years = how_soon(fire_number, balance, rate, deposit)
        print(f"You will reach your FIRE goal in approximately {years} years.")
    
    elif choice == "2":
        num_years = int(input("Enter the number of years you plan to save: "))
        balance = float(input("Enter your current savings balance: "))
        rate = float(input("Enter your expected annual return rate (as a decimal, e.g., 0.055 for 5.5%): "))
        deposit = float(input("Enter your annual contribution amount: "))
        final_amount = how_much(num_years, balance, rate, deposit)
        print(f"After {num_years} years, your savings will grow to approximately ${final_amount:,.2f}.")
    
    else:
        print("Invalid input. Please enter 1 or 2.")
