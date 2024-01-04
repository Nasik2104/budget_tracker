const dino = document.getElementById("dino")
const cactus = document.getElementById("cactus")
let count = 0

function jump () {
    if (dino.classList != "jump") {
        dino.classList.add("jump");

        setTimeout(function () {
            dino.classList.remove("jump")
        }, 300);
    }
}

document.addEventListener("keydown", function(event) {
    jump();
})

let isAlive = setInterval(function (){
    let dinoTop = parseInt(window.getComputedStyle(dino).getPropertyValue("top"));
    let cactusLeft = parseInt(window.getComputedStyle(cactus).getPropertyValue("left"));
    count += 0.01

    if (cactusLeft < 50 && cactusLeft > 0 && dinoTop >= 140){
        alert("Game Over! Score:" + Math.round(count));
        count = 0

    }
    updateScoreDisplay()

}, 10);
function updateScoreDisplay() {
    var scoreElement = document.getElementById("counter");

    scoreElement.innerHTML = Math.round(count);

}


