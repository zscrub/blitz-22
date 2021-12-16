from random import randint

flip = {0: "Heads", 1: "Tails"}
# returns tuple of True/False if team who called coin toss wins/loses and a string declaring what won the toss
def coin_toss(selection):
    result = randint(0,1)
    if selection == result:
        return True, flip[selection] + " wins the toss!"
    else:
        return False, flip[result] + " wins the toss!"
