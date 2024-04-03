""""
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает
его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.

Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения,
разделённые пробелом, последней строкой в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику
и одной строкой со средними оценками по трём предметам.


Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667
"""

with open('dataset_3363_4.txt') as file:  # Открываем файл
    text = file.readlines()  # Считываем весь текст
    average_value, subjects = [], {'math': [], 'physics': [], 'russian': []}
    for line in text:
        cnt = 0
        i = line.find(';')
        lst = list(line[i + 1:-1].split(';'))
        average_value.append((float(lst[0]) + float(lst[1]) + float(lst[2])) / 3)
        for key in subjects.keys():
            subjects[key].append(float(lst[cnt]))
            cnt += 1
    avg_math = sum(subjects['math']) / len(subjects['math'])
    avg_physics = sum(subjects['physics']) / len(subjects['physics'])
    avg_russian = sum(subjects['russian']) / len(subjects['russian'])
    for i in average_value:
        print(i)
    print(avg_math, avg_physics, avg_russian)


