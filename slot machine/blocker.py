import random

MAX__LINES = 3
MAX__BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

Symbol__count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

Symbol__values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spinner(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine_columns(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=" ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Enter amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a valid number")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the lines that you want to bet on (1-{MAX__LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX__LINES:
                break
            else:
                print(f"Enter a valid number of lines between 1 and {MAX__LINES}.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line (${MIN_BET}-${MAX__BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX__BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX__BET}.")
        else:
            print("Enter a valid number")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to place this bet. You have only ${balance}.")
        else:
            break
    print(f"Your balance: ${balance}")
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
    
    # Simulate the slot machine spin
    columns = get_slot_machine_spinner(ROWS, COLS, Symbol__count)
    print_slot_machine_columns(columns)

    winnings, winning_lines = check_winnings(columns, lines, bet, Symbol__values)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines:", *winning_lines)
    else:
        print("You didn't win on any lines.")

# Call the main function to run the program
main()
