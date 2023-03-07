class Ghost {
    constructor(x, y, width, height, speed, imgX, imgY, range) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.speed = speed;
        this.direction = DIRECTION_DOWN;
        this.imgX = imgX;
        this.imgY = imgY;
        this.range = range;
        this.randomTargetIndex = parseInt(Math.random() * RandomTargetList.length);
        this.target = RandomTargetList[this.randomTargetIndex];
        setInterval(() => {
            this.changeTarget();
        }, 10000);
    }

    moveProcess() {
        if (this.isPacmanInRange()) {
            this.target = pacman;
        } else {
            this.target = RandomTargetList[this.randomTargetIndex];
        }
        this.changeDirectionIfPossible();
        this.move_forward();
        if (this.check_collision()) {
            this.move_backward();
        }
    }

    draw() {
        ctx.save();
        ctx.drawImage(ghostFrames,
            this.imgX,
            this.imgY,
            this.width,
            this.height,
            this.x - BLOCK_SIZE * 0.4,
            this.y - BLOCK_SIZE * 0.4,
            BLOCK_SIZE * 1.8,
            BLOCK_SIZE * 1.8);
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

    isPacmanInRange() {
        const xDif = Math.abs(pacman.getMapX() - this.getMapX());
        const yDif = Math.abs(pacman.getMapY() - this.getMapY());
        return Math.sqrt(xDif * xDif + yDif * yDif) <= this.range;
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

    changeTarget() {
        this.randomTargetIndex = (this.randomTargetIndex + 1) % RandomTargetList.length;
    }

    changeDirectionIfPossible() {
        let tmpDirection = this.direction;
        this.direction = this.calculateNewDirection(
            map,
            parseInt(this.target.x / BLOCK_SIZE),
            parseInt(this.target.y / BLOCK_SIZE)
        );
        if (typeof this.direction == "undefined") {
            this.direction = tmpDirection;
            return;
        }
        this.move_forward();
        if (this.check_collision()) {
            this.move_backward();
            this.direction = tmpDirection;
        } else {
            this.move_backward();
        }
    }

    calculateNewDirection(map, destX, destY) {
        let mp = [];
        for (let i = 0; i < map.length; i++) {
            mp[i] = map[i].slice();
        }

        let queue = [
            {
                x: this.getMapX(),
                y: this.getMapY(),
                rightX: this.getMapXRight(),
                rightY: this.getMapYBottom(),
                moves: [],
            },
        ];

        while (queue.length > 0) {
            let poped = queue.shift();
            if (poped.x == destX && poped.y == destY) {
                return poped.moves[0];
            } else {
                mp[poped.y][poped.x] = 1;
                let neighborList = this.addNeighbors(poped, mp);
                for (let i = 0; i < neighborList.length; i++) {
                    queue.push(neighborList[i]);
                }
            }
        }
        return 1;
    }

    addNeighbors(poped, mp) {
        let queue = [];
        let numOfRows = mp.length;
        let numOfColumns = mp[0].length;

        if (
            poped.x - 1 >= 0 &&
            poped.x - 1 < numOfRows &&
            mp[poped.y][poped.x - 1] != 1
        ) {
            let tempMoves = poped.moves.slice();
            tempMoves.push(DIRECTION_LEFT);
            queue.push({ x: poped.x - 1, y: poped.y, moves: tempMoves });
        }
        if (
            poped.x + 1 >= 0 &&
            poped.x + 1 < numOfRows &&
            mp[poped.y][poped.x + 1] != 1
        ) {
            let tempMoves = poped.moves.slice();
            tempMoves.push(DIRECTION_RIGHT);
            queue.push({ x: poped.x + 1, y: poped.y, moves: tempMoves });
        }
        if (
            poped.y - 1 >= 0 &&
            poped.y - 1 < numOfColumns &&
            mp[poped.y - 1][poped.x] != 1
        ) {
            let tempMoves = poped.moves.slice();
            tempMoves.push(DIRECTION_UP);
            queue.push({ x: poped.x, y: poped.y - 1, moves: tempMoves });
        }
        if (
            poped.y + 1 >= 0 &&
            poped.y + 1 < numOfColumns &&
            mp[poped.y + 1][poped.x] != 1
        ) {
            let tempMoves = poped.moves.slice();
            tempMoves.push(DIRECTION_DOWN);
            queue.push({ x: poped.x, y: poped.y + 1, moves: tempMoves });
        }
        return queue;
    }
}
