import keyword

name = input("What is your name? ")
goal = input("What is your goal? ")
deadline = input("When do you want to achieve it? ")

print("\n----- MY GOAL PLAN -----")
print("Name:", name, end=" | ")
print("Goal:", goal)
print("Deadline:", deadline)

print("\nMy plan:\n")
print("Name:", name)
print("Goal:", goal)
print("Deadline:", deadline)

print("\nPython reserved keywords:")
print(keyword.kwlist)
