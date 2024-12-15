var map = L.map("map").setView([55.894323, 21.252698], 16);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

var marker = L.marker([55.894563, 21.251528]).addTo(map);
marker.bindPopup("<b>Savanorių g. 23A</b>");
// https://www.openstreetmap.org/#map=17/55.894323/21.252698
