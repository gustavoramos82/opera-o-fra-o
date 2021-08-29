a1 = float(input('Digite o numerador da primeira fração'))
d1 = float(input('Digite o denominador da primeira fração'))
a2 = float(input('Digite o numerador da segunda fração'))
d2 = float(input('Digite o denominador da primeira fração'))

ope = int(input('Digite 0 para soma, 1 para subtração, 2 para multiplicação e 3 para divisão'))

if ope == 0:
    if d1 != d2:
        print('O resultado é {}/{}'.format(n1*d2+n2*d1,d2*d1))
    else:
        print('O resultado é {}/{}'.format(a1+a2,d1))

if ope == 1:
    if d1 != d2:
        print("O resultado é {}/{}".format(n1*d2-n2*d1,d1*d2))
    else:
        print('O resultado é {}/{}'.format(a1-a2,d1))

if ope == 2:
    print('O resultado é {}/{}'.format(a1*a2,d1*d2))

if ope == 3:
    print('O resultado é {}/{}'. format(a1*d2,a2*d1))
