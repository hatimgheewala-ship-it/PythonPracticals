m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("Average Marks:", average)

if average >= 90 and average <= 100:
    print("Grade: A")
elif average >= 75 and average < 90:
    print("Grade: B")
elif average >= 60 and average < 75:
    print("Grade: C")
elif average >= 50 and average < 60:
    print("Grade: D")
else:
    print("Grade: F")