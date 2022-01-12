'''Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать» подразумевается «написать программу, которая угадывает число».
Алгоритм учитывает информацию о том, больше ли или меньше случайное число нужного нам числа.'''


import numpy as np

min_, max_ = 1, 101


def random_predict(number = 1):
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(min_, max_)
        if number == predict_number:
            break  # выход из цикла, если угадали
    return count


def titenkov_predict(number = 1):
    mn, mx = min_, max_
    count = 0
    print(mn , mx)
    while True:
        count += 1
        predict_number = int((mx + mn) / 2) #выбираем число из середины возможного диапазона
        print(predict_number)
        print(number)
        if predict_number == number:
            break # угадали - выходим из цикла
        elif predict_number < number: 
            mn = predict_number
        elif predict_number > number:
            mx = predict_number    
    return count           


# print(f"Количество попыток: {random_predict()}")


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    # np.random.seed(np.random.randint(1,100))  # создаем рандомный сид для проверок
    np.random.randint(1,100) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    # print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    # score_game(random_predict)
    # print(f'Ваш алгоритм угадывает число в среднем за {score_game(random_predict)} попыток')
    print(f'Ваш алгоритм угадывает число в среднем за {score_game(titenkov_predict)} попыток')
