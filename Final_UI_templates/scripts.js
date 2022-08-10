$(document).ready(function() {
  $('#menu-btn').click(function() {
    $(this).css({"display":"none"})
    $('#close-box').css({"display":"block"})
    $('aside').toggle(50)
    $('.head-search').css({"display": "none"})
  })
  $('#close-box').click(function() {
    $(this).css({"display":"none"})
    $('#menu-btn').css({"display":"block"})
    $('aside').hide(50)
    $('.head-search').css({"display": "block"})
    $('.categories-list').hide(function() {
      $('.drop-down').removeClass('down')
    })
  })
  $('.toggle-category').click(function() {
    $('.categories-list').slideToggle(200, function() {
      $('.drop-down').toggleClass('down')
    })
  })
  $('#f-link').click(function() {
    $('#d-logout-panel').slideToggle(100, function() {
      $('.d-p-c-down').toggleClass('down')
    })
  })
  $('.m-p-c-down').click(function() {
    $('#logout-panel').slideToggle(100, function() {
      $('.m-p-c-down').toggleClass('down')
    })
  })
})