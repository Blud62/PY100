import numpy as np

# Function to calculate future value with annual contributions
def future_value(initial, contribution, rate, years):
    future_value = initial * (1 + rate) ** years
    for i in range(1, years + 1):
        future_value += contribution * (1 + rate) ** (years - i)
    return future_value

# Function to calculate Required Minimum Distributions (RMDs)
def calculate_rmd(balance, age):
    rmd_table = {
        73: 26.5, 74: 25.5, 75: 24.6, 76: 23.7, 77: 22.9, 
        78: 22.0, 79: 21.1, 80: 20.2, 81: 19.4, 82: 18.5,
        # Add more ages as needed
    }
    if age in rmd_table:
        rmd = balance / rmd_table[age]
        return rmd
    else:
        return 0

# Function to calculate social security benefits based on retirement age
def calculate_social_security(age, monthly_benefit, retirement_age):
    if age >= retirement_age:
        return monthly_benefit * 12
    else:
        return 0

# Function to estimate living expenses in retirement
def estimate_living_expenses(current_expenses, inflation_rate, years):
    return current_expenses * (1 + inflation_rate) ** years

# Function to calculate yearly withdrawals based on different scenarios
def calculate_withdrawal(portfolio, withdrawal_rate, years):
    return portfolio * withdrawal_rate

# Main retirement planning function
def retirement_plan(
    initial_investment, 
    annual_contribution, 
    return_rate, 
    current_age, 
    retirement_age, 
    life_expectancy,
    social_security_monthly,
    current_expenses,
    inflation_rate,
    withdrawal_rate
):
    years_to_retirement = retirement_age - current_age
    years_in_retirement = life_expectancy - retirement_age

    # Step 1: Calculate future value of investments at retirement
    portfolio_at_retirement = future_value(initial_investment, annual_contribution, return_rate, years_to_retirement)
    
    # Step 2: Calculate social security payments
    yearly_social_security = calculate_social_security(retirement_age, social_security_monthly, retirement_age)
    
    # Step 3: Estimate living expenses at retirement (adjusted for inflation)
    expenses_at_retirement = estimate_living_expenses(current_expenses, inflation_rate, years_to_retirement)
    
    # Step 4: Calculate yearly withdrawal (e.g., 4% rule)
    yearly_withdrawal = calculate_withdrawal(portfolio_at_retirement, withdrawal_rate, years_in_retirement)
    
    # Step 5: Calculate RMDs for each year in retirement
    rmds = []
    for age in range(retirement_age, life_expectancy):
        rmd = calculate_rmd(portfolio_at_retirement, age)
        portfolio_at_retirement -= rmd  # Subtract RMD from portfolio
        rmds.append(rmd)
    
    # Print a summary
    print(f"Retirement Plan Summary:")
    print(f"Portfolio at Retirement: ${portfolio_at_retirement:,.2f}")
    print(f"Yearly Social Security Payments: ${yearly_social_security:,.2f}")
    print(f"Estimated Yearly Living Expenses: ${expenses_at_retirement:,.2f}")
    print(f"Yearly Withdrawal (e.g., 4% rule): ${yearly_withdrawal:,.2f}")
    print(f"Required Minimum Distributions (RMDs) by Year: {rmds}")

# Example usage
retirement_plan(
    initial_investment=500000, 
    annual_contribution=8000, 
    return_rate=0.07, 
    current_age=62, 
    retirement_age=70, 
    life_expectancy=90,
    social_security_monthly=2000,
    current_expenses=50000,
    inflation_rate=0.03,
    withdrawal_rate=0.04
)
