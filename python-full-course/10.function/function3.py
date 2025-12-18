
def display_invoice(username, amount, due_date):
  print(f"Hello {username}")
  print(f"The amount due on {due_date} is ${amount:.2f}")


display_invoice("Rashedin", 100, "2022-01-01")