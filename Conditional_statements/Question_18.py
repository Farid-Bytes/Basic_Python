score = float(input("Enter the score out of 100: "))
if score > 100:
    print("Invalid score!")
elif score >= 40:
    print("Pass")
else:
    print("Fail")
