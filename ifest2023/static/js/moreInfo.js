/*const targetData = document.querySelector(".round-display-toggle");
const trigger = document.querySelector(".round-heading");
trigger.onclick = function(){
    if (targetData.style.display !== "none") {
        targetData.style.display = "none";
    }
    else {
        targetData.style.display = "block";
    }
};*/

// function toggleDisplay(){
//     arg = event.target.getAttribute('arg');
//     const targetData = document.getElementById(arg);
//       if (targetData.style.display !== "none") {
//          targetData.style.display = "none";
//      }
//     else {
//          targetData.style.display = "block";
//      }

// }

var pieSize = 55;

for (i = 1; i < 4; i++) {
  $(".pie__corner:first-child").clone().appendTo(".pie");
}

const moveBg = () => {
  $('.pie__piece').width(pieSize + pageYOffset / $('.container').height() * pieSize + 'rem');
};

moveBg();

window.addEventListener('scroll', function () {
  moveBg();
});