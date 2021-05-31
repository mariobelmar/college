from random import randint

class Voiture:
    def __init__(self, nom='auto'):
        self.nom = nom
        self.gaz = 15
    def show(self):
        print(f"I'm a car, my name is {self.nom:12} my tank has {15} litres")
    def run(self, distance=1):
        # print(f'je roule de {distance} km')
        self.gaz = self.gaz - distance
        print(f' .... je roule de {distance} km, il me reste: {self.gaz}')

cars = [Voiture(f'auto_{i}') for i in range(6)]

for car in cars:
    car.run(randint(1, 5))
    car.show()

#  .... je roule de 1 km, il me reste: 11
# I'm a car, my name is auto_0       my tank has 11 litres
#  .... je roule de 5 km, il me reste: 7
# I'm a car, my name is auto_1       my tank has 7 litres
#  .... je roule de 3 km, il me reste: 9
# I'm a car, my name is auto_2       my tank has 9 litres
#  .... je roule de 1 km, il me reste: 10
# I'm a car, my name is auto_3       my tank has 10 litres
#  .... je roule de 1 km, il me reste: 10
# I'm a car, my name is auto_4       my tank has 10 litres
#  .... je roule de 2 km, il me reste: 11
# I'm a car, my name is auto_5       my tank has 11 litres

