
homework = int(input("How many minutes of homework do you have? "))
free_time = int(input("How many minutes of free time do you have? "))

if homework > free_time:
    print("You have more homework than free time.")
    print("Finish your homework first.")
else:
    print("You have enough free time for a balanced day.")

if homework >= 60:
    print("Plan: Divide homework into smaller sessions.")
else:
    print("Plan: Complete your homework in one session.")

if free_time >= 30:
    print("Enjoy at least 30 minutes of fun!")
else:
    print("Keep your free time short today.")

print("Remember to take breaks!")
