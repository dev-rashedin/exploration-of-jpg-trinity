# Python Slot Machine

import random

def spin_row():
  symbols = ["🍒",  "🍉", "🍋", "🔔", "✨"]
  results = []

  return [random.choice(symbols) for _ in range(3)]

def print_row(row):
  print("*************************")
  print(" | ".join(row))

def get_payout(row, bet):
  if row[0] == row[1] == row[2]:
    if row[0] == '🍒':
      return bet * 3
    elif row[0] == '🍉':
      return bet * 4
    elif row[0] == '🍋':
      return bet * 5
    elif row[0] == '🔔':
      return bet * 1
    elif row[0] == '✨':
      return bet * 10
  return 0
  

def main():
  balance = 100
  
  print("*************************")
  print(" Welcome to Python Slots ")
  print("Symbols: 🍒 🍉 🍋 🔔 ✨")
  print("*************************")

  while balance > 0:
    print(f"Current balance: ${balance}")

    bet = input("Place your bet amount: ")

    if not bet.isdigit():
      print("please enter a valid number")
      continue

    bet = int(bet)

    if bet > balance:
      print("Insufficient funds")
      continue

    if bet <= 0:
      print("Bet must be greater than 0")
      continue

    balance -= bet

    row = spin_row()
    print("spinning...\n")
    print_row(row)

    payout = get_payout(row, bet)
     
    if payout > 0:
      print(f"You won ${payout}")
    else:
      print("Sorry you lost this round")
    balance += payout

    play_again = input("Do you want to spin again? (Y/N)").lower()

    if play_again != 'y':
      break

  print(f"Game over! Your final balance is ${balance}")

if __name__ == '__main__':
  main()