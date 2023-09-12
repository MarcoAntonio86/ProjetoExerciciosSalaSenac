while True:
  produto = input('Informe o produto: ')
  quantidade = int(input('Informe a quantidade: '))
  valor = float(input('Informe o valor: '))
  total = quantidade * valor
  print(f'O valor a ser pago, do produto {produto} é de R$ {total:.2f}')
  continuar = input('Deseja continuar? [S/N] ').strip().upper()
  if continuar == 'N':
    break


    
    
    
 
    
