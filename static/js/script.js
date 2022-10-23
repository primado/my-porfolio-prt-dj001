/* Open when someone clicks on the span element */
function openNav() {
  document.getElementById("myNav").style.height = "100vh";
}

/* Close when someone clicks on the "x" symbol inside the overlay */
function closeNav() {
  document.getElementById("myNav").style.height = "0";
}

/* Initialize Animate on scroll library */
document.addEventListener("DOMContentLoaded", function () {
  AOS.init();
});
