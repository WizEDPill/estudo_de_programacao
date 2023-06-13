import random
escolha= str(input('informe qual você quer pedra, papel ou tesoura?'))
n1= 'pedra'
n2= 'papel'
n3= 'tesoura'

lista = [n1, n2,n3]
escolhido= random.choice(lista)
#para escolher um item na escolhido 
if escolha == n1: 
    if escolhido ==n2: 
        print(f'Voce perdeu, pois a maquina escolheu {escolhido} que protege de {escolha}')
    if escolhido == n3:
        print(f'voce ganhou pois {n1} ganha de {escolhido}')
    if escolhido == escolha:
        print(f'impatou pois voce escolheu {escolha} e a maquina tambem escolheu{escolhido}')
elif escolha == n2:
    if escolhido == n2: 
        print(f'voces impataram, pois a {escolhido} é igual a {escolha}')
    if escolhido == n3: 
        print(f'voce perdeu, pois {escolhido} corta {escolha}')
    if escolhido == n1: 
        print(f'voce ganhor, pois {escolha} ganha de {escolhido}')
elif escolha == n3: 
    if escolhido == n2: 
        print(f'voce ganhou pois a maquina escolheu {escolhido} e voce {escolha}')
    if escolhido == n3: 
        print(f'voces escolheram o mesmo {escolha}')
    if escolhido == n1:
        print(f'voce perdeu, pois {escolhido} quebra{escolha} ')