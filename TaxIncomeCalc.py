income = float(input("Enter the annual income: "))
tax = 0
if (income > 85528):
  surplus = income- 85528 
  surplus = surplus *0.32
  tax = 14839.2 + surplus
elif(income <= 0):
  tax = 0
elif(income <= 85528):
  tax = income * 0.18
  tax = tax -556.2

if (tax < 0 ):
  tax =0 
tax = round(tax, 0)
print("The tax is:", tax, "thalers")