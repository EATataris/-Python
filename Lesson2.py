#1
default_list = [1, 'Hello', None, True, [2, 3], {'x': 1, 'y': 2}]
for i in default_list:
    print(f'{i} - {type(i)}')

#2
def split_list(list):
    lists = []
    final_list = []
    while len(list) > 2:
        lists.append(list[:2])
        list = list[2:]
    else:
        lists.append(list[:len(list)])
    for i in lists:
        i.reverse()
        for j in i:
            final_list.append(j)
    return final_list


ls = [1, 2, 3, 4, 5]
print(split_list(ls))

#3
#решение списками
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
try:
    month = int(input('Введите номер месяца: '))
    if month in winter:
        print('Зима')
    elif month in spring:
        print('Весна')
    elif month in summer:
        print('Лето')
    elif month in autumn:
        print('Осень')
    else:
        print('Такого месяца не существует')
except ValueError:
    print('Введите целое число')

#решение словарем
year = {'winter': [1, 2, 12],
        'spring': [3, 4, 5],
        'summer': [6, 7, 8],
        'autumn': [9, 10, 11]}

month = int(input('Введите номер месяца: '))
for k, v in year.items():
    if month in v:
        print(k)

#4
string = input('Введите произвольную строку: ')
string_list = string.split()
for i, j in enumerate(string_list, 1):
    print(i, j[:10])

#5
my_list = [7, 5, 3, 3, 2]
rating = int(input('Веедите новый элемент рейтинга: '))
my_list.append(rating)
sorted_list = [str(i) for i in sorted(my_list, reverse=True)]
print(', '.join(sorted_list))
