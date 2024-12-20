import os    
import time    
import random
import time

# Alex Wilson- Add menu for mode selection
mode = input("Enter game mode: '1' for Single Player, '2' for Multiplayer: ")

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
Game = Running    
Mark = 'X'   
TIME_LIMIT = 10

# Alex Wilson - Added more theme colors
themes = {
    1 : {'border': '\033[95m', 'empty': '\033[0m', 'player1': '\033[91m', 'player2': '\033[94m'},
    2 : {'border': '\033[92m', 'empty': '\033[0m', 'player1': '\033[93m', 'player2': '\033[96m'},
    3 : {'border': '\033[94m', 'empty': '\033[0m', 'player1': '\033[92m', 'player2': '\033[91m'},
    4 : {'border': '\033[93m', 'empty': '\033[0m', 'player1': '\033[95m', 'player2': '\033[94m'},
    5 : {'border': '\033[96m', 'empty': '\033[0m', 'player1': '\033[94m', 'player2': '\033[92m'},
    6 : {'border': '\033[90m', 'empty': '\033[0m', 'player1': '\033[91m', 'player2': '\033[93m'}
}  


def CheckPosition(x):    
    if board[x] == ' ':    
        return True    
    else:    
        return False     
        
def DrawBoard(theme):  
    border_color = theme['border']
    empty_color = theme['empty']
    player1_color = theme['player1']
    player2_color = theme['player2']
    
  #added a border to the board game and changed "%c" to "%s" to accept string

    print(border_color + " _________________")
    print("|  _____________  |")
    print("| |  " + empty_color + "%s" % board[1] + border_color + " | " + empty_color + "%s" % board[2] + border_color + " | " + empty_color + "%s" % board[3] + border_color + "  | |")
    print("| | ___|___|___ | |")    
    print("| |  " + empty_color + "%s" % board[4] + border_color + " | " + empty_color + "%s" % board[5] + border_color + " | " + empty_color + "%s" % board[6] + border_color + "  | |")
    print("| | ___|___|___ | |")    
    print("| |  " + empty_color + "%s" % board[7] + border_color + " | " + empty_color + "%s" % board[8] + border_color + " | " + empty_color + "%s" % board[9] + border_color + "  | |")    
    print("| |____|___|____| |") 
    print("|_________________|" + empty_color) 

# Maylee Cianca - Function with winning combinations 
def CheckWin():
    global Game
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], 
        [1, 4, 7], [2, 5, 8], [3, 6, 9], 
        [1, 5, 9], [3, 5, 7]          
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            Game = Win
            return
    if ' ' not in board[1:]:
        Game = Draw
    else:
        Game = Running
   

print("Welcome to Tic-Tac-Toe!")
print("Get ready to enjoy some exciting rounds of Tic-Tac-Toe!")
print("May the best player win! Have fun!")

# Maylee Cianca - Print statment that will show what board we are using
print(" 1 | 2 | 3 \n___|___|___\n 4 | 5 | 6 \n___|___|___\n 7 | 8 | 9 \n")


print("\nRules:\nThis is a two-player game where each player will take turns marking\n an empty square and who evers gets 3 of their mark in a row in\n any direction wins the game!")

# Alex Wilson - Rounds can be unlimited so you can play as many as you want instead of 1 or 3
rounds = int(input("How many rounds do you want to play?" ))
print(f"You have chosen to play {rounds} round(s). Let's begin!")

 
# Instead of having "player 1 and player 2", users are able to name themselves
player_1 = input('Player 1, please enter your name: ').title()  
print('Hi', player_1 + ", you are player 1.\n")
player_2 = input('Player 2, please enter your name: ').title()
print('Hi', player_2 + ", you are player 2.\n")

# Alex Wilson - Added a randomizer for who starts each round
for round_number in range(1, rounds + 1):
    print(f"Round {round_number} of {rounds}!")
    if random.choice([True, False]):
        print(f"{player_1} starts this round!")
        player = 1
    else:
        print(f"{player_2} starts this round!")
        player = 2

# Maylee Cianca - Changed the "X" to an "M", which is the first letter of my name
# Alex Wilson - I changed the "O" to an "A" so that when I playing my opponent I am using the beginning initial to my  name instead of the traditional "O"
player1_mark = input(player_1 + " please input your mark character ")
player2_mark = input(player_2 + " please input your mark character ")
print("Player 1 [" + player1_mark + "] --- Player 2 [" + player2_mark + "]\n")    
print()    
print()    
print("Please Wait...")
time.sleep(3)

print("Select a theme:")
for theme_num, _ in themes.items():
    print(theme_num)
selected_theme = int(input("Enter the theme number: "))

selected_theme = themes.get(selected_theme, themes[1])  

# Maylee Cianca - Added game countdown timer
print("Get ready to play!")
print("The game is starting in:")

for i in range(5, 0, -1):
    print(i)
    time.sleep(1) 

print("Go!") 
time.sleep(1)

# Maylee Cianca - Added time limit to each turn
while(Game == Running):    
    os.system('cls' if os.name == 'nt' else 'clear')
    DrawBoard(selected_theme)
    
    if(player % 2 != 0):
        current_player = player_1
        Mark = player1_mark
    else:
        current_player = player_2
        Mark = player2_mark

    print(f"{current_player}'s turn! You have {TIME_LIMIT} seconds to make your move.")

    start_time = time.time()
    try:
        while True:
            time_taken = time.time() - start_time
            if time_taken > TIME_LIMIT:
                print(f"\nTime's up! {current_player} took too long.")
                time.sleep(2)
                break
            choice = input(f"Enter the position [1-9]: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= 9 and CheckPosition(choice):
                    board[choice] = Mark
                    player += 1
                    CheckWin()
                    break
                else:
                    print("Invalid input. Try again!")
            else:
                print("Please enter a number between 1 and 9.")
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
        exit()
        
os.system('cls')    
DrawBoard(selected_theme)    
if(Game == Draw):    
    print("It's a draw!")
elif(Game == Win):    
    player -= 1    
    if(player % 2 != 0): 
        
        print(player_1, "Has won!")
    else:    
        print(player_2,"Has won!")

# Alex Wilson - Scorebaord that will show how many games players have won between rounds and final score
os.system('cls')
scores = {player_1: 0, player_2: 0}
DrawBoard(selected_theme)
if(Game == Draw):
        print("It's a draw!")
elif(Game == Win):
        player -= 1
        if(player % 2 != 0):
            print(player_1, "Has won!")
            scores[player_1] += 1
        else:
            print(player_2, "Has won!")
            scores[player_2] += 1

    
print(f"Scores after Round {round_number}:")
print(f"{player_1}: {scores[player_1]}, {player_2}: {scores[player_2]}")


print("\nGame Over!")
if scores[player_1] > scores[player_2]:
    print(f"{player_1} wins the game!")
elif scores[player_2] > scores[player_1]:
    print(f"{player_2} wins the game!")
else:
    print("It's a tie!")

# Maylee Cianca - Added ACSII art
def print_smiley_face():
    smiley = """
       _______
     .-       -.
    /           \\
   |    O   O    |
   |     \\_/     |
   |   \\_____/   |
    \\           /
     `-.______.-'
    """
    print(smiley)

print_smiley_face()

