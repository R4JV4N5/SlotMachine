import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_value = {
    "A" :5,
    "B": 4,
    "C": 3,
    "D":2
}
def check_winnings(columns , lines , bet , values):
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line +1)


    return winnings , winning_lines

def get_slot_spin(rows , cols , symbols):
    all_symbols = []
    for symbol , count in symbols.items():
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


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i !=len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row])
        print()




def deposit():
    while True:
        amount = input('what would you like to deposit : $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print("Invalid entry, please enter a number")
    return amount

def no_of_lines():
    while True:
        lines = input(f'enter number of lines to bet on (1-{MAX_LINES})?')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('invalid number of lines')
        else:
            print('please enter a number')
    return lines

def get_bet():
    while True:
        amount = input('Enter bet amount on each lines:')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'please enter amount between ${MIN_BET} and ${MAX_BET}')
        else:
            print('Please enter valid number')
    return amount

def game(balance):
    lines = no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f'Low balance to bet \n current balance: ${balance}')
        else:
            break


    print(f' You are betting ${bet} on {lines} lines \n total bet amount = {bet*lines}')

    slots = get_slot_spin(ROWS , COLS, symbol_value)
    print_slot_machine(slots)
    winnings,winning_lines= check_winnings(slots , lines ,bet, symbol_value)

    print(f" You won {winnings}")
    print("you won on lines:" , *winning_lines)

    return winnings

def main():
    balance = deposit()
    while True:
        print(f'current balance is ${balance}')
        answer = input('press enter to spin (q to quit)')
        if answer == 'q':
            break
        balance += game(balance)
    print(f"you left with ${balance}")
    

main()