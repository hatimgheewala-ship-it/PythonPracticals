
temperature = int(input("Enter temperature in °C: "))
rain = input("Is it raining? (yes/no): ")
wind = input("Is it windy? (yes/no): ")
puddles = input("Are there puddles? (yes/no): ")

if temperature < 15:
    print("Wear a warm jacket.")
else:
    print("Wear light clothes.")

if rain == "yes":
    print("Carry an umbrella.")
else:
    print("No umbrella needed.")

if wind == "yes":
    print("Wear a windbreaker.")
else:
    print("No windbreaker needed.")

if puddles == "yes":
    print("Wear waterproof shoes.")
else:
    print("Regular shoes are fine.")
