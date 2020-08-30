income = int(input())

if income <= 15527:
    percent = int(0)
    calculated_tax = round(income * percent / 100)
elif income <= 42707:
    percent = int(15)
    calculated_tax = round(income * percent / 100)
elif income <= 132406:
    percent = int(25)
    calculated_tax = round(income * percent / 100)
else:
    percent = int(28)
    calculated_tax = round(income * percent / 100)

print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
