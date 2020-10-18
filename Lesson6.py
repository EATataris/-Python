import time

#1
class TrafficLight():
    __color = ['red', 'yellow', 'green']

    def running(self):
        for i in self.__color:
            print(i)
            if i == 'red':
                time.sleep(7)
            elif i == 'yellow':
                time.sleep(2)
            else:
                time.sleep(10)

lights = TrafficLight()
lights.running()

#2
class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_weight(self):
        weight_one_sm = 25
        road_thickness = 5
        return self._length * self._width * weight_one_sm * road_thickness / 1000

road = Road(20, 5000)
road_2 = Road(30, 1000)
print(road.road_weight(), 'т')
print(road_2.road_weight(), 'т')

#3
class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


Andrew = Position('Anfrew', 'Besos', 'Top manager', 20000, 15000)
print(Andrew.get_full_name())
print(Andrew.get_total_income())

#4
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f'Текущая скорость авто {self.speed} км/ч'

    def go(self):
        return f'Машина поехала!'

    def stop(self):
        return f'Машина остановилась'

    def turn(self, direction):
        return f'Машина повернула на {direction}'

class TownCar(Car):
    def definition(self):
        return 'Городская машина'
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости!!'
        else:
            return f'Текущая скорость авто {self.speed} км/ч'

class SportCar(Car):
    def definition(self):
        return 'Спортивная машина'

class WorkCar(Car):
    def definition(self):
        return 'Рабочая машина'
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости!!'
        else:
            return f'Текущая скорость авто {self.speed} км/ч'

class PoliceCar(Car):
    def definition(self):
        return 'Полицейская машина'


town_car = TownCar(60, 'blue', 'Honda', False)
police_car = PoliceCar(300, 'white', 'Ferrari', True)
sport_car = SportCar(350, 'yellow', 'Lamborghini', False)
work_car = WorkCar(50, 'black', 'Lada', False)
print(town_car.show_speed())
print(town_car.definition())
print(town_car.color)
print(town_car.name)
print(town_car.is_police)
print(town_car.turn('лево'))
print(work_car.show_speed())

#5
class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Рисую ручкой. Не очень красиво'

class Pencil(Stationery):
    def draw(self):
        return f'Рисую карандашом. Получается эскиз'

class Handle(Stationery):
    def draw(self):
        return f'Все закрашу маркером!!'


pen = Pen('Гелевая ручка')
pencil = Pencil('Графитовый карандащ')
handle = Handle('Жирный маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())