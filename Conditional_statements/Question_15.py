number = float(input("Enter a number: "))
lower, upper = map(float, input("Enter the range (lower upper): ").split())
if lower <= number <= upper:
    print("Number is within the range")
else:
    print("Number is outside the range")
