number=int(input('informe um valor de 1 até 20 '))
numero=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
if number > 20: 
    number=int(input('Por favor insira um valor valido: '))
else: 
    print(f'você selecionou o numero {numero[number]}')