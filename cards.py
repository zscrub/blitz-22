import json
from on_field import Field_data
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

                    
        # Who places card is Offense
        # Who places card is Defense

        #special teams plays
        def kick_off(spot, player='Zack/New England'):
            match spot:
                case 0:
                    print("55 yard kick")
                    Field_data.spot_ball(Field_data, 10)
                case 1:
                    print("45 yard kick")
                    Field_data.spot_ball(Field_data, 20)
                case 2:
                    print("35 yard kick")
                    Field_data.spot_ball(Field_data, 30)
                case 3:
                    print("25 yard kick")
                    Field_data.spot_ball(Field_data, 40)
                case 4:
                    print("15 yard kick")
                    Field_data.spot_ball(Field_data, 50)
                case 5:
                    print(f"Recieving Team Touchdown! {player.name} + 6!")
                    # for demonstration purposes:
                    Field_data.touchdown(player)

        def punt_play(yards):
            match yards:
                case 0:
                    print("30 yard punt")
                    Field_data.move_ball(Field_data, 30)
                case 1:
                    print("35 yard punt")
                    Field_data.move_ball(Field_data, 30)
                case 2:
                    print("40 yard punt")
                    Field_data.move_ball(Field_data, 40)
                case 3: 
                    print("45 yard punt")
                    Field_data.move_ball(Field_data, 45)
                case 4:
                    print("50 yard punt")
                    Field_data.move_ball(Field_data, 50)
                case 5:
                    print("Recieving Team Touchdown!")
                    Field_data.touchdown(team_or_player="Zack/New England")


        # function to get Offensive, Defensive, Special teams deck/plays 
        # both 1 parameter as a string "offensive", "defensive", "specialkickoff", "specialpunt"
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
            kickoff_deck = Cards.get_deck("specialkick")
            punt_deck = Cards.get_deck("specialpunt")
            shuffle(offensive_deck)
            shuffle(defensive_deck)
            shuffle(kickoff_deck)
            shuffle(punt_deck)
            return offensive_deck, defensive_deck, kickoff_deck, punt_deck

print(Cards.get_plays("defensive")) # : Returns array of smaller lists, [str, str(function), int]
