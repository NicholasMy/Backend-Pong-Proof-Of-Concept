import json

from PongBall import PongBall
from PongPlayer import PongPlayer


class PongGame:
    def __init__(self):
        self.left = PongPlayer()
        self.right = PongPlayer()
        self.ball = PongBall()
        self.height = 600
        self.width = 800

    def to_json(self):
        game_dict = {
            "left": self.left.position,
            "right": self.right.position,
            "ballx": self.ball.x,
            "bally": self.ball.y,
            "score": f"{self.left.score} - {self.right.score}",
        }
        j = json.dumps(game_dict)
        return j

    def update_from_socket(self, j):
        if j["player"] == "left":
            self.left.direction = j["direction"]
        elif j["player"] == "right":
            self.right.direction = j["direction"]

    def advance_frame(self):
        # Move the left player
        if self.left.direction == "up":
            self.left.position -= 15
        elif self.left.direction == "down":
            self.left.position += 15

        # Right player
        if self.right.direction == "up":
            self.right.position -= 15
        elif self.right.direction == "down":
            self.right.position += 15

        # Move the ball
        self.ball.x += self.ball.x_velocity
        self.ball.y += self.ball.y_velocity

        if self.ball.x < 0 - self.ball.width:
            # Right player scored
            self.right.score += 1
            self.ball.x = 380
            self.ball.y = 280
            self.ball.x_velocity *= -1

        if self.ball.x > self.width:
            # Left player scored
            self.left.score += 1
            self.ball.x = 380
            self.ball.y = 280
            self.ball.x_velocity *= -1

        # Hits top or bottom wall
        if self.ball.y < 0:
            self.ball.y_velocity *= -1
        if self.ball.y > 600 - self.ball.height:
            self.ball.y_velocity *= -1

        # Hits left player
        if self.left.position < self.ball.y < self.left.position + 150 + self.ball.height and self.ball.x <= 25:
            self.ball.x_velocity *= -1

        # Hits right player
        if self.right.position < self.ball.y < self.right.position + 150 + self.ball.height and self.ball.x + self.ball.width / 2 >= self.width - self.ball.width:
            self.ball.x_velocity *= -1

        # bot mode
        # self.left.position = self.ball.y - 75
        self.right.position = self.ball.y - 75
