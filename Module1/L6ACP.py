swimmer = input("Can the swimmer swim? (yes/no): ").lower()
age = int(input("Enter the swimmer's age: "))
supervision = input("Is an instructor present? (yes/no): ").lower()

if swimmer == "yes" and age >= 12:
    print("Allowed in the deep end.")

elif swimmer == "yes" and age < 12 and supervision == "yes":
    print("Allowed in the shallow pool with an instructor.")

elif swimmer == "no" or not (supervision == "yes"):
    print("Shallow pool only. Adult supervision is required.")

else:
    print("Shallow pool only. Ask a lifeguard for help.")
