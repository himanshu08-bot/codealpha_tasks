import random

# Predefined list of words
words = ["python", "hangman", "coding", "simple", "random"]

# Randomly select a word
word_to_guess = random.choice(words)
guessed_word = ["_"] * len(word_to_guess)

# Keep track of guessed letters and attempts
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("You have 6 incorrect guesses allowed.\n")

# Game loop
while incorrect_guesses < max_incorrect and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print(f"Remaining attempts: {max_incorrect - incorrect_guesses}")
    
    guess = input("Guess a letter: ").lower()
    
    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue
    
    guessed_letters.append(guess)
    
    # Check if guess is correct
    if guess in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
        print("Good guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")

# End of game results
if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Out of attempts! The word was:", word_to_guess)
