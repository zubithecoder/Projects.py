# Creating a Slot Machine Program Using Only Python

import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐'] 

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols)) 
    return results

def print_row(row):
    print("^^^^^^^^^^^^^")
    print(" | ".join(row))  # Improved 
    print("^^^^^^^^^^^^^")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        print("🎉 Jackpot! You won 5x your bet! 🎉")
        return bet * 5 
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        print("😊 Nice! You won 2x your bet! 😊")
        return bet * 2
    else:
        print("😞 No win this time. Try again! 😞")
        return 0
    

def main():
    balance = 100

    print("*******************************")
    print("Welcome to Python Slot Machine!")
    print("Symbols: 🍒  🍉  🍋  🔔  ⭐")
    print("*******************************") 

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("< Please enter a valid number >")
            continue

        bet = int(bet)

        if bet > balance:
            print("< Insufficient balance >")
            continue

        if bet <= 0:
            print("< Bet must be greater than zero >")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row) 

        payout = get_payout(row, bet) 

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("You lost your bet.")

        balance += payout 

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"Thanks for playing! Your final balance is ${balance}. Goodbye!")
            break

        if balance <= 0:
            print("💀 You've run out of money! Game over. 💀")
            break

if __name__ == "__main__":
   main() 

