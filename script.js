const matches = document.querySelectorAll("div.tvarkarastis__match");
const currentDate = new Date();
const year = currentDate.getFullYear();
for (var match of matches) {
  const month_day = match.querySelector("span.tvarkarastis__date--day");
  const hour_min = match.querySelector("span.tvarkarastis__date--hour");
  const month = month_day.innerHTML.slice(0, 2);
  const day = month_day.innerHTML.slice(-2);
  const hour = hour_min.innerHTML.slice(0, 2);
  const min = hour_min.innerHTML.slice(-2);
  var match_date = new Date(year, month - 1, day, hour + 2, min);
  if (match_date > currentDate) {
    match.classList.add("tvarkarastis__match--current");
    break;
  }
}
