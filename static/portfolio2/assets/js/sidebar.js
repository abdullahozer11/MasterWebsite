"use strict";
const body = document.body;
const menu = body.querySelector(".menu");
const menuItems = menu.querySelectorAll(".menu__item");
const menuBorder = menu.querySelector(".menu__border");
let activeItem = menu.querySelector(".active");

function clickItem(item, index) {
    menu.style.removeProperty("--timeOut");
    if (activeItem == item) return;
    if (activeItem) {
        activeItem.classList.remove("active");
    }
    item.classList.add("active");
    activeItem = item;
    offsetMenuBorder(activeItem, menuBorder);
}

function offsetMenuBorder(element, menuBorder) {
    const offsetActiveItem = element.getBoundingClientRect();
    const top = Math.floor(offsetActiveItem.top - menu.offsetTop - (menuBorder.offsetHeight - offsetActiveItem.height) / 2) + "px";
    menuBorder.style.transform = `translate3d(0, ${top} , 0)`;
}

offsetMenuBorder(activeItem, menuBorder);
menuItems.forEach((item, index) => {
    item.addEventListener("mouseover", () => clickItem(item, index));
})
window.addEventListener("resize", () => {
    offsetMenuBorder(activeItem, menuBorder);
    menu.style.setProperty("--timeOut", "none");
});
