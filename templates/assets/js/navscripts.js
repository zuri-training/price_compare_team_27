$(document).ready(function() {
  $('#menu-btn').click(function() {
    $(this).css({"display":"none"})
    $('#close-box').css({"display":"block"})
    $('aside').toggle(50)
    $('.head-search').css({"visibility": "hidden"})
  })
  $('#close-box').click(function() {
    $(this).css({"display":"none"})
    $('#menu-btn').css({"display":"block"})
    $('aside').hide(50)
    $('.head-search').css({"visibility": "visible"})
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


var d_logoutBtnDrop = document.getElementById('f-link')
var d_ignoreLogoutPanel = document.getElementById('d-logout-panel')

document.addEventListener('click', function(event) {
  let isIgnoreLogout = d_ignoreLogoutPanel.contains(event.target)
  let isIgnoreLogoutDrop = d_logoutBtnDrop.contains(event.target)

  if (!isIgnoreLogout && !isIgnoreLogoutDrop) {
    $('#d-logout-panel').hide(100, function() {
      $('.d-p-c-down').removeClass('down')
    })
  }
})



var m_logoutBtnDrop = document.getElementById('m-p-c-down')
var m_ignoreLogoutPanel = document.getElementById('logout-panel')

document.addEventListener('click', function(event) {
  let isIgnoreLogout = m_ignoreLogoutPanel.contains(event.target)
  let isIgnoreLogoutDrop = m_logoutBtnDrop.contains(event.target)

  if (!isIgnoreLogout && !isIgnoreLogoutDrop) {
    $('#logout-panel').hide(100, function() {
      $('.m-p-c-down').removeClass('down')
    })
  }
})


var menuPanel = document.getElementById('aside')
var menuBtn = document.getElementById('menu-btn')
var closeBtn = document.getElementById('close-box')

document.addEventListener('click', function(event) {
  let isIgnoreMenuPanel = menuPanel.contains(event.target)
  let isIgnoreMenuBtn = menuBtn.contains(event.target)
  let isCloseBtn = closeBtn.contains(event.target)

  if (!isIgnoreMenuPanel && !isIgnoreMenuBtn && !isCloseBtn) {
    $('#menu-btn').css({"display":"block"})
    $('#close-box').css({"display":"none"})
    $('aside').hide()
    $('.head-search').css({"visibility": "visible"})
    $('.categories-list').hide(function() {
      $('.drop-down').removeClass('down')
    })
  }
})



// $(this).css({"display":"none"})
//     $('#close-box').css({"display":"block"})
//     $('aside').toggle(50)
//     $('.head-search').css({"display": "none"})