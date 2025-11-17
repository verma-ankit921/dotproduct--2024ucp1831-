a = list(map(int, input("Enter vector A elements: ").split()))
b = list(map(int, input("Enter vector B elements: ").split()))
dot = sum(x*y for x, y in zip(a, b))
print("Dot product:", dot)

