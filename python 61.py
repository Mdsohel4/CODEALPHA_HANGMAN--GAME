import random

words = ['python', 'developer', 'hangman', 'internship', 'codealpha']
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman!")

while attempts > 0 and '_' in guessed:
    print("\nWord: " + ' '.join(guessed))
    print("Used letters:", ' '.join(used_letters))
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that.")
        continue

    used_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if '_' not in guessed:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost. The word was:", word)
