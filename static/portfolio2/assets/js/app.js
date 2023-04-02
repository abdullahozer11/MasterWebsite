gsap.registerPlugin(ScrollTrigger);

let card_width;

// Define a function to update the card width
function updateCardWidth() {
  card_width = document.querySelector(".card").offsetWidth + 2 * document.querySelector(".card").offsetLeft;
}

// Call the updateCardWidth function initially
updateCardWidth();

// Call the updateScrollTrigger function every time the window is resized
window.addEventListener("resize", updateCardWidth);

site_container = document.querySelector(".site-container");

showcase = document.querySelector(".showcase");
sc_container = document.querySelector(".sc-container");
card = document.querySelector(".card");
let tl0 = gsap.timeline();

for (let i = 1; i < card_count; i++) {
    tl0.to(sc_container, {x: -card_width * i})
}

ScrollTrigger.create({
    animation: tl0,
    trigger: showcase,
    pin: true,
    start: "top top",
    end: "+=" + (5 * card_width),
    scrub: true,
    snap: 1 / (card_count - 1)
});

// about section animation
class TextScramble {
    constructor(el) {
        this.el = el
        this.chars = '!<>-_\\/[]{}—=+*^?#________'
        this.update = this.update.bind(this)
    }

    setText(newText) {
        const oldText = this.el.innerText
        const length = Math.max(oldText.length, newText.length)
        const promise = new Promise((resolve) => this.resolve = resolve)
        this.queue = []
        for (let i = 0; i < length; i++) {
            const from = oldText[i] || ''
            const to = newText[i] || ''
            const start = Math.floor(Math.random() * 40)
            const end = start + Math.floor(Math.random() * 40)
            this.queue.push({from, to, start, end})
        }
        cancelAnimationFrame(this.frameRequest)
        this.frame = 0
        this.update()
        return promise
    }

    update() {
        let output = ''
        let complete = 0
        for (let i = 0, n = this.queue.length; i < n; i++) {
            let {from, to, start, end, char} = this.queue[i]
            if (this.frame >= end) {
                complete++
                output += to
            } else if (this.frame >= start) {
                if (!char || Math.random() < 0.28) {
                    char = this.randomChar()
                    this.queue[i].char = char
                }
                output += `<span class="dud">${char}</span>`
            } else {
                output += from
            }
        }
        this.el.innerHTML = output
        if (complete === this.queue.length) {
            this.resolve()
        } else {
            this.frameRequest = requestAnimationFrame(this.update)
            this.frame++
        }
    }

    randomChar() {
        return this.chars[Math.floor(Math.random() * this.chars.length)]
    }
}

const phrases = [
    "",
    "His never ending curiosity",
    "Earned him a national honor. Third place in TUBITAK National Math Competition. 2009",
    "Took him to the best campus. 2012-2017/Bosphorus University",
    "Made him leave home. 2018/Istanbul",
    "For a very exciting future. 2018/Rouen",
    "With ups and downs. 2019/Grenoble",
    "But mostly ups. 2021/Paris",
    "And a chance to find love. 2022/Paris",
    "I hope the best is yet to come!",
]

const el = document.querySelector('.scrambling-text')
const fx = new TextScramble(el)

// look later
fx.setText(phrases[1]);

let ahead = [false, false, false, false, false, false, false, false, false, false];
function toggle_text(index) {
    if (ahead[index] === true) {
        fx.setText(phrases[index-1]);
    } else {
        fx.setText(phrases[index]);
    }
    ahead[index] = !ahead[index];
}

about_section = document.querySelector(".about-section");
img_wrapper = document.querySelector(".img-wrapper");

tl = gsap.timeline();

// Comic Book Start
tl.add(function(){
    fx.setText(phrases[1]);
})
    // move to second comic
    .to(".img-wrapper", {x: '-15%', ease: "linear"})
    .add(function(){
        toggle_text(2);
    })
    .to(".img-wrapper", {x: '-30%', ease: "linear"})
    // move to third comic
    .to(".img-wrapper", {x: '-45%', ease: "linear"})
    .add(function(){
        toggle_text(3);
    })
    .to(".img-wrapper", {x: '-60%', ease: "linear"})
    // move to forth comic
    .to(".img-wrapper", {x: '-30%', y: '-15%', ease: "linear"})
    .add(function(){
        toggle_text(4);
    })
    .to(".img-wrapper", {x: '0', y: '-30%', ease: "linear"})
    // move to fifth comic
    .to(".img-wrapper", {x: '-15%', ease: "linear"})
    .add(function(){
        toggle_text(5);
    })
    .to(".img-wrapper", {x: '-30%', ease: "linear"})
    // move to sixth comic
    .to(".img-wrapper", {x: '-45%', ease: "linear"})
    .add(function(){
        toggle_text(6);
    })
    .to(".img-wrapper", {x: '-60%', ease: "linear"})
    // move to seventh comic
    .to(".img-wrapper", {x: '-30%', y: '-45%', ease: "linear"})
    .add(function(){
        toggle_text(7);
    })
    .to(".img-wrapper", {x: '0', y: '-60%', ease: "linear"})
    // move to eighth comic
    .to(".img-wrapper", {x: '-15%', ease: "linear"})
    .add(function(){
        toggle_text(8);
    })
    .to(".img-wrapper", {x: '-30%', ease: "linear"})
    // move to ninth comic
    .to(".img-wrapper", {x: '-45%', ease: "linear"})
    .add(function(){
        toggle_text(9);
    })
    .to(".img-wrapper", {x: '-60%', ease: "linear"})

ScrollTrigger.create({
    animation: tl,
    trigger: about_section,
    pin: true,
    start: "top top",
    end: '+=5000',
    scrub: true,
    snap: {
        snapTo: 1 / 8,
    }
});
