const gameContainer = document.getElementById("game");


const COLORS = [
  "red",
  "blue",
  "green",
  "orange",
  "purple",
  "red",
  "blue",
  "green",
  "orange",
  "purple"
];

// here is a helper function to shuffle an array
// it returns the same array with values shuffled
// it is based on an algorithm called Fisher Yates if you want ot research more
function shuffle(array) {
  let counter = array.length;

  // While there are elements in the array
  while (counter > 0) {
    // Pick a random index
    let index = Math.floor(Math.random() * counter);

    // Decrease counter by 1
    counter--;

    // And swap the last element with it
    let temp = array[counter];
    array[counter] = array[index];
    array[index] = temp;
  }

  return array;
}

let shuffledColors = shuffle(COLORS);

// this function loops over the array of colors
// it creates a new div and gives it a class with the value of the color
// it also adds an event listener for a click for each card
function createDivsForColors(colorArray) {
  for (let color of colorArray) {
    // create a new div
    const newDiv = document.createElement("div");

    // give it a class attribute for the value we are looping over
    newDiv.classList.add( color);

    // call a function handleCardClick when a div is clicked on
    newDiv.addEventListener("click", handleCardClick);

    // append the div to the element with an id of game
    gameContainer.append(newDiv);
  }
}
//variebles to play the game
awaitingEndMove = false
let activeTile = null
revealedCards = 0
totalColors = COLORS.length


// TODO: Implement this function!
function handleCardClick(event) {
  if(awaitingEndMove){
    return
  }

  
  let currentCard = event.target
  currentCard.style.backgroundColor = currentCard.classList

  if(!activeTile){
    activeTile = currentCard
    return
  
  }



  console.log(activeTile)
  console.log(currentCard)

  
  awaitingEndMove = true
 


  //make cards flip back around after a second
  setTimeout(function(){
    activeTile.style.backgroundColor = null
    currentCard.style.backgroundColor = null

    awaitingEndMove = false
    activeTile = null
  },1000)
  
  


  // you can use event.target to see which element was clicked
  // console.log("you just clicked", currentCard);
  


  
}



// when the DOM loads
createDivsForColors(shuffledColors);

