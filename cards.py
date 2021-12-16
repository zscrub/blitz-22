# methods of plays with the defensive play as an argument, e machethod calculates the result based on the input
# array/dictionary of plays for user to call, and to be referenced for hand array

# Offense = Run plays, Draw plays, Pass plays, Play-action plays, Screen
# Defense = Defend run, Defend pass, Fumble, Interception, All out blitz, Zone blitz, Penalty
"""
Offensive plays & yardage:
    Run:            10, 15, 20 yards
    Draw:           15, 20 yards
    Pass:           10, 30, 40 yards
    Play-action:    10, 30 yards


"""

# field goal method with all odds + dice roll

class Cards:
    class Offense:
        # Run plays
        def run_play(defense):
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

        def draw_play(defense):
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
        def pass_play(defense):
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

        def play_action(defense):
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

    offensive_cards=dir(Offense)
    

    class Defense:
        defensive_calls = { 0: "Pass Defense", 
                            1: "Run Defense", 
                            2: "Fumble", 
                            3: "Interception", 
                            4: "All Out Blitz",
                            5: "Zone Blitz",
                            6: "Penalty" }
