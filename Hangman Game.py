import random

# Step 1: Choose a Word List
word_list = ["python", "hangman", "programming", "developer", "algorithm","computer", "software", "application", "database", "network"]

def get_random_word(word_list):
    """Select a random word from the word list."""
    return random.choice(word_list)

def display_word_progress(word, guessed_letters):
    """Display the current progress of the word being guessed."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    word = get_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = set()
    max_attempts = 6
    
    print("Welcome to Hangman!")
    
    while len(incorrect_guesses) < max_attempts:
        print(f"Word: {display_word_progress(word, guessed_letters)}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Remaining attempts: {max_attempts - len(incorrect_guesses)}")

        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter.")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            incorrect_guesses.add(guess)
            print(f"Incorrect guess: {guess}")
            
    if len(incorrect_guesses) == max_attempts:
        print(f"Sorry, you've run out of attempts. The word was: {word}")

play_hangman()