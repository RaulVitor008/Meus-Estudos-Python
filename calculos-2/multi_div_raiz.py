print('agora vamos usar mais um pouco a matematica?','vamos novamente digitar oque pede')
n3 = float(input('digite mais um numero: '))
n4 = float(input('digite outro numero: '))
multi= n3 * n4
subt=n3 - n4
print(f'Multiplicação,{multi}, a subtração,{subt},')
if n4 != 0:
    div = n3 / n4
    print(f'a divisão {div}')
else:
    print('Tente novamente um numero não pode ser dividido por 0')
n5=int(input('digite um numero acima de 10: '))
do=n5*2
tri=n5*3
qua=n5*4
ra=n5**0.5
print(f'raiz quadrada do numero é {ra:.2f}, dobro é {do}, triplo é {tri} e o quadri é {qua}')
