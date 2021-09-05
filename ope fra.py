from fractions import Fraction
from termcolor import colored

#colocando os números correspondente ao numerador e ao denominador.

a1 = Fraction(input('Digite o numerador da primeira fração:'))
d1 = Fraction(input('Digite o denominador da primeira fração:'))
a2 = Fraction(input('Digite o numerador da segunda fração:'))
d2 = Fraction(input('Digite o denominador da primeira fração:'))

#caso os denominadores forem diferentes de zero.

if d1 == 0 or d2 == 0:
    print(colored('O denominador de uma fração tem que ser diferente de zero, por favor tente novamente e mude o valor do denominador.','red'))

ope = int(input("insira 0 para adição, 1 para subtração, 2 para multiplicação e 3 para divisão:"))

if ope > 3 or  ope < 0:
    print(colored('Só aceitamos como valor de 0 a 3 representando as respectivas operações, por favor, tente novamente.', 'red'))

# definindo as varáveis pra ficar mais fácil.

adi = a1*d2+a2*d1
dif = a1*d2-a2*d1
prode = d1*d2
mutn = a1*a2
proddn = a1*d2
prodnu = a2*d1

#Operação da adição

if ope == 0:
    if d1 != d2:
        print('O resultado é {}/{}'.format(adi,prode))
        print('A sua forma irredutivel é:')
        print(colored(Fraction(adi,prode),'green'))
    else:
        print('O resultado é {}/{}'.format(a1+a2,d1))
        print('Sua forma irredutivel é:')
        print(colored(Fraction(a1+a2,d1),'green'))

#Operação da subtração

if ope == 1:
    if d1 != d2:
        print('O resultado é {}/{}'.format(dif,prode))
        print('A sua forma irredutível é')
        print(colored(Fraction(dif,prode),'green'))
    else:
        print('O resultado é {}/{}'.format(a1-a2,d1))
        print('A sua forma irredutivel é:')
        print(colored(Fraction(a1-a2,d1),'green'))

#Operação da multiplicação

if ope == 2:
    print('O resultado é {}/{}'.format(mutn,prode))
    print('Sua forma irredutivel é:')
    print(colored(Fraction(mutn,prode)))

#Operação da divisão

if ope == 3:
    print('O resultado será {}/{}'.format(proddn,prodnu))
    print('Sua forma irredutivel é:')
    print(colored(Fraction(proddn,prodnu),'green'))




