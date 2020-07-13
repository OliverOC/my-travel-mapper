var countryButtons = document.querySelectorAll('.countries-img-link');
var countryCards = document.querySelectorAll('.map-card');

function displayCard () {
    var nameId = 'id'.concat(this.name);
    var card = document.getElementById(nameId);

    for (var i = 0; i<countryCards.length; i++) {
        countryCards[i].style.display = 'none';
    }

    card.style.display = 'block';
}

for (var button = 0; button < countryButtons.length; button++) {
    countryButtons[button].addEventListener('click', displayCard);
}
