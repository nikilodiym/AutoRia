function toggleDetailFav(btn) {
    btn.classList.toggle('is-liked');
}

function copyVin(vin) {
    navigator.clipboard.writeText(vin).catch(function() {});
}