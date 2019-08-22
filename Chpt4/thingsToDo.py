# Thing 1
print('---Thing 1---')
guess_me = 7

def tryToGuessMe(guess):
    if (guess < guess_me):
        return "Too Low"
    elif (guess > guess_me) :
        return "Too High"
    else:
        return "Just Right"

print ("Value for 10:", tryToGuessMe(10))
print ("Value for 5:", tryToGuessMe(5))
print ("Value for 7:", tryToGuessMe(7))

#Thing 2
print('---Thing 2---')
guess_me = 7
start = 1
while (True):
    if (start < guess_me):
        print("Too Low")
    elif (start > guess_me):
        print("oops")
    else:
        print("Found it!")
        break
    start+=1

#Thing 3
print('---Thing 3---')
thing3List = [3, 2, 1, 0]
for thing3 in thing3List:
    print(thing3)

#Thing 4
print("---Thing 4---")
evenList = [number for number in range(10) if number % 2 == 0]
print("Even numbers:", evenList)

#Thing 5
print('---Thing 5---')
squareDict = {number: number*number for number in range(10)}
print("Square Dict:", squareDict)

#Thing 6
print('---Thing 6---')
oddSet = { number for number in range(10) if number % 2 == 1}
print("Odd Set:", oddSet)

#Thing 7
print("---Thing 7---")
def thing7Gen(range=range(10)):
    for num in range:
        yield ("Got %s" % num)

for line in thing7Gen():
    print(line)

#Thing 8
print('---Thing 8---')
def good():
    return ['Harry', 'Ron', 'Hermione']

print("Return from good:", good())

#Thing 9
print('---Thing 9---')
def get_odds(range=range(10)):
    for num in range:
        if (num % 2 == 1):
            yield num


count = 0
for oddResult in get_odds():
    if (count == 2):
        print('Third value from get_odds:', oddResult)
        break
    count+=1

#Thing 10
print('---Thing 10---')
def startEndPrinter(func):
    def new_function(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")

    return new_function

@startEndPrinter
def simpleFunc():
    print("Doing stuff")

simpleFunc()

#Thing 11
print("---Thing 11---")
class OopsException(Exception):
    pass

try:
    raise OopsException("Hello World")
except OopsException as opExc:
    print("Caught an oops")

#Thing 12
print('---Thing 12---')
title = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

titlePlotDict = dict(zip(title, plots))

print("Dict of titles and plots:", titlePlotDict)