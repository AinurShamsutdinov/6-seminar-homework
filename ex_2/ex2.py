from random import randint as rand


def guess_number(low, high, tries):
    guess = rand(low, high)
    input_num: int = int()
    for i in range(tries):
        input_num = int(input('Enter number: '))
        if guess == input_num:
            print('You won!')
            break
        elif input_num > guess:
            print('Lower!')
        elif input_num < guess:
            print('Higher!')
    if input_num != guess:
        print('You lost.')


if __name__ == '__main__':
    low_end = int(input('Enter lower end: '))
    high_end = int(input('Enter higher end: '))
    tries = int(input('Enter amount of tries: '))
    guess_number(low_end, high_end, tries)
