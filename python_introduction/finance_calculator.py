mi = int(input("Enter your monthly income: "))
me = int(input("Enter your total monthly expenses: "))
ms = mi-me
print(f"Your monthly savings are $ {ms}")
ps = ms * 12 +(ms*12*0.05)
print(f"Projected savings after one year, with interest, is: {ps}")