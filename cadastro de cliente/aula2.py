nome=input('qual é o seu nome? ')
idade=int(input('qual a sua idade? '))
print(nome)
print(idade)

if idade > 18:
   print('pode entrar')
else:
    print('não pode entrar')
    
with open('base_dados.csv','a')as arquivo:
    arquivo.write(f'seja bem-vindos {nome}. \n')