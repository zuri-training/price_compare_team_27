function navbar() {
    var x = document.getElementById("my-top-nav");
    if (x.className === "header-nav") {
      x.className += " responsive";
    } else {
      x.className = "header-nav";
    }
  }

  function loginNav() {
    var x = document.getElementById("my-cart-nav");
    if (x.className === "cart-nav") {
      x.className += " responsive";
    } else {
      x.className = "cart-nav";
    }
  }