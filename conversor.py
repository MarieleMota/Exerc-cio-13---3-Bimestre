def conversor():
  valor_cm = float(input('Digite um valor em CENTÍMETROS: '))

  valor_pol = valor_cm / 2.54

  msg = open('Texto.txt', 'w+')
  msg.write('\nO valor {} em centímetros, corresponde a {:.2f} em polegadas' .format(valor_cm, valor_pol))

  msg.seek(0.0)
  print(msg.read())

conversor()
print('Teste na aula do dia 06/10')