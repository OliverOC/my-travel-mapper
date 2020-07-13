//var nav = document.querySelector(".navbar-nav");
//var navButtons = document.querySelectorAll(".nav-item");
////var currentLocation = location.href;
//
//function setActive () {
////    nav.find(".active").removeClass("active");
////    this.classList.add("active");
//    this.innerHTML = 'check';
//}
//
//for (var button = 0; button < navButtons.length; button++) {
//    navButtons[button].addEventListener('click', setActive);
//}

//function setActive() {
//    var x = document.getElementById("test6");
//    if (x.classList.contains("active")) {
//      x.classList.remove("active");
//    } else {
//      x.classList.add("active");
//    }
//}
//
//for (var button = 0; button < navButtons.length; button++) {
//    navButtons[button].addEventListener('click', setActive);
//}

//function logoShrink () {
//    var logo = document.getElementById("main-logo");
//
//    logo.height = 100px;
//}

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        document.getElementById("main-logo").style.height = "100px";
    } else {
        document.getElementById("main-logo").style.height = "300px";
    }
}