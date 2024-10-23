from game import play_game
def configure_word():
    word = ""
    while not word:
        temp = input("Vul een woord in om te raden: ").strip()
        if temp.isalpha():
            word = temp
            return word
        else:
            print("Je woord mag alleen letters hebben!")

if __name__ == "__main__":
    print("Welkom bij galgje!")
    print("Raad het woord voordat je levens op zijn.")
    input("Druk op enter om te beginnen...")
    while True:
        word_to_guess = configure_word()
        play_game(word_to_guess)
        if input("Wil je nog een keer spelen (j/n): ").lower() != "j":
            break