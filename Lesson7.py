#1
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] += other.matrix[i][j]
        return self

    def __str__(self):
        return '\n'.join([' '.join([str(j) for j in i]) for i in self.matrix])


mx = Matrix([[1, 2], [3, 4]])
mx_2 = Matrix([[5, 6], [7, 8]])
print(mx)
print(mx_2)
print(mx + mx_2)

#2
class Coat:
    def __init__(self, volume):
        self.cloth = volume / 6.5 + 0.5

class Suit:
    def __init__(self, height):
        self.cloth = 2 * height + 0.3

class Clothes:
    def __init__(self):
        self.cloth = 0
        self.total = []

    def add_coat(self, volume):
        self.total.append(Coat(volume))

    def add_suit(self, height):
        self.total.append(Suit(height))

    def total_consumption(self):
        total = self.cloth
        for i in self.total:
            total += i.cloth
        return total


clothes = Clothes()
clothes.add_coat(10)
clothes.add_coat(10)
clothes.add_suit(5)
clothes.add_suit(5)
print(clothes.total_consumption())