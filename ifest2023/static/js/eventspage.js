// const btn=document.querySelectorAll('.btn');

// for(let i=0;i<btn.length;i++)
// {
//     if((i%2)==0)
//         btn[i].style.backgroundColor="#004D40";
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