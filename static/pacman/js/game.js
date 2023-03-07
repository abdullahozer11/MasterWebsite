const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext("2d");
const pacmanFrames = document.getElementById('pacman-frames');
const ghostFrames = document.getElementById('ghost-frames');

const up = document.getElementById('up');
const down = document.getElementById('down');
const left = document.getElementById('left');
const right = document.getElementById('right');

const WALL_COLOR = '#342DCA';
const wallInnerColor = '#000000';
const FOOD_COLOR = '#fdfd01';

const DIRECTION_RIGHT = 4;
const DIRECTION_UP = 3;
const DIRECTION_LEFT = 2;
const DIRECTION_DOWN = 1;

const BLOCK_SIZE = 20;
let wallSpaceWidth = BLOCK_SIZE / 3;
let wallOffset = (BLOCK_SIZE - wallSpaceWidth) / 2;
const fps = 30;

const GHOST_WIDTH = 126;
const GHOST_HEIGHT = 117;
const GHOST_POSITIONS = [
    {x: 0, y: 0},
    {x: 176, y: 0},
    {x: 0, y: GHOST_HEIGHT},
    {x: 176, y: GHOST_HEIGHT},
];

const RandomTargetList = [
    {x: BLOCK_SIZE, y: BLOCK_SIZE},
    {x: BLOCK_SIZE, y: 19 * BLOCK_SIZE},
    {x: 19 * BLOCK_SIZE, y: BLOCK_SIZE},
    {x: 19 * BLOCK_SIZE, y: BLOCK_SIZE}
];

const map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

// game functions
let draw_rect = (x, y, width, height, color) => {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, width, height);
}

let draw_walls = () => {
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[i].length; j++) {
            if (map[i][j] === 1) {
                draw_rect(j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, WALL_COLOR);
                if (j > 0 && map[i][j - 1] === 1) {
                    draw_rect(
                        j * BLOCK_SIZE,
                        i * BLOCK_SIZE + wallOffset,
                        wallSpaceWidth + wallOffset,
                        wallSpaceWidth,
                        wallInnerColor
                    );
                }

                if (j < map[0].length - 1 && map[i][j + 1] === 1) {
                    draw_rect(
                        j * BLOCK_SIZE + wallOffset,
                        i * BLOCK_SIZE + wallOffset,
                        wallSpaceWidth + wallOffset,
                        wallSpaceWidth,
                        wallInnerColor
                    );
                }

                if (i < map.length - 1 && map[i + 1][j] === 1) {
                    draw_rect(
                        j * BLOCK_SIZE + wallOffset,
                        i * BLOCK_SIZE + wallOffset,
                        wallSpaceWidth,
                        wallSpaceWidth + wallOffset,
                        wallInnerColor
                    );
                }
                if (i > 0 && map[i - 1][j] === 1) {
                    draw_rect(
                        j * BLOCK_SIZE + wallOffset,
                        i * BLOCK_SIZE,
                        wallSpaceWidth,
                        wallSpaceWidth + wallOffset,
                        wallInnerColor
                    );
                }
            }
        }
    }
}

let draw_foods = () => {
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[i].length; j++) {
            if (map[i][j] === 2) {
                draw_rect(j * BLOCK_SIZE + BLOCK_SIZE / 3, i * BLOCK_SIZE + BLOCK_SIZE / 3, BLOCK_SIZE / 3, BLOCK_SIZE / 3, FOOD_COLOR);
            }
        }
    }
}

let game_loop = () => {
    draw();
    update();
}

let move_ghosts = () => {
    for (let i = 0; i < ghosts.length; i++) {
        ghosts[i].moveProcess();
    }
}

check_collision = (ghost, pacman) => {
    return ghost.getMapX() === pacman.getMapX() && ghost.getMapY() === pacman.getMapY();
}

let check_ghost_collision = () => {
    for (let i = 0; i < ghosts.length; i++) {
        let collided = check_collision(ghosts[i], pacman);
        if (collided) {
            return true;
        }
    }
    return false;
}

let draw_game_over = () => {
    ctx.font = "50px Emulogic";
    ctx.fillStyle = "white";
    ctx.fillText("Game Over", 4 * BLOCK_SIZE, 10 * BLOCK_SIZE);
}

let restart = () => {
    pacman.x = BLOCK_SIZE;
    pacman.y = BLOCK_SIZE;
    pacman.direction = DIRECTION_RIGHT;
    pacman.nextDirection = DIRECTION_RIGHT;
}

