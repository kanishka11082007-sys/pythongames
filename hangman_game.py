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
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


def getwords():
    try:
        with open('words.txt', 'r') as f:
            word_list = f.read().splitlines()
        return random.choice(word_list)
    except FileNotFoundError:
        print("file not found!!")


def hangman():
    chosen_word = getwords()
    display = ["_"]*len(chosen_word)
    gussedletter = set()
    endofloop = False
    lives = 6

    print("\n---------- Welcome To Hangman Game ----------\n")
    print("You have to guess: ", ' '.join(display))
    print(f"You have {lives} lives")
    while not endofloop:
        guess = input("Guess a letter: ").lower()
        if guess in gussedletter:
            print("already guesses try another letter")
        else:
            gussedletter.add(guess)
        if guess in chosen_word:
            for index, char in enumerate(chosen_word):
                if guess == char:
                    display[index] = guess
            print(' '.join(display))
        if guess not in chosen_word:
            print(stages[lives])
            lives = lives-1
            print("remaining lives: ", lives)
        if lives == 0:
            print("you lose!!")
            print("The word was", chosen_word)
            endofloop = True
        if '_' not in display:
            print("You won")
            endofloop = True


while True:
    ask = input("Do you want to play Hangman(y/n): ")
    if ask.lower() in 'y':
        hangman()
    elif ask.lower() in 'n':
        print("program exited successfully")
    else:
        print("error encountered!(enter valid choice)")
