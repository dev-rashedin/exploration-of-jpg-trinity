# Python Concession Stand Progam


# dictionary {key:value}

menu = {
  "burger": 3.99,
  "fries": 1.99,
  "shake": 1.99,
  "pizza": 8.99,
  "ice cream": 3.99,
  "coke": 1.99,
  "water": 1.99
}

cart = []

total = 0

print("----- MENU -----")
for key, value in menu.items():
  print(f"{key:10}: ${value:.2f}")

print("---------------")

while True:
  food = input("Select an item(q to quit): ")
  if food.lower() == 'q':
    break
  elif menu.get(food) is not None:
    cart.append(food)

print("------ YOUR CART------")

for food in cart:
  total += menu.get(food)
  print(food, end=" ")

print()
print(f" Your total is: ${total}")