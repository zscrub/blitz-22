import json
from random import shuffle
# methods of plays with the defensive play as an argument, e machethod calculates the result based on the input
# array/dictionary of plays for user to call, and to be referenced for hand array

# Offense = Run plays, Draw plays, Pass plays, Play-action plays, Screen
# Defense = Defend run, Defend pass, Fumble, Interception, All out blitz, Zone blitz, Penalty

# field goal method with all odds + dice roll

class Cards:
        # Run plays
        def run_play(defense, yards):
            match defense:
                case 0:
                    print("Full Gain")
                case 1:
                    print("No Gain")
                case 2:
                    print("Turnover")
                case 3:
                    print("2x Gain")
                case 4:
                    print("-10 Yards")
                case 5:
                    print("Full Gain + 10 yards")
                case 6:
                    print("-10 Yards, Replay down")
        def draw_play(defense, yards):
            match defense:
                case 0:
                    print("Full Gain")
                case 1:
                    print("No Gain")
                case 2:
                    print("Defense scores a Touchdown")
                case 3:
                    print("Full Gain")
                case 4:
                    print("No Yards")
                case 5:
                    print("Full Gain + 10 yards")
                case 6:
                    print("-5 Yards, Replay down")

        # Passing plays
        def pass_play(defense, yards):
            match defense:
                case 0:
                    print("No Gain")
                case 1:
                    print("Full Gain")
                case 2:
                    print("2x Gain")
                case 3:
                    print("Turnover")
                case 4:
                    print("Full Gain + 10 yards")
                case 5:
                    print("-10 yards")
                case 6:
                    print("-10 Yards, Lose down")
        def play_action(defense, yards):
            match defense:
                case 0:
                    print("Half Gain")
                case 1:
                    print("Full Gain")
                case 2:
                    print("Turnover")
                case 3:
                    print("Turnover")
                case 4:
                    print("-10 yards")
                case 5:
                    print("-5 yards")
                case 6:
                    print("Full Gain")
        
        # function to get Offensive or Defensive deck/plays, takes 1 parameter as a string "offensive", or "defensive"
        def get_deck(side) -> list:
            with open('decks.json', 'r') as f:
                decks = json.load(f)
                return decks[f"{side}_deck"]

        def get_plays(side) -> list:
            with open('decks.json', 'r') as f:
                decks = json.load(f)
                return decks[f"{side}_plays"]            

        # special teams still needed
        # do {
        #       ...code
        #   }

        # shuffled decks ready for live
        def set_decks() -> list:
            offensive_deck = Cards.get_deck("offensive")
            defensive_deck = Cards.get_deck("defensive")
            shuffle(offensive_deck)
            shuffle(defensive_deck)
            return offensive_deck, defensive_deck

# Cards.get_plays("offensive") : Returns array of smaller lists, [str, str(function), int]