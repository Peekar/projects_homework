num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

fltNum = num1/num2
intNum =  num1//num2
fltNumRnd = fltNum.__round__()

print(f"Float number: {fltNum} or {fltNumRnd}")
print(f"Integer number: {intNum}")