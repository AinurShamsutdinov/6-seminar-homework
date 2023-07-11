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
    low, high, tries = (int(i) for i in input('Enter lower end, higher end, amount of tries: ').split(' '))
    guess_number(low, high, tries)
