var bird;
var walls;
var topScore = 0;
var sqFont;

function preload() {
    sqFont = loadFont('js/flappy/Square.ttf');
}

function setup() {
    textFont(sqFont);
    cv = createCanvas(400,600);
    cv.parent('canvas');
    bird = new Bird();
    walls = new Walls();
}

function draw() {
    background(255);
    walls.update();
    bird.update();
}

function keyPressed() {
    if (key === ' ') {
        bird.flap();
    }
}