let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
  const map = new Map(document.getElementById("map"), {
    center: { lat: 41.6474, lng: -0.8861 },
    zoom: 12,
    mapId: "4504f8b37365c3d0",
  });
  const marker = new AdvancedMarkerElement({
    map,
    position: { lat: 41.6231, lng: -0.9324 },
  });
}

initMap();