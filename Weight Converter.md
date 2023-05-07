# Python
Python excercises
print("Weight Converter")
print("*"*20)
weight = int(input('Please enter your weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() =="L":
    converted = weight * 0.45
    print(f"You are {converted} kilos.")
else:
    converted = weight // 0.45
    print(f"You are {converted} pounds.")
