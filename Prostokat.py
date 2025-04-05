class Prostokat():
    bok1 = 0
    bok2 = 0
    poleProsto = 0
    obwodProsto = 0

    def __init__ (self,bok1,bok2):
        self.bok1 = bok1
        self.bok2 = bok2
        self.poleProsto = bok1*bok2
        self.obwodProsto = bok1 +bok1 + bok2+bok2
    def wysPole(self):
        print(f'Pole prostokąta to {self.poleProsto}')

    def wysObwod(self):
        print(f'Obwód prostokąta to {self.obwodProsto}')

prostokat1 = Prostokat(6,6)

prostokat1.wysPole()
prostokat1.wysObwod()

class Kwadrat():
    bok1 = 0
    bok2 = 0
    poleKwad = 0
    obwodKwad = 0

    def __init__(self,bok1,bok2):
        self.bok1 = bok1
        self.bok2 = bok2
        self.poleKwad = bok1*bok2
        self.obwodKwad = bok1+bok1+bok2+bok2
    
    def wysPol(self):
        print(f'Pole kwadrata to {self.poleKwad}')

    def wysObw(self):
        print(f'Obwód kwadrata to {self.obwodKwad}')

kwadrat1 = Kwadrat(7,7)

kwadrat1.wysObw()
kwadrat1.wysPol()