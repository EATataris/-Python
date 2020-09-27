#1
a = 1
b = 'hello'
print(a, b)
c = input('введите переменную c:')
d = input('введите переменную d:')
print(c, d)
#2
time = int(input('введите время в секундах:'))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) - minutes * 60
print(f'{hours}:{minutes}:{seconds}')
#3
num = input('введите число')
sum = int(num) + int(2 * num) + int(3 * num)
print(sum)
#4
some_num = int(input('введите положительное число:'))
max_num = some_num % 10
some_num = some_num // 10
while some_num > 0:
    if some_num % 10 > max_num:
        max_num = some_num % 10
    some_num = some_num // 10
print(max_num)
#5
proceeds = float(input('введите значение выручки: '))
costs = float(input('введите значение издержек: '))
if proceeds > costs:
    print('Фирма прибыльна!')
    profit = proceeds / (proceeds - costs)
    workers = int(input('Введите количество сотрудников'))
    profit_per_worker = profit / workers
    print(profit)
    print(profit_per_worker)
elif proceeds < costs:
    print('Фирма убыточна!')
else:
    print('Фирма работает в ноль')
#6
first_result = 2
final_result = 4
day = 1
while first_result < final_result:
    print(f'{day}-ый день: {first_result}')
    first_result = first_result + first_result * 0.1
    day += 1
else:
    print(f'{day}-ый день: {first_result}')
    first_result = first_result + first_result * 0.1
    print(f'Ответ: на {day}-ый день спорсмен достиг результата - не менее {final_result} км')
    day += 1