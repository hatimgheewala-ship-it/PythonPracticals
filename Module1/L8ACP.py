x = int(input("Enter first value: "))
y = int(input("Enter second value: "))
z = int(input("Enter third value: "))

print("Before Swapping:")
print("x =", x)
print("y =", y)
print("z =", z)

temp = x
x = z
z = y
y = temp

print("After Swapping:")
print("x =", x)
print("y =", y)
print("z =", z)