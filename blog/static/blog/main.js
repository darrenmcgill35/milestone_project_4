 function initMap() {
     const map = new google.maps.Map(document.getElementById("map"), {
         zoom: 5,
         center: {
             lat: 53.350140,
             lng: -6.266155
         }
     });

     const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

     const locations = [
         {lat: 53.360799, lng: -6.251241}
     ];

     const markers = locations.map(function (location, i) {
         return new google.maps.Marker({
             position: location,
             label: labels[i % labels.length]
         });
     });
     const markerCluster = new MarkerClusterer(map, markers, {
         imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
     });
 }