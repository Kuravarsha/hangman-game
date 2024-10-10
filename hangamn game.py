import random

# Word categories
words = {
    "animals": ["tiger", "elephant", "giraffe", "penguin", "kangaroo"],
    "countries": ["germany", "canada", "brazil", "india", "japan"],
    "movies": ["inception", "avatar", "gladiator", "matrix", "titanic"]
}

# Hangman stages (ASCII art)
hangman_pics = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========""", """
       ------
       |    |
       O    |
            |
            |
            |
    =========""", """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========""", """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========""", """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========""", """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========""", """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    ========="""
]

# Function to choose a word from the selected category
def choose_word(category):
    return random.choice(words[category])

# Function to display the current game status
def display_game_status(hangman_pics, incorrect_guesses, correct_guesses, secret_word):
    print(hangman_pics[len(incorrect_guesses)])
    print("Incorrect guesses: ", " ".join(incorrect_guesses))
    print("Word: ", " ".join([letter if letter in correct_guesses else "_" for letter in secret_word]))

# Main game loop
def play_hangman():
    print("Welcome to Hangman!")
    
    # Choose a category
    category = input("Choose a category (animals, countries, movies): ").lower()
    if category not in words:
        print("Invalid category. Exiting game.")
        return
    
    # Choose difficulty level
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    if difficulty == "easy":
        allowed_incorrect_guesses = 8
    elif difficulty == "medium":
        allowed_incorrect_guesses = 6
    else:
        allowed_incorrect_guesses = 4
    
    secret_word = choose_word(category)
    correct_guesses = []
    incorrect_guesses = []
    hint_used = False
    
    print(f"You have {allowed_incorrect_guesses} incorrect guesses allowed. Let's start!")

    while len(incorrect_guesses) < allowed_incorrect_guesses:
        display_game_status(hangman_pics, incorrect_guesses, correct_guesses, secret_word)
        guess = input("Guess a letter (or type 'hint' for a clue): ").lower()
        
        if guess == "hint" and not hint_used:
            print(f"Hint: The word is related to {category}.")
            hint_used = True
            continue
        elif guess == "hint" and hint_used:
            print("Hint already used!")
            continue
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in correct_guesses or guess in incorrect_guesses:
            print("You already guessed that letter!")
            continue

        if guess in secret_word:
            correct_guesses.append(guess)
            if all([letter in correct_guesses for letter in secret_word]):
                print(f"Congratulations! You guessed the word: {secret_word}")
                break
        else:
            incorrect_guesses.append(guess)
    
    if len(incorrect_guesses) == allowed_incorrect_guesses:
        display_game_status(hangman_pics, incorrect_guesses, correct_guesses, secret_word)
        print(f"Sorry, you've been hanged! The word was: {secret_word}")

# Run the game
play_hangman()
