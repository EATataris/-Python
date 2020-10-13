#1
with open('lesson5.txt', 'w') as f_obj:
    while True:
        string_txt = input('Введите строку: ')
        if string_txt != '':
            f_obj.write(string_txt + '\n')
        else:
            break

#2
with open('lesson52.txt') as read_f:
    str_num = 0
    words_num = 0
    for line in read_f:
        str_num += 1
        print(f'в {str_num} строке {len(line.split())} слов ')
    print(f'колво строк - {str_num}')

#3
with open('workers.txt') as read_workers:
    salary = 0
    workers_num = 0
    for line in read_workers:
        workers_num += 1
        salary += int(line.split()[1])
        if int(line.split()[1]) < 20000:
            print(f'Оклад ментьше 20тыс. у {line.split()[0]}')
    print(f'средняя величина дохода сотрудников {salary / workers_num}')

#4
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('numbers.txt', 'r') as read_num, open('numbers_rus.txt', 'w', encoding='UTF-8') as write_num:
    a = read_num.readlines()
    b = [i.split() for i in a]
    c = []
    for i in b:
        for k, v in translate.items():
            if i[0] == k:
                i[0] = v
        c.append(' '.join(i) + '\n')
    write_num.writelines(c)

#5
with open('digits.txt', 'w') as digits:
    digits_str = input('Ввелите числа через пробел: ')
    digits.write(digits_str)
with open('digits.txt') as digits:
    res = []
    for i in digits.read().split():
        res.append(int(i))
    print(sum(res))