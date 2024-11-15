print('escreva um nemero em metros para saber seu valor em')
n = float(input('digite aqui:'))
print('O valor que você digitou foi de {} m'
      '\nseu valor em kilometros é:{}km'
      '\nseu valor em hectometro é: {}hm '
      '\nseu valor em decametros é: {}dam'
      '\nseu valor em decimetros é: {} cm'
      '\nseu valor em centimetros é: {} dm'
      '\nseu valor em milimetros é: {} mm'
      .format(n, (n/1000), (n/100), (n/10), (n*10), (n*100), (n*1000)))
