#!/usr/bin/env python3
import re
import random


def play():
    words = ['oleg', 'tinkoff']

    word = random.choice(words)
    attempts = 5
    num_missed = 0
    gessed_letters = ''

    while num_missed < 5:
        letter = input('Guess a letter:\n')
        if letter in word:
            gessed_letters += letter
            cripted_word = re.sub(f'[^{gessed_letters}]', '*', word)
            print(f'Hit!\n' +
                  f'The word: {cripted_word}\n\n')
            if cripted_word == word:
                print('You win!')
                return

        else:
            num_missed += 1
            cripted_word = re.sub(f'[^{gessed_letters}]', '*', word) if gessed_letters else '*'*len(word)
            print(f'Missed, mistake {num_missed} out of {attempts}.\n\n' +
                  f'The word: {cripted_word}\n')

    print('You lost!')
    return


if __name__ == "__main__":
    play()
