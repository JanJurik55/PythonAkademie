"""
projekt_2A.py: druhy projekt do Engeto Online Python Akademie
"Tic-tac-toe"

author: Jan Juřík
email: jurik.jan.2222@gmail.com
discord: jackobs1395
"""

rules = """
Tic-tac-toe is played on a three-by-three 
grid by two players, who alternately place
the marks X and O in one of the nine 
spaces in the grid. 
The player who succeeds in placing three 
of their marks in a horizontal, vertical, 
or diagonal row is the winner.
"""


# uvitaci text a pravidla
def welcome():
    separator = '=' * 40
    print(f"{separator}\n{'Welcome to Tic-Tac-Toe': ^40}\n{separator}")
    print(rules)
    
    grid_points = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}

    print("Numbers of positions to place marks:")
    show_grid(grid_points)
    print(separator)

# výpis hracího pole
def show_grid(grid):
    separator = "+---+---+---+"
    print(separator)
    print(f"| {grid[1]} | {grid[2]} | {grid[3]} |")
    print(separator)
    print(f"| {grid[4]} | {grid[5]} | {grid[6]} |")
    print(separator)
    print(f"| {grid[7]} | {grid[8]} | {grid[9]} |")
    print(separator)

# zadávací dialog s kontrolou vlozene hodnoty, vrati cislo policka
def player_move(name):
    turn = True
    while(turn):
        value = input(f"Player {name} | Please enter your move number: ")
        turn = input_control(value)
    return int(value)

# kontrola vstupní hodnoty (číslo, rozsah, obsazenost)
def input_control(value):
    test = True
    if not value.isdigit():
        print("It is not a number")
    elif int(value) not in range(1, 10):
        print("The number is not in range")
    elif grid_game[int(value)] != " ":
        print("Occupied position")
    else: 
        test = False
    return test
         

# nalezení vítězných trojic pro zvolené políčko
def choose_lines(position):
    TO_WIN = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9), 
        (1, 4, 7), (2, 5, 8), (3, 6, 9), 
        (1, 5, 9), (3, 5, 7)
        ]
    rows = []
    for var in TO_WIN:
        if position in var:
            rows.append(var)
    return rows

# ověření zda jsou v trojici stejné znaky 
def test_three_in_line(rows):
    for var in rows:
        if grid_game[var[0]] == grid_game[var[1]] and grid_game[var[1]] == grid_game[var[2]]:
            return True


     
# vlastni hra
def running_game():
    i = 0
    game = True
    player_mark = ("X", "O")
    global grid_game 
    grid_game = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
    while game:
        my_point = player_move(player_mark[i % 2])
        grid_game[my_point] = player_mark[i % 2]
        show_grid(grid_game)
        if test_three_in_line(choose_lines(my_point)):
            print((f"Player {player_mark[i % 2]} won.\n"))
            game = False
        elif (" " not in grid_game.values()):
            print("Draw. \n")
            game = False
        i += 1

# dialog Chces hrat dalsi hru
def next_game():
    next = ""
    while not (next == "y" or next == "n"):   
        next = input("Next game?   [y/n]  ")
        if next == "n":
           return False
        elif next == "y":
           print("\n")
           return True
        

if __name__ == "__main__":

    welcome()
    running_game()
    while next_game():
        running_game() 

 