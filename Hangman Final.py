import random
def select_word():
    words = ["apple", "banana", "cherry", "date"]
    return random.choice(words)
def play_game(word):
    guessed_letters = set()
    attempts = 0
    max_attempts = 7
    word_set = set(word)

    while len(guessed_letters) < len(word_set) and attempts < max_attempts:
        guess = input("Guess a letter: ")
        if guess in word_set:
            guessed_letters.add(guess)
            print(" ".join([c if c in guessed_letters else "_" for c in word]))
        else:
            attempts += 1
            print(" ".join(["Hangman"[i] for i in range (attempts)]))
    if len(guessed_letters) == len(word_set):
        print("congratulations! You guessed the word:", word)
    else:
        print("sorry, you run out of attempts. The word was:", word)
selected_word = select_word()
play_game(selected_word)