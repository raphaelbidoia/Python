frase = str(input('digite uma frase: '))
n2 = frase.lower().strip()
n1 = n2.count('a')
print(f'Hà {n1} a´s em sua frase')
n3 = n2.find('a')+1
print(f'o primeiro a em sua frase esta localizado na posição: {n3}')
n4 = n2.rfind('a')+1
print(f'O ultimo a de sua frase aparece na posição: {n4}')
