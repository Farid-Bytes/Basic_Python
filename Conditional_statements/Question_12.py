temp = float(input("Enter temperature in Celsius: "))
if temp <= 0:
    print("Freezing")
elif temp <= 30:
    print("Moderate")
else:
    print("Hot")
