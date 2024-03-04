class Device:
    def __init__(self,name,stranproz):
        self.name=name
        self.stranproz=stranproz
    def info(self):
        print(f'названия дивайса : {self.name}')
        print(f'страна производство :{self.stranproz}')

class CoffeMachine(Device):
    def __init__(self,name,stranproz,coffe,sugar):
        super().__init__(self,name,stranproz)
        self.coffe = coffe
        self.sugar = sugar
    def coffe(self):
        print('информация---------')
        super().info()
        print(f"вы захотели {self.coffe}")
        print(f'вы насыпали {self.sugar} сахара')

class Blender(Device):
    def __init__(self, name,stranproz,speed,):
        super().__init__(self,name,stranproz)
        self.speed=speed
    def blender(self):
        print('информация---------')
        super().info()
        print(f'скорость {self.speed}')
    
class MeatGrinder(Device):
    def __init__(self,name,stranproz,power):
        super().__init__(self,name,stranproz)
        self.power=power
    def meat_grind(self):   
        print('информация---------')
        super().info()
        print(f'мощность {self.power}')
    
blen=Blender('Bork', 'USA','1000W')
blen.blender()




class Ship:
    def __init__(self, name,width,height):
        self.name=name
        self.width=width
        self.height=height
    def  infoo(self):
        print('информация о судне-----------')
        print(f"имя{self.name}")
        print(f'высота{self.height},ширина{self.width}')

class  Frigate(Ship):
    def __init__(self, name, width, height,pushki,chel):
        super().__init__(name, width, height)
        self.pushki = pushki
        self.chel = chel
    def cruise(self):
        print('информация---------')
        super().infoo()
        print(f"количество пушек {self.pushki}")
        print(f'{self.chel} человек на борту')
    
class Destroyer(Ship):
    def __init__(self, name, width, height,che,speed):
        super().__init__(name, width, height)
        self.che=che
        self.speed=speed
    def destroyer(self):
        print("Информация--------")
        super().infoo()
        print(f"скорость {self}")
        print(f'{self.che} человек на борту ')
    
class Cruiser(Ship):
    def __init__(self,name,width,height,army,chell):
        super().__init__(name,width,height)
        self.army=army
        self.chel=chell
    def cruiser(self):
        print('информация---------')
        super().infoo()
        print(f" Толщина брони {self.army}")
        print(f'{self.chell} человек на борту ')

    
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def display_amount(self):
        print(f'${self.dollars}.{self.cents:02}')

    def set_dollars(self, value):
        self.dollars = value

    def set_cents(self, value):
        self.cents = value