// Edit trip switch button
var switchEditDelete = document.getElementById('edit-delete-button');

function showEditDelete () {
    var editDelete = document.querySelectorAll('.edit-delete');
    for (var i = 0; i < editDelete.length; i++) {
         if (editDelete[i].style.display === 'block') {
            editDelete[i].style.display = 'none';
         } else {
            editDelete[i].style.display = 'block';
         }
    }
}

switchEditDelete.addEventListener('click', showEditDelete);


// Toggle photo card front/back on hover
var cards = document.querySelectorAll('.photo-card-content');

function showBack () {
    var cardFront = this.querySelector('.photo-card-front');
    var cardBack = this.querySelector('.photo-card-back');

    cardFront.style.display = 'none';
    cardBack.style.display = 'flex';
}

function showFront () {
    var cardFront = this.querySelector('.photo-card-front');
    var cardBack = this.querySelector('.photo-card-back');

    cardFront.style.display = 'block';
    cardBack.style.display = 'none';
}

for (var card = 0; card < cards.length; card++) {
    cards[card].addEventListener('mouseenter', showBack);
    cards[card].addEventListener('mouseleave', showFront);
}

