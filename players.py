from cards import Cards

class Player:
    HAND_MAX=5
    hand=[]
    score=0
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.score = 0

    def set_team(self, team: str):
        self.team = team

    def draw_offensive_card(self, offensive_deck):
        # add card from offensive/defensive pile to hand
        if len(self.hand) < Player.HAND_MAX:
            self.hand.append(offensive_deck.pop())

    def draw_defensive_card(self, defensive_deck):
        if len(self.hand) < Player.HAND_MAX:
            self.hand.append(defensive_deck.pop())

    def clear_hand(self):
        self.hand.clear()
