// JavaScript source code
// Create an array of images
var images = [
    "🐶",
    "🐱",
    "🐭",
    "🐹",
    "🐰",
    "🐻",
    "🐼",
    "🐨"
];

// Duplicate the images to make pairs
var cards = images.concat(images);

// Shuffle the cards using the Fisher-Yates algorithm
function shuffle(array) {
    var currentIndex = array.length,
        temporaryValue,
        randomIndex;

    // While there remain elements to shuffle...
    while (currentIndex !== 0) {
        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}

cards = shuffle(cards);

// Create a variable to store the flipped cards
var flippedCards = [];

// Create a variable to store the number of moves
var moves = 0;

// Create a variable to store the number of matches
var matches = 0;

// Create a function to display the cards on the screen
function displayCards() {
    // Get the element with the id of "game"
    var game = document.getElementById("game");

    // Clear the game element
    game.innerHTML = "";

    // Loop through the cards array
    for (var i = 0; i < cards.length; i++) {
        // Create a div element for each card
        var card = document.createElement("div");

        // Add a class of "card" to the card element
        card.classList.add("card");

        // Add a data attribute to store the index of the card
        card.setAttribute("data-index", i);

        // Add an event listener to handle the click on the card
        card.addEventListener("click", flipCard);

        // Append the card element to the game element
        game.appendChild(card);
    }
}

// Create a function to flip a card
function flipCard() {
    // Get the index of the clicked card from the data attribute
    var index = this.getAttribute("data-index");

    // Check if the card is already flipped or matched
    if (this.classList.contains("flipped") || this.classList.contains("matched")) {
        // Do nothing
        return;
    }

    // Check if there are already two cards flipped
    if (flippedCards.length === 2) {
        // Do nothing
        return;
    }

    // Add a class of "flipped" to the card element
    this.classList.add("flipped");

    // Add the image to the card element
    this.innerHTML = cards[index];

    // Push the index to the flippedCards array
    flippedCards.push(index);

    // Check if there are two cards flipped
    if (flippedCards.length === 2) {
        // Increment the moves by one
        moves++;

        // Update the moves display
        document.getElementById("moves").innerHTML = moves;

        // Check if the two cards match
        if (cards[flippedCards[0]] === cards[flippedCards[1]]) {
            // Match found
            matchFound();
        } else {
            // No match found
            noMatchFound();
        }
    }
}

// Create a function to handle a match found
function matchFound() {
    // Increment the matches by one
    matches++;

    // Get the two matched cards by their index
    var card1 = document.querySelector(
        '[data-index="' + flippedCards[0] + '"]'
    );
    var card2 = document.querySelector(
        '[data-index="' + flippedCards[1] + '"]'
    );

    // Add a class of "matched" to the card elements
    card1.classList.add("matched");
    card2.classList.add("matched");

    // Remove the event listeners from the card elements
    card1.removeEventListener("click", flipCard);
    card2.removeEventListener("click", flipCard);

    // Clear the flippedCards array
    flippedCards = [];



    // Check if all matches are found
    if (matches === images.length) {
        // Game over, player wins!
        gameOver();
    }
}

// Create a function to handle no match found
function noMatchFound() {
    // Set a timeout of one second before flipping back the cards
    setTimeout(function () {
        // Get the two unmatched cards by their index
        var card1 = document.querySelector(
            '[data-index="' + flippedCards[0] + '"]'
        );
        var card2 = document.querySelector(
            '[data-index="' + flippedCards[1] + '"]'
        );

        // Remove the class of "flipped" from the card elements
        card1.classList.remove("flipped");
        card2.classList.remove("flipped");

        // Remove the image from the card elements
        card1.innerHTML = "";
        card2.innerHTML = "";

        // Clear the flippedCards array
        flippedCards = [];
    }, 1000);
}

// Create a function to handle game over
function gameOver() {
    // Display a message to congratulate the player
    alert("You win! You found all the matches in " + moves + " moves.");
}

// Call the displayCards function to start the game
displayCards();
