print("Welcome to the tip calculator!")

bill = float(input("What is the totatl bill? $"))
tip_perc = float(input("How much tip would you like to give? 10, 12 or 15?? "))
split = float(input("How many people to split the bill? "))

subtotal = (bill + (tip_perc * bill / 100)) / split

print(f"Each person should pay: {subtotal}")
