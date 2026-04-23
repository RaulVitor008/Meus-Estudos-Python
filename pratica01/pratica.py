#exercicio de caixa eletronico
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

num=int(input('digite um numero?'))
if (num %2 == 0):
    print('esse numero é par')
else:
    print('esse numero é impar')

palavra = input('diga uma palavra')
contador = 0
for letra in palavra:
    if letra in 'aeiou':
        contador = contador +1
print(f'vogais:{contador}')