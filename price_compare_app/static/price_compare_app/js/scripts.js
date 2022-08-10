$(document).ready(function() {
  $('#menu-btn').click(function() {
    $(this).css({"display":"none"})
    $('#close-box').css({"display":"block"})
    $('aside').toggle(50)
  })
  $('#close-box').click(function() {
    $(this).css({"display":"none"})
    $('#menu-btn').css({"display":"block"})
    $('aside').hide(50)
  })
  $('.toggle-category').click(function() {
    $('.categories-list').slideToggle(200, function() {
      $('.drop-down').toggleClass('down')
    })
  })
})