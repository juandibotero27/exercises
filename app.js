//1
// fav_num = 7
// url = 'http://numbersapi.com/'
// fav_nums = [7,4,6,5]

// $.getJSON(`${url}${fav_num}?json`).then(res => console.log(res))

// $.getJSON(`${url}${fav_nums}?json`).then(res => console.log(res))

// for(let i=0;i<4;i++){
//     Promise.all($.getJSON(`${url}${fav_num}?json`).then(facts => $('body').append(`<p>${facts.text}</p>`)))
// }

///////////////////////////////////////////////////////////////

//2
url = 'https://deckofcardsapi.com/api/deck'

$.getJSON(`${url}/new/draw`).then(res => console.log(`${res.cards[0].value} of ${res.cards[0].suit}`))

let firstCard = null;
$.getJSON(`${url}/new/draw/`)
  .then(data => {
    firstCard = data.cards[0];
    let deckId = data.deck_id;
    return $.getJSON(`${url}/${deckId}/draw/`);
  })
  .then(data => {
    let secondCard = data.cards[0];
    [firstCard, secondCard].forEach(function(card) {
      console.log(
        `${card.value.toLowerCase()} of ${card.suit.toLowerCase()}`
      );
    });
  });

// 3.
let deckId = null;
let $btn = $('button');
let $cardArea = $('#card-area');

$.getJSON(`${url}/new/shuffle/`).then(data => {
  deckId = data.deck_id;
  $btn.show();
});

$btn.on('click', function() {
  $.getJSON(`${url}/${deckId}/draw/`).then(data => {
    let cardSrc = data.cards[0].image;
    let angle = Math.random() * 90 - 45;
    let randomX = Math.random() * 40 - 20;
    let randomY = Math.random() * 40 - 20;
    $cardArea.append(
      $('<img>', {
        src: cardSrc,
        css: {
          transform: `translate(${randomX}px, ${randomY}px) rotate(${angle}deg)`
        }
      })
    );
    if (data.remaining === 0) $btn.remove();
  });
});




