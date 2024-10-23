from game import play_game
def configure_word():
    word = ""
    while not word:
        temp = input("Enter the word to guess: ").strip()
        if temp.isalpha():
            word = temp
            return word
        else:
            print("Word must contain only letters!")

if __name__ == "__main__":
    print("Welcome to Hangman!")
    print("Guess the word before the man hangs!")
    input("Press Enter to start the game...")
    while True:
        word_to_guess = configure_word()
        play_game(word_to_guess)
        if input("Do you want to play again? (y/n): ").lower() != "y":
            break