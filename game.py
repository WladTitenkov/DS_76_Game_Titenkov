import numpy as np

min_, max_ = 1, 101  # задаем границы загаданного числа


def random_predict(number=1):
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(min_, max_)
        if number == predict_number:
            break  # выход из цикла, если угадали
    return count


def titenkov_predict(number=1):
    mn, mx = min_, max_  # задаем локальные переменные верхней и нижней границ
    count = 0
    while True:
        count += 1
        # выбираем число из середины возможного диапазона
        predict_number = int((mx + mn) / 2)
        if predict_number == number:
            break  # угадали - выходим из цикла
        elif predict_number < number:
            mn = predict_number
            # меняем нижнюю границу на выбранное число
        elif predict_number > number:
            mx = predict_number
            # меняем верхнюю границу на выбранное число
    return count


def score_game(predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    # np.random.seed(np.random.randint(1,100))  # создаем рандомный сид для проверок
    np.random.seed(1)  # фиксируем сид для вопроизводимости
    random_array = np.random.randint(
        min_, max_, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток
    return(score)


if __name__ == '__main__':
    # score_game(random_predict)
    print(
        f'Рандомный алгоритм угадывает число в среднем за {score_game(random_predict)} попыток')
    print(
        f'Алгоритм "titenkov" угадывает число в среднем за {score_game(titenkov_predict)} попыток')
