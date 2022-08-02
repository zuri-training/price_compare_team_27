function myFunction() {
    var x = document.getElementById("mheader-nav");
    if (x.className === "header-nav") {
      x.className += " responsive";
    } else {
      x.className = "header-nav";
    }
  }