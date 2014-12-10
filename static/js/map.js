var map;
function initialize() {
        var mapOptions = {
          center: { lat: 45.231181, lng: 34.381133 },
          zoom: 2
        };
        map = new google.maps.Map(document.getElementById('map-canvas'),
            mapOptions)
}
google.maps.event.addDomListener(window, 'load', initialize);

/* AJAX request to get locations for map
 *
 */

$.ajax({
	url: "http://ec2-54-164-93-32.compute-1.amazonaws.com:5000/tweetLocations"
}).done(function(data){
	var tweetLocations = JSON.parse(data);
	
	// Load markers into array with Google LatLngs
	var markers = [];
	for (var i = 0; i < tweetLocations.length; i++) {
	  var latLng = new google.maps.LatLng(parseFloat(tweetLocations[i].lat),
	      parseFloat(tweetLocations[i].lng));
	  var marker = new google.maps.Marker({'position': latLng});
	  markers.push(marker);
	}
	// Puts all markers on the map using the MarkerCluterer library
	var markerCluster = new MarkerClusterer(map, markers);
	console.log(tweetLocations.length);
});
