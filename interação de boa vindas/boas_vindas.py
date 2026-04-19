nome=input('qual é o seu nome? ')
print('Ola',nome,'tudo bem com voce? qual a sua idade? ')
idade = input('minha idade é: ')
print('bom',nome,'bora começar o curso ja que voce tem',idade, 'anos?')
r = input('S/N? ').lower()
if(r == 'sim' or r == 's'):
    print('vamos la entao')
else:
    print('vai começar mesmo assim! hahahaha')
msg = 'O começo é sempre o mais importante, então vai se preparando. Bora dominar o básico para depois destruir no avançado!'
print(msg)
