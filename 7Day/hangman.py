import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word: str = random.choice(word_list)
word_len = len(chosen_word)

print(chosen_word)

correct_letters = []
game_over = False
placeholder = ""
for i in range(word_len):
    placeholder += '_'

print(placeholder)

while not game_over:
    print(stages[lives])

    guess = input("\nInsert a letter you think might be part of the word: ").lower()
    while len(guess) > 1:
        guess = input("\nInput too big! Try again, one letter at a time: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            gave_over = True
            print("YOU LOSE!!!")

    if '_' not in display:
        print("YOU WON!!!")
        game_over = True

    print(lives)
