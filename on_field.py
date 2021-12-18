class Field_data:
    midfield = 50
    field_length = 100
    MAX_DOWN = 4

    down = 1
    ball_spot = 1
    first_ball_spot = ball_spot
    first_down_marker = first_ball_spot + 10

    def __init__(self):
        self.down = 1
        self.ball_spot = 1

    def spot_ball(self, spot):
        self.ball_spot = spot
        print(f'Spot of ball (int): {self.ball_spot}')

    def move_ball(self, yards):
        if yards >= 0:
            self.ball_spot += yards
        else:
            self.ball_spot -= yards
        print(f'Spot of ball (int): {self.ball_spot}')

    def first_down(self):
        self.down = 1
        print(f'First down at the {self.ball_spot} yard line!')

    def touchdown(self, player):
        player.score += 6