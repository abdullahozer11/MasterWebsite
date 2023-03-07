class Pacman {
    constructor(x, y, width, height, speed) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.speed = speed;
        this.direction = DIRECTION_RIGHT;
        this.nextDirection = DIRECTION_RIGHT;
        this.currentFrame = 0;
        this.frameCount = 7;
        this.score = 0;
        this.lives = 3;
        setInterval(() => {
            this.changeAnimation();
        }, 150);
    }

    moveProcess() {
        this.changeDirectionIfPossible();
        this.move_forward();
        this.eat();
        if (this.check_collision()) {
            this.move_backward();
        }
    }

    draw() {
        ctx.save();
        ctx.translate(
            this.x + BLOCK_SIZE / 2,
            this.y + BLOCK_SIZE / 2
        );
        ctx.rotate((this.direction * Math.PI) / 2);
        ctx.translate(
            -this.x - BLOCK_SIZE / 2,
            -this.y - BLOCK_SIZE / 2
        );
        ctx.drawImage(pacmanFrames,
            this.currentFrame * BLOCK_SIZE,
            0,
            BLOCK_SIZE,
            BLOCK_SIZE,
            this.x,
            this.y,
            this.width,
            this.height);
        ctx.restore();
    }

    move_forward() {
        switch (this.direction) {
            case DIRECTION_RIGHT:
                this.x += this.speed;
                break;
            case DIRECTION_LEFT:
                this.x -= this.speed;
                break;
            case DIRECTION_UP:
                this.y -= this.speed;
                break;
            case DIRECTION_DOWN:
                this.y += this.speed;
                break;
        }
    }

    move_backward() {
        switch (this.direction) {
            case DIRECTION_RIGHT:
                this.x -= this.speed;
                break;
            case DIRECTION_LEFT:
                this.x += this.speed;
                break;
            case DIRECTION_UP:
                this.y += this.speed;
                break;
            case DIRECTION_DOWN:
                this.y -= this.speed;
                break;
        }
    }

    check_collision() {
        const mapX = this.getMapX();
        const mapY = this.getMapY();
        const mapXRight = this.getMapXRight();
        const mapYBottom = this.getMapYBottom();
        return map[mapY][mapX] === 1 ||
            map[mapY][mapXRight] === 1 ||
            map[mapYBottom][mapX] === 1 ||
            map[mapYBottom][mapXRight] === 1;
    }

    changeAnimation() {
        this.currentFrame = (this.currentFrame + 1) % this.frameCount;
    }

    changeDirectionIfPossible() {
        if (this.direction === this.nextDirection) {return}
        let tempDirection = this.direction;
        this.direction = this.nextDirection;
        this.move_forward();
        if (this.check_collision()) {
            this.move_backward();
            this.direction = tempDirection;
        }
    }

    eat() {
        let mapX = this.getMapX();
        let mapY = this.getMapY();
        if (map[mapY][mapX] === 2) {
            map[mapY][mapX] = 3;
            this.score ++;
        }
    }

    getMapX() {
        return parseInt(this.x / BLOCK_SIZE);
    }

    getMapXRight() {
        return parseInt((this.x + BLOCK_SIZE * 0.99) / BLOCK_SIZE);
    }

    getMapYBottom() {
        return parseInt((this.y + BLOCK_SIZE * 0.99) / BLOCK_SIZE);
    }

    getMapY() {
        return parseInt(this.y / BLOCK_SIZE);
    }
}
