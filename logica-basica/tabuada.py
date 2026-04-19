def gerar_tabuada():
    try:
        num = int(input('escolha um numero da tabuada: '))
        print(f'\ntabuada do {num}')
        for i in range(1, 11):
            print(f'{num} * {i} = {num * i}')
    except ValueError:
        print('por favor digite apenas um numero')
