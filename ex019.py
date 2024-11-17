import random
print('O professor irá sortear um aluno')
n1 = str(input('nome do aluno 1: '))
n2 = str(input('nome do aluno 2: '))
n3 = str(input('nome do aluno 3: '))
n4 = str(input('nome do aluno 4: '))
lista=[n1, n2, n3, n4]
print('O aluno sorteado para apresentar é:')
print(random.choice(lista))

