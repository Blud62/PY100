def calculate_sustainable_salary(current_age, life_expectancy, current_savings, retirement_accounts, social_security, annual_expenses, inflation_rate, investment_return):
    remaining_years = life_expectancy - current_age
    sustainable_salary = 0
    balance = current_savings + retirement_accounts

    # Adjust salary until balance lasts for remaining years
    for salary in range(int(annual_expenses), int(balance // remaining_years), 1000):
        temp_balance = balance
        for year in range(remaining_years):
            # Adjust expenses for inflation
            expenses = annual_expenses * (1 + inflation_rate) ** year
            # Add investment returns
            temp_balance *= (1 + investment_return)
            # Subtract salary and expenses
            temp_balance -= (salary + expenses)
            # Add Social Security (if applicable)
            if current_age + year >= 67:  # Assuming Social Security starts at 67
                temp_balance += social_security
            if temp_balance <= 0:
                break
        if temp_balance > 0:
            sustainable_salary = salary
            break

    return sustainable_salary

# Example inputs
current_age = 62
life_expectancy = 91
current_savings = 10000
retirement_accounts = 629000
social_security = 21600  # Annual Social Security benefits
annual_expenses = 48000
inflation_rate = 0.02
investment_return = 0.05

# Calculate sustainable salary
salary = calculate_sustainable_salary(current_age, life_expectancy, current_savings, retirement_accounts, social_security, annual_expenses, inflation_rate, investment_return)
print(f"Sustainable Salary: ${salary:,.2f} per year")