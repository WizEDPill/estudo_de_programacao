ano = int(input('Informe o ano atual: '))
anonas= int(input('informe o ano de nascimento'))
idade= ano-anonas
if idade == 18:
     print('você está em idade de se alistarr')
    
elif idade < 18:
    print('ainda não é hora de se alistar')
elif idade > 18: 
    print('Já passou da hora de se alistar')
