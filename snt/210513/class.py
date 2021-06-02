from random import randint

class Voiture:
    def __init__(self, nom='auto'):
        """
        This __init__ methos is automaticly called at instance creation
        """
        self.nom = nom
        self.gaz = 15

    def show(self):
        print(f"I'm a car, my name is {self.nom:12} my tank has {self.gaz} litres")

    def run(self, distance=1):
        """
        If there is no more gaz car will not be able to run
        """
        # print(f'je roule de {distance} km')
        if distance > self.gaz:
            print('je n\'ai pas assez d\'essence, recharge moi')
        else:
            self.gaz = self.gaz - distance
            print(f' .... je roule de {distance} km, il me reste: {self.gaz}')

cars = [Voiture(f'auto_{i}') for i in range(6)]

for car in cars:
    car.run(randint(1, 5))
    car.show()

cc = Voiture(nom='Mario')
cc.run(21)


print(cc.nom, cc.gaz)

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

