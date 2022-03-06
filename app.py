import json
import time

from flask import Flask, render_template, send_from_directory
from flask_sock import Sock

from PongGame import PongGame

app = Flask(__name__)
sock = Sock(app)

game = PongGame()


@app.route("/")
def hello_world():  # put application"s code here
    return render_template("index.html")


@app.route("/static/<path:file>")
def static_files(file):
    return send_from_directory("static", file)


@sock.route("/ws")
def ws(socket):
    while True:
        raw_data = socket.receive(timeout=0)
        if raw_data:
            j = json.loads(raw_data)
            game.update_from_socket(j)
            print(j)

        socket.send(game.to_json())
        game.advance_frame()
        time.sleep(.005)


if __name__ == "__main__":
    app.run()
