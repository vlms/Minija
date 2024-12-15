const nexts = document.querySelectorAll("div.next");
const currentDate = new Date();
const year = currentDate.getFullYear();
var playing_now = false;
for (var next of nexts) {
  const mon_d_h_min = next.querySelector("span.next__date");
  const month = mon_d_h_min.innerHTML.slice(0, 2);
  const day = mon_d_h_min.innerHTML.slice(3, 5);
  const hour = mon_d_h_min.innerHTML.slice(6, 8);
  const min = mon_d_h_min.innerHTML.slice(-2);
  var next_date = new Date(year, month - 1, day, hour, min);

  if (
    currentDate - next_date < 2 * 60 * 60 * 1000 &&
    currentDate - next_date > 0
  ) {
    playing_now = true;
    var next_left = next.querySelector("span.next__left");
    next.style.display = "grid";
    next_left.innerHTML = "Vyksta rungtynės";
    break;
  }
  if (next_date > currentDate) {
    var milis = next_date - currentDate;
    // console.log(next_date - currentDate);
    var next_left = next.querySelector("span.next__left");

    next.style.display = "grid";
    break;
  }
}

// var millis = 123456789;

function pad(number) {
  var result = "" + number;
  if (result.length < 2) {
    result = "0" + result;
  }

  return result;
}

function displaytimer() {
  //Thank you MaxArt.

  var days = Math.floor(milis / 864e5),
    hours = Math.floor((milis % 864e5) / 36e5),
    mins = Math.floor((milis % 36e5) / 6e4),
    secs = Math.floor((milis % 6e4) / 1000);

  var liko = "Liko: ";
  if (days) {
    liko += days + "d. " + pad(hours) + ":" + pad(mins) + ":" + pad(secs);
  } else {
    liko += hours + ":" + pad(mins) + ":" + pad(secs);
  }
  next_left.innerHTML = liko;
}

if (!playing_now) {
  setInterval(function () {
    milis -= 1000;
    displaytimer();
  }, 1000);
}
