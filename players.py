class Player:
    HAND_MAX=5
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def team(self, team: str):
        self.team = team

    # def draw_card(self):
    #     # add card from offensive/defensive pile to hand
    #     self.hand.append(card)