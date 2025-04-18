class Trojkat:
    bok1 = 0
    bok2 = 0
    bok3 = 0
    wysokosc = 0
    Pole_Troj = 0
    Obwod_Troj =  0
    
    def __init__(self,bok1,bok2,bok3, wysokosc):
        self.bok1 = bok1
        self.bok2 = bok2
        self.bok3 = bok3
        self.wysokosc = wysokosc
        self.Pole_Troj = bok1*wysokosc/2
        self.Obwod_Troj = bok1+bok2+bok3
        
    def wysPole(self):
        print(f'Pole trojkata to {self.Pole_Troj}')

    def wysObwod(self):
        print(f'Obwod trojkata to {self.Obwod_Troj}')

trojkat1 = Trojkat(9,9,9,9)

trojkat1.wysObwod()
trojkat1.wysPole()
class Prostopadloscian():
    