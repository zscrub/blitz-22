from random import shuffle
# methods of plays with the defensive play as an argument, e machethod calculates the result based on the input
# array/dictionary of plays for user to call, and to be referenced for hand array

# Offense = Run plays, Draw plays, Pass plays, Play-action plays, Screen
# Defense = Defend run, Defend pass, Fumble, Interception, All out blitz, Zone blitz, Penalty

# field goal method with all odds + dice roll

class Cards:
    class Offense:
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


        # dictionary of Offense cards with methods with id: [str, function, int]
        offensive_cards={
            # 5, 5, 3, 2
            0:  ["10 Yard run", run_play, 10],
            1:  ["15 Yard run", run_play, 15],
            2:  ["20 Yard run", run_play, 20],
            3:  ["25 Yard run", run_play, 25],

            # 8, 5, 2
            4:  ["10 Yard draw", draw_play, 10],
            5:  ["15 Yard draw", draw_play, 15],
            6:  ["20 Yard draw", draw_play, 20],
        
            # 5, 4, 3, 2, 1
            7:  ["10 Yard pass", pass_play, 10],
            8:  ["20 Yard pass", pass_play, 20],
            9:  ["30 Yard pass", pass_play, 30],
            10:  ["40 Yard pass", pass_play, 40],
            11:  ["50 Yard pass", pass_play, 50],
        
            # 10, 3, 2
            12:  ["10 Yard Play-action", play_action, 10],
            13:  ["30 Yard Play-action", play_action, 30],
            14:  ["50 Yard Play-action", play_action, 50],
        }

        offensive_deck = [
                            0, 0, 0, 0, 0, 0,
                            1, 1, 1, 1, 1, 1,
                            2, 2, 2,
                            3, 3,

                            4, 4, 4, 4, 4, 4, 4, 4,
                            5, 5, 5, 5, 5,
                            6, 6,

                            7, 7, 7, 7, 7,
                            8, 8, 8, 8,
                            9, 9, 9,
                            10, 10,
                            11,

                            12, 12, 12, 12, 12, 12, 12, 12,
                            13, 13, 13,
                            14, 14,
                        ]

    class Defense:
        defensive_calls = { 0: "Pass Defense", 
                            1: "Run Defense", 
                            2: "Fumble", 
                            3: "Interception", 
                            4: "All Out Blitz",
                            5: "Zone Blitz",
                            6: "Penalty" }


    offensive_cards=dir(Offense)
    offensive_cards=[x for x in offensive_cards if x[0]!="_"]




    # def populate_deck():
    #     offensive_deck=[]
    #     offensive_cards=dir(Cards.Offense)
    #     offensive_cards=[x for x in offensive_cards if x[0]!="_"]

        # for x in offensive_cards:
        #     for j in range(20):
        #         offensive_deck.append(x)
        # return offensive_deck


# print(Cards.populate_deck())
# print(Cards.Offense.run_play(1, 20))

deck = Cards.Offense.offensive_deck
shuffle(deck)
# print(deck[:5])
n=len(deck)
for i in range(n):
    print(Cards.Offense.offensive_cards[deck[i]][0])
print(n)