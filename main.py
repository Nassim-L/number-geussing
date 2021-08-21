import random
import os
from logo import logo

# difficulty_lvl
difficulty = {"easy": 10,
              "hard": 5}

# random number chose


def choserandomnumber():
    numbers_list = [x for x in range(0, 101)]
    return random.choice(numbers_list)


def guessing(y, x):
    if y > x:
        print(f'my number is less then {y}')
        return 0

    elif y < x:
        print(f'my number is great then {y}')
        return 0

    elif x == y:
        print("You win")
        return 1


def game():
    print(logo)
    x = choserandomnumber()

    d = input('Easy or Hard: ').lower()
    lifes = difficulty[d]
    game_is_over = False

    while not game_is_over:
        y = int(input('give me a number beetwin 0 and 100: '))

        n = guessing(y, x)

        if n == 0:
            lifes -= 1
            print('you have', lifes, 'left')

        if lifes == 0:
            print('you lose My number is', x)

        if lifes == 0 or n == 1:
            w = input('type ''Y'' play again, or "N" to end this game')

            if w == "y":
                os.system('clear')
                game()

            else:
                game_is_over = True


game()
