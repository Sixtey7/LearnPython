#Thing 1
print ('---Thing 1---')
class Thing():
    pass
example = Thing()
print ('Thing:', example)

#Thing 2
print('---Thing 2---')
class Thing2():
    letters = 'abc'

print ('Thing2:', Thing2.letters)

#Thing 3
print('---Thing 3---')
class Thing3():
    def __init__(self):
        self.letters = 'abc'

thing3 = Thing3()
print ('Thing3:', thing3.letters)

#Thing 4, Thing 6, Thing 7
print('---Thing 4, Thing 6, Thing 7---')
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return (str(self.number) + ': ' + self.name + ' (' + self.symbol + ')')

thing4 = Element('Hydrogen', 'H', 1)
print('Thing4:', thing4)

#Thing 5
print('---Thing 5---')
hydrogenDict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
thing5 = Element(**hydrogenDict)
print('Thing5:', thing5)

#Thing 8
print('---Thing 8---')
class NewElement():
    def __init__(self, input_name, input_symbol, input_number):
        self.__name = input_name
        self.__symbol = input_symbol
        self.__number = input_number
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, input_name):
        self.__name = input_name

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, input_symbol):
        self.__symbol = input_symbol

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, input_number):
        self.__number = input_number

thing8 = NewElement('Hydrogen', 'H', 1)
print ('Name:', thing8.name)
print ('Symbol:', thing8.symbol)
print ('Number:', thing8.number)

#Thing 9
print('---Thing 9---')
class Bear:
    @staticmethod
    def eats():
        return 'berries'

class Rabbit:
    @staticmethod
    def eats():
        return 'clover'

class Octothorpe:
    @staticmethod
    def eats():
        return 'campers'

thing9Bear = Bear()
thing9Rabbit = Rabbit()
thing9Octothorpe = Octothorpe()

print('Bear:', thing9Bear.eats())
print('Rabbit:', thing9Rabbit.eats())
print('Octothorpe:', thing9Octothorpe.eats())

#Thing 10
print('---Thing 10---')
class Laser:
    @staticmethod
    def does():
        return 'disintegrate'

class Claw:
    @staticmethod
    def does():
        return 'crush'

class SmartPhone:
    @staticmethod
    def does():
        return 'ring'

class Robot:
    def __init__(self, input_laser, input_claw, input_smartphone):
        self.laser = input_laser
        self.claw = input_claw
        self.smartphone = input_smartphone

    def does(self):
        print('Robot Does:',self.laser.does(), self.claw.does(), self.smartphone.does())

thing10Laser = Laser()
thing10Claw = Claw()
thing10SmartPhone = SmartPhone

thing10Robot = Robot(thing10Laser, thing10Claw, thing10SmartPhone)

thing10Robot.does()