#determine if we made profit or loss or just nothing we did
cost_price = 100
selling_price = 120

if selling_price > cost_price:
    print("Profit")
elif selling_price < cost_price:
    print("Loss")
else:
    print("No Profit No Loss")