investment_amount = float(input("Enter investment amount: "))
monthly_interest_rate = float(input("Enter the annual interest rate: "))
number_of_years = int(input("Enter the number of years: "))
future_investment_value = investment_amount * (1 + monthly_interest_rate/1200) ** (number_of_years * 12)
print("Accumulated value is", f"${future_investment_value:.2f}")