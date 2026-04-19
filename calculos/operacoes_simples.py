n1=float(input('digite um numero? '))
n2=float(input('digite um outro numero? '))
print(f'o resultado de,{n1},e,{n2},é igual a: {n1+n2}')
msg1=input('correto? Sim/Não: ').lower()
if(msg1 == 'sim' or msg1 == 's'):
    print("isso ai, estamos indo bem!")
else:
    print('não tem certeza?')
