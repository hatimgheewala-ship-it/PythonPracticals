#check whether the provided value is boolean or not

x = 5
y = 0
z = 8

# Checking boolean values
if x and y and z:
    print("All the values are True")
else:
    print("At least one value is False")

# Checking positive numbers using OR
p = -4
q = 9
r = -2

if p > 0 or q > 0:
    print("At least one number is positive")
else:
    print("No number is positive")

if p > 0 or r > 0:
    print("At least one number is positive")
else:
    print("No number is positive")