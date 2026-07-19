import random

def play_hangman():
    # 5 predefined words
    words = ["python", "banana", "guitar", "puzzle", "monkey"]
    
    # Select a random word from the list
    secret_word = random.choice(words).lower()
    
    # Store all letters guessed by the player (both correct and incorrect) in a list
    guessed_letters = []
    
    # Incorrect guesses limit
    incorrect_guesses_remaining = 6
    
    print("=" * 40)
    print("Welcome to Hangman!")
    print("=" * 40)
    print("I have chosen a secret word. Can you guess it?")
    print("You have 6 lives (incorrect guesses allowed). Good luck!")
    print()

    # Main game loop
    while incorrect_guesses_remaining > 0:
        # Display the word with guessed letters revealed and others as underscores
        current_display = []
        for letter in secret_word:
            if letter in guessed_letters:
                current_display.append(letter)
            else:
                current_display.append("_")
        
        print("Word to guess: " + " ".join(current_display))
        print(f"Incorrect guesses remaining: {incorrect_guesses_remaining}")
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print()

        # Check if the player has guessed all the letters
        # We check if every letter in the secret_word is in our list of guessed_letters
        word_is_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_is_guessed = False
                break

        if word_is_guessed:
            print("🎉 Congratulations! You guessed the word correctly! 🎉")
            print(f"The word was: {secret_word.upper()}")
            print("=" * 40)
            return

        # Player guess input
        guess = input("Guess a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single alphabetical letter.\n")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed the letter '{guess}'. Try a different one.\n")
            continue

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the secret word
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses_remaining -= 1
            print(f"❌ Oops! '{guess}' is not in the word.\n")

    # If the loop finished without winning, the player lost
    print("💀 Game Over! You ran out of guesses. 💀")
    print(f"The secret word was: {secret_word.upper()}")
    print("=" * 40)

if __name__ == "__main__":
    play_hangman()
    