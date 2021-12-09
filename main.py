# Coumpound intrest 
P = int(input("Enter starting principle please. "))
n = int(input("Enter Compound intrest rate.(daily, monthly, quarterly, half-year, yearly) "))
r = float(input("Enter annual interest amount. (decimal) "))
t = int(input("Enter the amount of years. "))

finalinterest = P * (1 + r/n) **n*t

print("The final amount after", t, "years is", finalinterest)

#made by code with maaz         


