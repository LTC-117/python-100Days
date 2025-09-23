def life_in_weeks(current_age: int):
    weeks_left = int(round((90 - current_age) * 12 * (13 / 3)))
    
    print(f"You have {weeks_left} weeks left.")

age = int(input("Insert your age: "))

life_in_weeks(age)
