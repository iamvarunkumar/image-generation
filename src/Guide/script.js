document.addEventListener("DOMContentLoaded", function () {
  var content = document.querySelector(".content");

  function scrollAppear() {
    var contentPosition = content.getBoundingClientRect().top;
    var screenPosition = window.innerHeight / 1.5;

    if (contentPosition < screenPosition) {
      content.classList.add("show");
    }
  }

  window.addEventListener("scroll", scrollAppear);
});
