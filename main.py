import keyboard
from cards import Cards
from time import sleep
from players import Player

# keyboard module requires root on linux 

# scoreboard
home = 0
away = 0

ball_spot = 0
first_down = ball_spot + 10

# each play, increment a var and compare to cards_per_quarter variable 
# if == 20: increment quarter 
# if quarter == 2 and cards_var == 14: 2 minute warning
# if quarter == 2 and cards_var == 20: new half

quarter = 1
cards_per_quarter = 20

offensive_deck = []
defensive_deck = []

player1 = Player("Zack")
player2 = Player("Bubbles")

# start game
def main():
    while True:
        sleep(0.2)



        # draw offensive card to player1 hand
        if keyboard.is_pressed('j'):
if __name__=="__main__":
    main()
