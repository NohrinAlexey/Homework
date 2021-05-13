summa = 0
new_summa = 0
list_cube = [i ** 3 for i in range(1, 1001, 2)] #Создаём список кубов чисел из диапазона 1-1000
for value in list_cube: #Перебираем список
    i = str(value) #Переводим значение числа в строку для дальнейшего перебора цифр
    for digit in i: #Перебираем каждую цифру в числе
        summa += int(digit) #Суммируем все цифры в числе
        if summa % 7 == 0: #Выбираем только те, которые делятся на 7
            print(summa) #Выводим список
for value in list_cube:
    value += 17
    i = str(value)
    for digit in i:
        new_summa += int(digit)
        if new_summa % 7 == 0:
            print('Сумма +17', new_summa)
