
field1 = int(input("Enter yield from field 1 (kg): "))
field2 = int(input("Enter yield from field 2 (kg): "))
field3 = int(input("Enter yield from field 3 (kg): "))
field4 = int(input("Enter yield from field 4 (kg): "))
field5 = int(input("Enter yield from field 5 (kg): "))

total = field1 + field2 + field3 + field4 + field5
average = total / 5

bags = total // 25
leftover = total % 25

print("Total harvest:", total, "kg")
print("Average yield:", average, "kg")
print("Full 25 kg bags:", bags)
print("Leftover grain:", leftover, "kg")

last_year = int(input("Enter last year's harvest (kg): "))

if total > last_year:
    print("Harvest increased by", total - last_year, "kg")
elif total < last_year:
    print("Harvest decreased by", last_year - total, "kg")
else:
    print("Harvest is the same as last year")

bonus = int(input("Enter bonus crop (kg): "))
total = total + bonus

seed = int(input("Enter seed reserve (kg): "))
remaining = total - seed

print("Updated total harvest:", total, "kg")
print("Harvest after seed reserve:", remaining, "kg")
