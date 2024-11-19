sides = input("Enter three sides of a triangle: ").split()
a = float(sides[0])
b = float(sides[1])
c = float(sides[2])

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Not a Valid Triangle")

