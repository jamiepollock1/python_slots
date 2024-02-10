import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(1, lines + 1):  # Adjusted to check lines correctly
        # Assume the line is a winning one until proven otherwise
        is_winning_line = True
        first_symbol = columns[0][line - 1]  # Adjust for zero-based indexing
        for col in columns[1:]:  # Start checking from the second column
            if col[line - 1] != first_symbol:
                is_winning_line = False
                break  # No need to check further if any symbol doesn't match
        
        # If it's a winning line, calculate winnings
        if is_winning_line:
            winnings += values[first_symbol] * bet
            winning_lines.append(line)  # Append the winning line number correctly

    return winnings, winning_lines



def spin_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_spin_results(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print (column[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number") 

    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on? (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number") 

    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number") 

    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
           print(f"You don't have enough money! Your current balance is ${balance}")
        else:
            break
    



    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

    slots = spin_machine(ROWS, COLS, symbol_count)
    print_spin_results(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer  = input("Press enter to play (q to quit) ")
        if answer == "q":
            break
        balance += spin(balance)

    print (f"You left with ${balance}")
  

main()