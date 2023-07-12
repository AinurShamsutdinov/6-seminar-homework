# hw 2
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
# ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# hw 3
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в
# задаче выше. Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

import random


def check_places(coordinates):
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j:
                if coordinates[i][0] == coordinates[j][0] or coordinates[i][1] == coordinates[j][1]:
                    return False
                elif coordinates[i][0] == coordinates[j][0] and coordinates[i][1] == coordinates[j][1]:
                    return False
                elif abs(coordinates[i][0] - coordinates[j][0]) == abs(coordinates[i][1] - coordinates[j][1]):
                    return False
    return True


def random_generator():
    count = 4
    generated: list = list()
    while count > 0:
        pairs = generate_pairs_8()
        if check_places(pairs):
            count -= 1
            generated.append(pairs)
    return generated


def generate_pairs_8():
    random_list: list = list()
    for i in range(8):
        random_list.append(generate_pair())
    return random_list


def generate_pair():
    first_num = random.randint(1, 8)
    second_num = random.randint(1, 8)
    return first_num, second_num


should_be_true = ((1, 2), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 7), (8, 5))
should_be_false = ((1, 2), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 4), (8, 5))
print('Test queens do not cross 1:\t', check_places(should_be_true), '\n')
print('Test queens cross 2:\t', check_places(should_be_false), '\n')

generated_pairs_4 = random_generator()
for item in generated_pairs_4:
    print(f'Random generated is cool:\t', check_places(item), item)

#
# Random generated a cool:	 True [(1, 6), (2, 2), (5, 4), (8, 3), (7, 5), (6, 8), (3, 7), (4, 1)]
# Random generated a cool:	 True [(2, 2), (4, 5), (8, 6), (7, 3), (5, 7), (3, 8), (6, 1), (1, 4)]
# Random generated a cool:	 True [(8, 3), (6, 8), (4, 4), (7, 6), (2, 5), (1, 2), (5, 1), (3, 7)]
# Random generated a cool:	 True [(8, 5), (4, 4), (5, 1), (1, 6), (6, 8), (2, 3), (3, 7), (7, 2)]
