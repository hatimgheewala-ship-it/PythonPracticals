
team1 = int(input("Enter points for Team 1: "))
team2 = int(input("Enter points for Team 2: "))
team3 = int(input("Enter points for Team 3: "))
team4 = int(input("Enter points for Team 4: "))
team5 = int(input("Enter points for Team 5: "))

total = team1 + team2 + team3 + team4 + team5
average = total / 5

print("Total points:", total)
print("Average points:", average)

boxes = total // 10
leftover = total % 10

print("Reward boxes:", boxes)
print("Leftover stars:", leftover)

last_week = int(input("Enter last week's total points: "))

if total > last_week:
    print("Points increased by", total - last_week)
elif total < last_week:
    print("Points decreased by", last_week - total)
else:
    print("Points are the same as last week")

bonus = int(input("Enter bonus points: "))
total += bonus

penalty = int(input("Enter points to deduct: "))
total -= penalty

print("Updated total points:", total)
