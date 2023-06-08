import numpy as np 

# loan details
principal = 100000
interest_rate = 0.05
years = 5

# calculate monthly interest rate and number of payments
monthly_interest_rate = interest_rate / 12
num_payments = years * 12

# calculate monthly payment using the formula
monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)

print("Monthly Payment: ", monthly_payment)