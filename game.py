from art import hangman_art
from clear_screen import clear_screen

class game():
  def __init__(self, word) -> None:
    self.word = word
    self.guessed = set()
    self.lives = len(hangman_art) - 1

  def display(self):
    clear_screen()
    self.display_lives()
    self.display_word_progress()
    self.display_guessed_letters()

  def display_lives(self):
    print(hangman_art[len(hangman_art) - self.lives - 1])
    print(f"Levens: {self.lives}")

  def display_guessed_letters(self):
    print(f"Geraden letters: {', '.join(sorted(self.guessed))}")
  
  def display_word_progress(self):
    print("Woord: ", end="")
    for letter in self.word:
      if letter in self.guessed:
        print(letter, end="")
      else:
        print("_", end="")
    print()
  
  def guess(self, letter):
    self.guessed.add(letter)
    if letter not in self.word:
      self.lives -= 1

  def is_game_over(self):
    if self.lives == 0:
      clear_screen()
      self.display_lives()
      print("Je hebt verloren!")
      print(f"Het woord was: {self.word}")
      return True
    for letter in self.word:
      if letter not in self.guessed:
        return False
    clear_screen()
    print("Je hebt gewonnen!")
    return True
  
  def do_game_cycle(self):
    self.display()
    while True:
      letter = input("Raad een letter: ").lower()
      if len(letter) == 1 and letter.isalpha() and letter not in self.guessed:
        break
      else:
        print("Kan niet. Vul één letter in die je nog niet geraden hebt.")
    self.guess(letter)
    return self.is_game_over()
  
def play_game(word):
  game_instance = game(word)
  while not game_instance.do_game_cycle():
    pass