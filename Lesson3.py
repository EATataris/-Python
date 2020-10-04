#1
def division(x, y):
    if y == 0:
        print('На ноль делить нельзя!')
    else:
        return x / y

x = float(input('Введите первый аргумент: '))
y = float(input('Введите второй аргумент: '))
print(division(x, y))

#2
def user_data(first_name, last_name, year, city, email, phone):
    print(f'{first_name} {last_name} {year} {city} {email} {phone}')

user_data(first_name='Leonel', last_name='Messi', year='1987', city='Rosario', email='LeoMessi@gmail.com', phone='+79788440982')

#3
def my_func(x, y, z):
    res = []
    res.append(x)
    res.append(y)
    res.append(z)
    res = sorted(res)
    return res[1] + res[2]

print(my_func(100, 400, 3))

#4
#с помощью **
def my_new_func(x, y):
    if x > 0 and y < 0:
        return x ** y
    else:
        print('x - должен быть положительным, а у - отрицательным!')

print(my_new_func(2, -2))

#c помощью цикла
def my_pow(x, y):
    res = 1
    counter = 0
    while counter < -1 * y:
        res = res * x
        counter += 1
    return 1 / res

print(my_pow(2, -2))

#5
def sum_line(str):
    res = []
    for i in str.split():
        res.append(float(i))
    return sum(res)

str = input('Введите числа через пробел: ')
print(sum_line(str))

# 6
def int_func(text):
    return text.capitalize()

def words_capitalize(text):
    res = []
    for i in text.split():
         res.append(int_func(i))
    return ' '.join(res)

print(int_func('text'))
print(words_capitalize('text teext'))