'''import random
n1 = str(input('nome do aluno 1: '))
n2 = str(input('nome do aluno 2: '))
n3 = str(input('nome do aluno 3: '))
n4 = str(input('nome do aluno 4: '))
lista=[n1, n2, n3, n4]
print('A ordem de apresentação é :')
print(random.sample(lista, 4))'''
import random
n1 = str(input('nome do aluno 1: '))
n2 = str(input('nome do aluno 2: '))
n3 = str(input('nome do aluno 3: '))
n4 = str(input('nome do aluno 4: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
