weather = input("Is it sunny, rainy, or cloudy? ").lower()
homework = input("Have you finished your homework? ").lower()
day = input("Is it a weekday or weekend? ").lower()

if weather == "sunny" and homework == "yes" and day == "weekend":
    print("Best plan: Go outside and enjoy the day!")

elif (weather == "rainy" or weather == "cloudy") and not homework == "yes":
    print("Best plan: Stay inside and finish your homework.")

elif weather == "sunny" and homework == "yes":
    print("Best plan: Enjoy some outdoor activities.")

else:
    print("Best plan: Finish your work and relax at home.")
