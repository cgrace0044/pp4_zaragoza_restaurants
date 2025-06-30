(async function() {
  // Import the Maps library from the Google Maps API
  const { Map } = await google.maps.importLibrary("maps");
  // Import the AdvancedMarkerElement from the Marker library
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
  // Create a new Map instance and render it inside the element with id "map"
  const map = new Map(document.getElementById("map"), {
    center: { lat: 41.6474, lng: -0.8861 }, // Set initial center of the map (latitude and longitude)
    zoom: 12, // Set initial zoom level
    mapId: "4504f8b37365c3d0",
  });
  // Add an advanced marker to the map at a specific position
  const marker = new AdvancedMarkerElement({
    map,
    position: { lat: 41.6231, lng: -0.9324 },
  });
})();