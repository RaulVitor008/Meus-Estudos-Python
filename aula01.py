# nome=input('qual é o seu nome? ')
# print('Ola',nome,'tudo bem com voce? qual a sua idade? ')
# idade = input('minha idade é: ')
# print('bom',nome,'bora começar o curso ja que voce tem',idade, 'anos?')
# r = input('S/N? ').lower()
# if(r == 'sim' or r == 's'):
#     print('vamos la entao')
# else:
#     print('vai começar mesmo assim! hahahaha')

# msg = 'O começo é sempre o mais importante, então vai se preparando. Bora dominar o básico para depois destruir no avançado!'
# print(msg)

# n1=float(input('digite um numero? '))
# n2=float(input('digite um outro numero? '))
# print(f'o resultado de,{n1},e,{n2},é igual a: {n1+n2}')
# msg1=input('correto? Sim/Não: ').lower()
# if(msg1 == 'sim' or msg1 == 's'):
#     print("isso ai, estamos indo bem!")
# else:
#     print('não tem certeza?')
# print('agora vamos usar mais um pouco a matematica?','vamos novamente digitar oque pede')

# n3 = float(input('digite mais um numero: '))
# n4 = float(input('digite outro numero: '))
# multi= n3 * n4
# subt=n3 - n4
# print(f'Multiplicação,{multi}, a subtração,{subt},')
# if  n4 != 0:
#     div = n3 / n4
#     print(f'a divisão {div}')
# else:
#    print('Tente novamente um numero não pode ser dividido por 0')

# n5=int(input('digite um numero acima de 10: '))
# do=n5*2
# tri=n5*3
# qua=n5*4
# ra=n5**0.5
# print(f'raiz quadrada do numero é {ra:.2f}, dobro é {do}, triplo é {tri} e o quadri é {qua}')
# print('viu como é facil, sqn kkkk e agora vamos aprender a tabuada?')

# def gerar_tabuada():
#     try:
#         num = int(input('escolha um numero da tabuada: '))
#         print(f'\ntabuada do {num}')
#         for i in range(1, 11):
#             print(f'{num} * {i} = {num * i}')
#     except ValueError:
#         print('por favor digite apenas um numero')

# idad=input('qual sua idade?: ').lower()
# possui_documento=input('voce tem documento?(sim/nao): ').lower()
# if idade >= 18 and possui_documento == 'sim':
#     print('pode entrar')
# else: 
#     print('não pode, apenas com o documento')

# A = int(input('informe os dias para ativade A:'))
# B = int(input('informe os dias para ativade b:'))
# C = int(input('informe os dias para ativade c:'))

# if (A >= 0 and B >= 0 and C >= 0):
#     tempo_total = A + B + C
#     print(f"O tempo total do projeto é de {tempo_total} dias.")
# else:
#     print("Erro: Os dias não podem ser negativos.")

# orçamento =float(input('qual foi o valor da compra?'))
# if(orçamento <=5897.58):
#     print('ultrapassou o limite de 5000')
# else:
#     print('não ultrapassou o limite de 5000')

# horario = 21
# if (horario <=18):
#     print('pode entrar')
# else:
#     print('passou das 18h, tente amanha')

# distancia = int(input('digite a distancia percorrida em km'))

# if (distancia <=100):
#     print('pagará 10 reais')
# elif 100 < distancia <= 200:
#     print("Valor do pedágio: R$ 20,00")
# else: 
#     print('pagará 30 reais')

# renda = int(input('qual a sua renda?'))
# parcela =int(input('qual numero de parcelas?'))
# if renda > 2000 and parcela<=0.3* renda:
#     print('aprovado')
# elif renda