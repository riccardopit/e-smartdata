'''
Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%,
annual capitalization and a 5-year investment period. Round the result to the nearest cent.
Tip: Use compound capitalization of interest.
Print the result to the console as shown below.
Expected result:
The future value of the investment: 1159.27 USD
'''

iv = 1000
r = 0.03
yrs = 5
fv = iv * (1 + r) ** yrs
print(f"The future value of the investment: {fv:.2f} USD")
