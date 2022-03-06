const socket = new WebSocket("ws://" + location.host + "/ws");
socket.addEventListener("message", event => {
    // console.log(event.data);
    update_game(JSON.parse(event.data));
});

// Tell the backend which way the player ("left" or "right") is currently moving (either "up", "down", or "none" (to stop))
function player_move(player, direction) {
    const data = {"player": player, "direction": direction};
    socket.send(JSON.stringify(data));
}

document.addEventListener("keydown", event => {
    console.log(event.code);
    if (event.code === "KeyW") {
        player_move("left", "up");
    } else if (event.code === "KeyS") {
        player_move("left", "down");
    } else if (event.code === "ArrowUp") {
        player_move("right", "up");
    } else if (event.code === "ArrowDown") {
        player_move("right", "down");
    }
});

document.addEventListener("keyup", event => {
    if (event.code === "KeyW") {
        player_move("left", "none");
    } else if (event.code === "KeyS") {
        player_move("left", "none");
    } else if (event.code === "ArrowUp") {
        player_move("right", "none");
    } else if (event.code === "ArrowDown") {
        player_move("right", "none");
    }
});

function update_game(dict) {
    console.log(dict);
    const left = document.getElementById("left");
    const right = document.getElementById("right");
    const ball = document.getElementById("ball");
    const score_div = document.getElementById("score-div");

    left.style.top = `${dict.left}px`;
    right.style.top = `${dict.right}px`;
    ball.style.top = `${dict.bally}px`;
    ball.style.left = `${dict.ballx}px`;
    score_div.innerHTML = `${dict.score}`;


}