import time

#1
# class TrafficLight():
#     __color = ['red', 'yellow', 'green']
#
#     def running(self):
#         for i in self.__color:
#             print(i)
#             if i == 'red':
#                 time.sleep(7)
#             elif i == 'yellow':
#                 time.sleep(2)
#             else:
#                 time.sleep(10)
#
# lights = TrafficLight()
# lights.running()

#2
class Road():
    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width

    def road_weiht(self):
        weight_one_sm = 25
        road_thickness = 5
        return self.length * self.width * weight_one_sm * road_thickness / 1000

road = Road(20, 5000)
road_2 = Road(30, 1000)
print(road.road_weiht(), 'т')
print(road_2.road_weiht(), 'т')