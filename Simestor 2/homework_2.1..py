import random  # импортируем библиотеку random для заполнения массива случайными числами


def fill(value):  # создаем функцию с циклом для заполнения массива
    mas_ = []  # локальная переменная - массив
    for i in range(value):  # цикл действующий в диапазоне value
        mas_.append(random.randint(0, value))  # добавляем в конец массива случайное число от 0 до n

    return mas_  # вернем значение mas - заполненный случайными числами массив


mas = fill(10)  # заполним массив mas функцией fill с параметром 10


def sorting(mas_):  # функция сортировки массива, простым выбором

    for i in range(len(mas_)):  # цикл действующий в диапазоне длинны массива mas_
        if mas_[i] % 2 == 0:  # добавим условие: если элемент массива i делится без остатка на 2, то выполним дальнейшие действия
            for j in range(len(mas_)):  # добавим вложенный цикл действующий в диапазоне длинны массива mas_
                if i != j and mas_[j] % 2 == 0:  # если выбранные элементы i и j не одинаковы и элемент массива j четный, то:
                    if mas_[i] < mas_[j]:  # сравниваем элементы i и j
                        mas_[i], mas_[j] = mas_[j], mas_[i]  # если элемент i меньше элемента j, то меняем местами

    return mas_  # вернем отсортированный массив


print("\033[32m {}".format(mas)+' - исходный массив')  # выведем заполненный случайными числами массив
print("\033[31m {}".format(sorting(mas))+' - отсортированный массив')  # выведем отсортированный массив
