// Creating map object
var map = L.map("map", {
	center: [40.7128, -104.0059],
	zoom: 5
});
  
// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
	attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
	maxZoom: 18,
	id: "mapbox/streets-v11",
	accessToken: API_KEY
}).addTo(map);
  
// If data.beta.nyc is down comment out this link
var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";
//var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson";
  
// Example of points
/*d3.json(link, function(data) {
	L.geoJson(data).addTo(map);
});*/

markers = []

// Grabbing our GeoJSON data..
d3.json(link, function(data) {
	// Creating a GeoJSON layer with the retrieved data
	data["features"].forEach(e => {
		var circle = L.circle(e["geometry"]["coordinates"].slice(0,2).reverse(), {
			color: "dark-gray",
			fillColor: getColor(e["properties"]["mag"]),
			fillOpacity: 0.5,
			radius: parseInt(e["properties"]["mag"])*20000,
			weight: 1
        })
        
        circle.bindPopup("Magnitude: " + e["properties"]["mag"] + "<br>Location: " + e["properties"]["place"]);

        circle.addTo(map)
	})
});

var legend = L.control({position: 'bottomright'});
legend.onAdd = function(map) {
    var div = L.DomUtil.create("div", "info legend"),
        grades = [0, 1, 2, 3, 4, 5],
        colors = ["#98ee00", "#d4ee00", "#eecc00", "#ee9c00", "#ea822c", "#ea2c2c"];
    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
      div.innerHTML +=
        "<i style='background: " + colors[i] + "'></i> " +
        grades[i] + (grades[i + 1] ? "&ndash;" + grades[i + 1] + "<br>" : "+");
    }
    return div;
};

legend.addTo(map);

function getColor(d) {
    return d > 5 ? '#EA2C2C"' :
           d > 4 ? '#EA822C' :
           d > 3 ? '#EE9C00' :
           d > 2 ? '#EECC00' :
           d > 1 ? '#D4EE00' :
                   '#98EE00';
}