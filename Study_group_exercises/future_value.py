import numpy as np

# Define the initial investment and assumptions
initial_investment = 260000
annual_contribution = 3144
years = 4

# Different return rate scenarios
conservative_rate = 0.05
moderate_rate = 0.07
optimistic_rate = 0.10

# Function to calculate future value with annual contributions
def future_value(initial, contribution, rate, years):
    future_value = initial * (1 + rate) ** years
    for i in range(1, years + 1):
        future_value += contribution * (1 + rate) ** (years - i)
    return future_value

# Calculate future values for each scenario
conservative_value = future_value(initial_investment, annual_contribution, conservative_rate, years)
moderate_value = future_value(initial_investment, annual_contribution, moderate_rate, years)
optimistic_value = future_value(initial_investment, annual_contribution, optimistic_rate, years)

# Print values formatted to 2 decimal places with commas
print()
print(f"Conservative estimate: => ${conservative_value:,.2f}")
print()
print(f"Moderate estimate: => ${moderate_value:,.2f}")
print()
print(f"Optimistic estimate: ==> ${optimistic_value:,.2f}")
print()
