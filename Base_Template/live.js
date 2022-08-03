
$('document').ready(function() {
  $('#view').click(function() {
    $('#toggleCard').slideToggle(130);
  });
})



// $(document).ready(function(){
//   // Show hide popover
//   $("#view").click(function(){
//     $("#toggleCard").slideToggle("fast");
//   });
// });
// $(document).on("click", function(event){
//   var $trigger = $("#toggleCard");
//   if($trigger !== event.target && !$trigger.has(event.target).length) {
//     $("#toggleCard").slideUp("fast");
//     console.log('hi');
//   }            
// });

