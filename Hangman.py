import random
import resources

# read the words from the document words.txt
with open('words.txt') as words:
    word_list = words.read().upper().splitlines()

underscore = '_'
lost = 'LOST'
won = 'WON'
game_on = 'GAME ON'

# shuffle the list of words so that it will be randomly selected at first
random.shuffle(word_list)

# word to guess
secret_word = word_list.pop()

# list variables to track correct and incorrect letters guessed to decide win/lose
correct = []
incorrect = []


###
# Function to draw the UI
# It will eventually draw the Gallows and display the word
###
def draw_board():
    print(resources.hangman_board[len(incorrect)])

    for letter in secret_word:
        if letter in correct:
            print(letter, end='  ')
        else:
            print(underscore, end='  ')

    print("\n\n")

    # Displaying missed letters
    print("******* Missed Letters *******")

    for missed_letter in incorrect:
        print(missed_letter, end='  ')

    print("\n******************************\n")


###
# Allow the users to take a guess
# Append the letter to correct or incorrect.
###
def user_guess():
    while True:
        guessed_letter = input("Guess a letter. \n: ").upper()

        if len(guessed_letter) == 0:
            print("Please enter your selection.")
        elif len(guessed_letter) > 1:
            print("Please enter only one letter at a time. Guess again.")
        elif guessed_letter.isnumeric():
            print("Please enter only letters, not numbers. Guess again. ")
        elif guessed_letter in correct:
            print("You have already guessed that letter. Guess again.")
        elif guessed_letter in incorrect:
            print("You have guessed the wrong letter. Guess again.")
        else:
            break;

    if guessed_letter in secret_word:
        correct.append(guessed_letter)
    else:
        incorrect.append(guessed_letter)


###
#  Check to see if the user has won the game
###
def check_win():
    if len(incorrect) > 5:
        return lost

    for letter in secret_word:
        if letter not in correct:
            return game_on

    return won


while True:
    draw_board()
    user_guess()
    win_condition = check_win()

    if win_condition == lost:
        print('GAME OVER! THE WORD WAS ***** %s *****' % secret_word)
        print(resources.hangman_board[6])
        break
    elif win_condition == won:
        print('YOU WON! THE WORD WAS ***** %s *****' % secret_word)
        break
