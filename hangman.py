'''
- pick a word
- map out the length of characters and print out blank spaces for them
- take 1 character input from the player and if it matches character for word input character in blank space
- 5 lives and if input from player doesn't match character from word take away 1 life
'''
import random

words = ['amazon', 'facebook', 'twitter', 'instagram', 'table', 'python', 'tarantula', 'house']
word_list = []
word_to_play = words[random.randint(0, len(words) - 1)]
letters_played = []
lives = 5

def pick_a_word():
    global words, word_list

    for i in word_to_play:
        word_list.append(i)
    for x in range(len(word_list)):
        word_list[x] = '_'
    print(word_list)
    print(word_to_play)

def guess_letter():
    global lives, word_to_play
    while '_' in word_list:
        letter_guess = input("Guess a letter: ")
        if letter_guess in word_to_play and letter_guess not in letters_played:
            indices = [i for i, a in enumerate(word_to_play) if a == letter_guess]
            for x in indices:
                word_list[x] = letter_guess
                letters_played.append(letter_guess)
            print(word_list)
        elif letter_guess not in word_to_play and letter_guess not in letters_played:
            letters_played.append(letter_guess)
            lives = lives - 1
            print('You have ' + str(lives) + ' lives left')
            if lives == 0:
                print('You lose :(')
                play_again()
        elif letter_guess in letters_played:
            print("letter already used")
            continue
    print('Well done you guessed the word with ' + str(lives) + ' lives left')
    play_again()

def play_again():
    global word_list, letters_played, lives, words, word_to_play
    ask = input('Play again? (y/n)')
    if ask == 'y':
        word_list = []
        letters_played = []
        lives = 5
        word_to_play = words[random.randint(0, len(words) - 1)]
    pick_a_word()
    guess_letter()

pick_a_word()
guess_letter()