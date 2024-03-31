"""
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
"""

with open('dataset_3363_3.txt') as file:    # Открываем файл
    text = file.readlines()     # Считываем весь текст
    words_dict = {}     # Создаем словарь
    for line in text:   # Итерируемся по строкам из текста
        for word in list(line.split(' ')):      # Итерируемся по словам из строк
            if word.replace('\n', '').lower() in words_dict:    # Если слово в словаре, увеличиваем значение
                words_dict[word.replace('\n', '').lower()] += 1
            else:
                words_dict[word.replace('\n', '').lower()] = 1      # Иначе добавляем слово как ключ со значением один
    max_value = max(words_dict.values())    # Ищем максимальное значение словаря
    final_dict = {key: value for key, value in words_dict.items() if value == max_value}    # Формируем новый словарь с максимальными значениями
    print(final_dict)

