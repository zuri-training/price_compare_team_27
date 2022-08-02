// const f = document.getElementById("form")
// const q = document.getElementById("query")
// const site = "oursitedomain.com"



// f.addEventListener('submit' , submitted);


// let dropDown = document.getElementById('drop-down');
// let toggleCard = document.getElementById('toggleCard');
// function toggleFunx() {
//   toggleCard.style.display = "block"
// }


// dropDown.addEventListener('click', toggleFunx)


$('document').ready(function() {
  $('#drop-down').click(function() {
    $('#toggleCard').slideToggle(300);
  });
})

