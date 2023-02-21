#Alex Karu
class Calc:
    # Funktsioon liidab x- i ja y- i
    def add(x, y):
        return x + y
    #funktsioon lahutab y- i x- ist
    def subtract(x, y):
        return x - y
    #funktsioon korrrutab x- i y- iga
    def multiply(x, y):
        return x * y
    #funktsioon jagab x- i y-iga
    def divide(x, y):
        return x / y
    def power(x, y):
        vastus = 1
        for i in range(y):
            vastus *= x
        return vastus

num1 = int(input('Mis on esimene number: ')) #Küsib kasutajalt esimest arvu
num2 = int(input('Mis on teine number: ')) #Küsib kasutajalt teist arvu
valik = int(input('1- liitmine, 2- lahutamine, 3-korrutamine, 4- jagamine, 5- astendamine: ')) #Küsib kasutajalt mida nad sooovivad teha
#Liidab
if valik == 1:
    print(Calc.add(num1, num2))
#lahutab
if valik == 2:
    print(Calc.subtract(num1, num2))
#korrutab
if valik == 3:
    print(Calc.multiply(num1, num2))
#jagab
if valik == 4:
    print(Calc.divide(num1, num2))
#Astendab
if valik == 5:
    print(Calc.power(num1, num2))


