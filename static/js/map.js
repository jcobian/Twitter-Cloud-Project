function initialize() {
        var mapOptions = {
          center: { lat: -34.397, lng: 150.644},
          zoom: 8
        };
        var map = new google.maps.Map(document.getElementById('map-canvas'),
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
	/*for (var i = 0; i < data.length; i++) {
		console.log(i + ': ' + data[i]);
	}*/
	console.log(tweetLocations.length);
});
