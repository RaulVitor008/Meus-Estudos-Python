nome=input('qual é o seu nome? ')
print('Ola',nome,'tudo bem com voce? qual a sua idade? ')
idade = input('minha idade é: ')
print('bom',nome,'bora começar o curso ja que voce tem',idade, 'anos?')
r = input('S/N? ').lower()
if(r == 'sim' or r == 's'):
    print('vamos la entao')
else:
    print('vai começar mesmo assim! hahahaha')
msg = 'Seja bem-vindo ao curso, entao vamos começar com o basico'
print(msg)
