var contactButton = document.querySelector(".contact-button");
var contactForm = document.querySelector(".contact-section");

contactButton.addEventListener("click", function(event) {
  event.preventDefault();
  contactForm.classList.toggle("show");
});
