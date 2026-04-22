# exercicio de caixa eletronico
saldo=float(input('qual o saldo em conta? '))
saque=float(input('qual o valor do saque? '))
if saque <= 0:
    print('sem dinheiro')
    exit()
sobrou = saldo - saque
if saque <= saldo:
    print(f'Aguarde... contagem... saldo agora é de:{sobrou}')
else:
    print('saldo insufiente')