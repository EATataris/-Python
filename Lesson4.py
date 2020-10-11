#1 Не хотел в отдельный файл переность. Можете закомментировать остальной код, проверить первое задание,
# а затем закоментировать первое и остальные проверять
from sys import argv

script_name, working_hours, salary_per_hour, bonus = argv
salary = (int(working_hours) * int(salary_per_hour)) + int(bonus)

print(salary)

#2
first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
second_list = [j for i, j in zip(first_list, first_list[1:]) if j > i]
print(second_list)

#3
list_range = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(list_range)

#4
list_a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_b = [i for i in list_a if list_a.count(i) == 1]
print(list_b)

#5
from functools import reduce

list_reduce = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda x, y: x * y, list_reduce))

#6
from itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

some_list = [1, 2, 3]
c = 0
for i in cycle(some_list):
    if c > 5:
        break
    else:
        print(i)
    c += 1

#7
def fact(n):
    factorial = 1
    for i in range(2, n + 2):
        yield factorial
        factorial *= i

for el in fact(4):
    print(el)


