const xmlhttp = new XMLHttpRequest();
const url = "http://pricify.zurifordummies.com/static/price.json";
xmlhttp.open("GET", url, true);
xmlhttp.send();
xmlhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    const data = JSON.parse(this.responseText);
    //console.log(data);
    const months = data.Iphone_13_pro_max.map(function (elem) {
      return elem.date;
    });
    //console.log(months);
    const jumia = data.Iphone_13_pro_max.map(function (elem) {
      return elem.jumia;
    });
    const konga = data.Iphone_13_pro_max.map(function (elem) {
      return elem.konga;
    });

    const ctx = document.getElementById("canvas").getContext("2d");
    const myChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: months,
        datasets: [
          {
            label: "Jumia",
            data: jumia,
            backgroundColor: "transparent",
            borderColor: "orange",
            borderWidth: 4,
          },
          {
            label: "Konga",
            data: konga,
            backgroundColor: "transparent",
            borderColor: "pink",
            borderWidth: 4,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  }
};
