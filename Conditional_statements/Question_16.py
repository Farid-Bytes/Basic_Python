a, b, c = map(float, input("Enter three sides of a triangle: ").split())
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
