class Uppgift:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    # def __str__(self):
    #     return f'Uppgift: X={self.X}, Y={self.Y}'
if __name__ == '__main__': 
    min_uppgift = Uppgift(10, 5)
    print(min_uppgift)