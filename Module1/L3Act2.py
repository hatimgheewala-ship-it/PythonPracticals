#program to change the datatype of variable

name="Alkesh"
grade=9
is_studying=True
percentage=99.33


print("Name :", name)
print("Data Type of Name is", type(name))

print("grade :", grade)
print("Data Type of Grade is", type(grade))

print("is_studying :", is_studying)
print("Data Type of is_studying is", type(is_studying))

print("percentage :", percentage)
print("Data Type of percentage is", type(percentage))

# Type casting to convert the datatype of variables
print("\n After Type Casting....")
grade = str(grade)
print(grade)
print("Data Type of age is", type(grade))
percentage = int(percentage)
print(percentage)
print("Data Type of Weight is", type(percentage))