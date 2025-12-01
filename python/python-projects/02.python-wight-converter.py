# Python Weight Converter

weight = float(input('Enter your weight: '))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == 'K':
    weight = weight * 2.20462
    unit = "Lbs."
    valid = True
elif unit == 'L':
    weight = weight / 2.20462
    unit = "Kgs."
    valid = True
else:
    valid = False
    print(f"{unit} is not a valid unit")


if valid:
    print(f'Your weight is {round(weight, 1)} {unit}')
