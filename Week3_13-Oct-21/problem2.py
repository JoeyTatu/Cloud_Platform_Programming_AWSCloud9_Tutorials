age = int(input("Please enter your age: ")) # int(input...) to convert str to int
height = int(input("Please enter your height (cm): "))

weight = float(((height - 100 + age % 10) * 0.90)) # float not needed, but just to be sure

weight_lbs = round((weight / 0.45359237),2) # round(weightLbs, 2) will round the number to 2 decimal places.
weight_stone = round((weight / 6.35029318),2)
height_feet = round((height / 30.48),2)

result = f'Age: {age} years\nHeight: {height} cm / {height_feet} ft \nRecommended weight: {weight} kg / {weight_lbs} lbs / {weight_stone} st'
print(result)