var prevScrollPos = window.pageYOffset;

window.onscroll = function () {
  var currentScrollPos = window.pageYOffset;
  var container = document.querySelector(".container");

  if (prevScrollPos > currentScrollPos) {
    // Scrolling Up
    container.classList.add("visible");
  } else {
    // Scrolling Down
    container.classList.remove("visible");
  }

  prevScrollPos = currentScrollPos;
};

window.addEventListener("DOMContentLoaded", function () {
  setTimeout(function () {
    var appName = document.querySelector(".welcome-section h1");
    appName.style.opacity = "1";
    appName.style.transform = "translateX(0)";

    var appDesc = document.querySelector(".welcome-section p");
    appDesc.style.opacity = "1";
    appDesc.style.transform = "translateX(0)";
  }, 200);

  animateElements();
});

window.addEventListener("scroll", function () {
  animateElements();
});

function animateElements() {
  var elementsToShow = document.querySelectorAll(".hidden");

  for (var i = 0; i < elementsToShow.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = elementsToShow[i].getBoundingClientRect().top;
    var elementBottom = elementsToShow[i].getBoundingClientRect().bottom;

    if (elementTop < windowHeight && elementBottom >= 0) {
      elementsToShow[i].classList.add("visible");
      elementsToShow[i].classList.remove("hidden");
    }
  }
}
