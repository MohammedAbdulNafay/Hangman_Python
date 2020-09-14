import random
import resources

guessed = []
underscore = "_"
lost = 'LOST'
won = 'WON'
game_on = 'GAME ON'

# read the words from the document words.txt
with open('words.txt') as words:
    word_list = words.read().upper().splitlines()

# shuffle the list of words so that it will be randomly selected at first
random.shuffle(word_list)

# word to guess
word = word_list.pop()

# list variables to track correct and incorrect letters guessed to decide win/lose
correct = []
incorrect = []


###
# Function to draw the UI
# It will eventually draw the Gallows and display the word
###
def draw_board():
    print(resources.hangman_board[len(incorrect)])

    for letter in word:
        if letter in correct:
            print(letter, end='  ')
        else:
            print(underscore, end='  ')

    print("\n\n")


####
# Allow the user to input single letter as a guess
#
def input_letter():
    while True:
        input_letter = input("Enter a letter: ").upper()

        if input_letter.isnumeric():
            print("Please enter only letters, not numbers")
        elif len(input_letter) == 0:
            print("Please enter your selection")
        elif len(input_letter) > 1:
            print("Please enter only a single letter")
        else:
            return input_letter


###
# Check to see if a letter has been guessed already
#
def check_letter(letter_guessed):
    if letter_guessed in guessed:
        print("You have already guessed the letter: %s " % letter_guessed)
    else:
        print("You have guessed the letter: %s " % letter_guessed)
        guessed.append(letter_guessed)
        if letter_guessed in word:
            correct.append(letter_guessed)
            print("You have guessed CORRECTLY")
        else:
            incorrect.append(letter_guessed)
            print("You have guessed INCORRECTLY")

###
#  Check to see if the user has won the game
###
def check_win():
    if len(incorrect) > 5:
        return lost

    for letter in word:
        if letter not in correct:
            return game_on

    return won


while True:
    print("****************************************")
    print("You have guessed the following letters: ")
    print("CORRECT LETTERS    : ")
    for letter in correct:
        print(letter, end="  ")

    print("\nINCORRECT LETTERS  : ")
    for letter in incorrect:
        print(letter, end="  ")
    print("\n***************************************")

    draw_board()
    guessed_letter = input_letter()
    check_letter(guessed_letter)
    win_condition = check_win()

    if win_condition == lost:
        print('GAME OVER! THE WORD WAS ***** %s *****' % word)
        print(resources.hangman_board[6])
        break
    elif win_condition == won:
        print('YOU WON! THE WORD WAS ***** %s *****' % word)
        break

    response = input("Press <ENTER> to Continue, <Q> to Quit: ").upper()

    if response == "Q":
        print('YOU QUIT! THE WORD WAS ***** %s *****' % word)
        break
