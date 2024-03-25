with open('dataset_3363_2.txt') as f:
    lst = list(f.readline().strip())    #Конвертируем строку в список
    str_value, int_value, f = [], [], ''    #Обьявляем два списка для str и int значений и строку в которую будем складывать значения
    while len(lst) != 0:    #Запускаем цикл, пока не вырежем все значения из начального списка
        if lst[0].isdigit():    #Всегда проверяем только первое значение на тип int
            if len(lst) > 1 and lst[1].isdigit():   #Проверка на index out of range и на число из двух символов
                int_value.append(lst[0] + lst[1])   #Добавляем число из двух символов в список для чисел
                lst.pop(0), lst.pop(0)  #Вырезаем два символа
            else:
                int_value.append(lst[0])    #Просто добавляем одно число в список для чисел
                lst.pop(0)  #Вырезаем число
        else:   #Если значение str
            str_value.append(lst[0])    #Добавляем str в cписок для букв
            lst.pop(0)  #Вырезаем str из исходного списка
    for i in range(len(str_value)):     #Запускаем цикл по длине списка
        f += str_value[i] * int(int_value[i])   #Перемножаем значения из списков и добавляем их к строке