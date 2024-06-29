Functions
check_winnings(columns, lines, bet, values)

Checks the winnings based on the outcome of the slot machine spin.
Iterates through each line to see if the symbols in that line match across all columns.
If all symbols match, it calculates the winnings and appends the winning line to a list.
Returns the total winnings and the list of winning lines.
get_slot_machine_spinner(rows, cols, symbols)

Generates the slot machine columns with randomly selected symbols.
Creates a list of all symbols based on their counts.
For each column, it randomly selects symbols and ensures each symbol is used according to its count.
Returns a list of columns with randomly selected symbols.
print_slot_machine_columns(columns)

Prints the slot machine columns row by row.
Each symbol is separated by a vertical bar (|).
deposit()

Prompts the user to enter an amount to deposit.
Ensures the entered amount is a valid positive number.
Returns the deposited amount.
get_number_of_lines()

Prompts the user to enter the number of lines they want to bet on.
Ensures the entered number is within the valid range (1 to MAX__LINES).
Returns the number of lines.
get_bet()

Prompts the user to enter the bet amount per line.
Ensures the entered amount is within the valid range (MIN_BET to MAX__BET).
Returns the bet amount.
main()

The main function that runs the slot machine game.
Prompts the user to deposit an amount.
Prompts the user to enter the number of lines to bet on.
Prompts the user to enter the bet amount and ensures the total bet does not exceed the balance.
Simulates the slot machine spin by generating random columns.
Prints the slot machine columns.
Checks and prints the winnings and any winning lines.
Execution Flow
Deposit: The user is prompted to enter an amount to deposit into their balance.
Select Lines: The user selects the number of lines to bet on.
Place Bet: The user places a bet on each line.
Spin the Slot Machine: The slot machine generates random symbols for each column.
Check Winnings: The program checks for any winning lines and calculates the winnings.
Display Results: The program displays the symbols, total winnings, and any winning lines.
