

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
  temp = round((9 * temp) / 5 + 32, 1)
  unit = "F"
  valid = True
elif unit == "F":
  temp = round((temp - 32) * 5 / 9, 1)
  unit = "C"
  valid = True
else:
  valid = False
  print(f"{unit} is not a valid unit")


if valid:
  print(f'The temperature is {round(temp, 1)} °{unit}')