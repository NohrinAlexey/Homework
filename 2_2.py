

some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

index = 0
lenght_list=len(some_list)
for i in range(lenght_list):
    prefix = ''
    item_of_list = some_list[index]
    if item_of_list.find('+')!=-1:
        prefix,item_of_list = item_of_list[0],item_of_list[1]
        print(item_of_list)
    if item_of_list.isdigit():
        num = int(item_of_list)
        some_list[index] = '{}{:02d}'.format(prefix,num)
        some_list.insert(index,'"')
        some_list.insert(index + 2,'"')
        index += 3
    else:
        index += 1

sting_from_some_list = " ".join(some_list)
print(sting_from_some_list)

# Александр, привет. Я понимаю что этот код почти полностью совпадает с твоим решением задачи, которое было разобрано на третьем уроке.
# И после того как я увидел это решение, то никакие другие способы решения в голову не шли.
# В следующий раз не буду смотреть разбор решения задач до того, пока сам не сделаю.
# Я попытался внести в решение какие-то свои варианты. Частично у меня получилось.
# Почти каждая строка этого кода мной осмыслена и много раз была проверена в дебаггере, чтобы понять как это работает)
# Остальные задания 2 урока сделаны полностью мной с нуля с помощью гугла и какой-то матери)