let check_win = () => {
    if (pacman.score === 217) {
        ctx.font = "50px Emulogic";
        ctx.fillStyle = "white";
        ctx.fillText("You Win", 4 * BLOCK_SIZE, 10 * BLOCK_SIZE);
        clearInterval(GameInterval);
    }
}

let update = () => {
    pacman.moveProcess();
    move_ghosts();
    if (check_ghost_collision()) {
        pacman.lives--;
        if (pacman.lives === 0) {
            draw_game_over();
            clearInterval(GameInterval);
        } else {
            restart();
        }
    }
    check_win();
}

let draw_ghosts = () => {
    for (let i = 0; i < ghosts.length; i++) {
        ghosts[i].draw();
    }
}

let draw = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    draw_rect(0, 0, canvas.width, canvas.height, 'black');
    draw_score();
    draw_lives();
    draw_walls();
    draw_foods();
    pacman.draw();
    draw_ghosts();
}

let draw_score = () => {
    ctx.font = "30px Emulogic";
    ctx.fillStyle = "white";
    ctx.fillText("Score: " + pacman.score, 20, map.length * BLOCK_SIZE + 30);
}

const livesXPos = 270;

let draw_lives = () => {
    ctx.font = "30px Emulogic";
    ctx.fillStyle = "white";
    ctx.fillText("Lives: ", livesXPos, map.length * BLOCK_SIZE + 30);
    for (let i = 0; i < pacman.lives; i++) {
        ctx.drawImage(pacmanFrames,
            2 * BLOCK_SIZE,
            0,
            BLOCK_SIZE,
            BLOCK_SIZE,
            livesXPos + 80 + i * (BLOCK_SIZE + 2),
            471,
            BLOCK_SIZE,
            BLOCK_SIZE);
    }
}

pacman = new Pacman(BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE / 5);
let ghosts = [];
ghosts.push(new Ghost(9 * BLOCK_SIZE, 10 * BLOCK_SIZE, GHOST_WIDTH, GHOST_HEIGHT, BLOCK_SIZE / 10, GHOST_POSITIONS[0].x, GHOST_POSITIONS[0].y, 5));
ghosts.push(new Ghost(9 * BLOCK_SIZE, 11 * BLOCK_SIZE, GHOST_WIDTH, GHOST_HEIGHT, BLOCK_SIZE / 10, GHOST_POSITIONS[1].x, GHOST_POSITIONS[1].y, 6));
ghosts.push(new Ghost(11 * BLOCK_SIZE, 10 * BLOCK_SIZE, GHOST_WIDTH, GHOST_HEIGHT, BLOCK_SIZE / 10, GHOST_POSITIONS[2].x, GHOST_POSITIONS[2].y, 7));
ghosts.push(new Ghost(11 * BLOCK_SIZE, 10 * BLOCK_SIZE, GHOST_WIDTH, GHOST_HEIGHT, BLOCK_SIZE / 10, GHOST_POSITIONS[3].x, GHOST_POSITIONS[3].y, 8));
game_loop();

document.addEventListener('keydown', (e) => {
    switch (e.key) {
        case 'ArrowUp':
            pacman.nextDirection = DIRECTION_UP;
            break;
        case 'ArrowDown':
            pacman.nextDirection = DIRECTION_DOWN;
            break;
        case 'ArrowLeft':
            pacman.nextDirection = DIRECTION_LEFT;
            break;
        case 'ArrowRight':
            pacman.nextDirection = DIRECTION_RIGHT;
            break;
    }
});

let touchStartX = 0;
let touchStartY = 0;
const minSwipeDistance = 30;

document.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
});

document.addEventListener('touchend', (e) => {
    const touchEndX = e.changedTouches[0].clientX;
    const touchEndY = e.changedTouches[0].clientY;
    const dx = touchEndX - touchStartX;
    const dy = touchEndY - touchStartY;

    if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > minSwipeDistance) {
        pacman.nextDirection = dx > 0 ? DIRECTION_RIGHT : DIRECTION_LEFT;
    } else if (Math.abs(dy) > Math.abs(dx) && Math.abs(dy) > minSwipeDistance) {
        pacman.nextDirection = dy > 0 ? DIRECTION_DOWN : DIRECTION_UP;
    }
});

up.addEventListener('click', () => {
    pacman.nextDirection = DIRECTION_UP;
});

down.addEventListener('click', () => {
    pacman.nextDirection = DIRECTION_DOWN;
});

left.addEventListener('click', () => {
    pacman.nextDirection = DIRECTION_LEFT;
});

right.addEventListener('click', () => {
    pacman.nextDirection = DIRECTION_RIGHT;
});

let GameInterval = setInterval(game_loop, 1000 / fps);
