number_in_english = input('Введите число от 0 до 10 на английском ')


def num_translate_adv(num):

    """ Функция возвращает перевод на русский введенного названия числа на английском
    Если название введено с заглавной буквы, то и результат будет выведен с залавной буквы

    :parameter (str) Название числа на английском от 0 до 10. Например ten, one и т.д.
    """

    nums = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    result = ''
    if num.istitle(): # Проверка ввода на первую заглавную букву
        num = num.lower()
        result = nums[num].title() # Если ввод с заглавной, то результат преобразуем в title
    else:
         result = nums[num]
    return result


print(num_translate_adv(number_in_english))