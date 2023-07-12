# Задание №4
# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

__riddle_answers__: dict = dict()

def solve_riddle(riddle: str, solutions: list, tries: int=5):
    answer: str = str()
    print(f'Riddle: \n{riddle}')
    for i in range(tries):
        answer = input('Enter the answer: ')
        if answer in solutions:
            return i + 1
    return 0


# Задание №5
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

def vault():
    solutions: dict = {'riddle riddle riddle riddle riddle ridle': ['answer', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8', 'answer9'],
                       'riddle riddle riddle riddle riddle': ['answer', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8'],
                       'riddle riddle riddle riddle': ['answer', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7'],
                       'riddle riddle riddle': ['answer', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6'],
                       'riddle riddle': ['answer', 'answer2', 'answer3', 'answer4', 'answer5'],
                       'riddle': ['answer', 'answer2', 'answer3', 'answer4']}
    for key, value in solutions.items():
        solve_riddle(key, value)


# # Задание №6
# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


def form_report(riddle: str, tries: int):
    __riddle_answers__[riddle] = tries


def print_report():
    for riddle, answer in __riddle_answers__.items():
        print(f'Riddle: {riddle}\nAmount of wrong answers: {answer}\n')


def test():
    solutions: dict = {
        'riddle riddle riddle riddle riddle ridle': 3,
        'riddle riddle riddle riddle riddle': 7,
        'riddle riddle riddle riddle': 4,
        'riddle riddle riddle': 8,
        'riddle riddle': 6,
        'riddle': 6
    }
    [form_report(riddle, count) for riddle, count in solutions.items()]
    print_report()


if __name__ == '__main__':
    test()
