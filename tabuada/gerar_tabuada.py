print('viu como é facil,sqn kkkk e agora vamos aprender a tabuada?')
def gerar_tabuada():
    try:
        num = int(input('escolha um numero da tabuada: '))
        for i in range(1,11):
            resultado = num * i
            print(f'{num}*{i}={resultado}')
    except ValueError:
        print('por favor digite apenas um numero')

gerar_tabuada()
