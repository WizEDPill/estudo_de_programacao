valor=float(input('Informe o valor da casa: '))
salario=float(input('Informe o seu salario: '))
anos=int(input('Em quantos anos deseja pagar ?'))
#o mensal tem que ser 30% do salario  senão será negado
meses= anos * 12 
total= valor/meses 
salariop= salario*0.3 
if total> salariop:
    print('Seu emprestimo não foi aprovado pois excedeu 30 por cento do valor do salario')
elif total <= salariop: 
    print('Parabéns seu financiamento foi aprovado !')
    print(f'seu pagamento mensal será{total}')
    
