
contm=0 
contf=0
conti=0
while True:
    idade=+1
    idade=int(input('informe sua idade:'))
    sexo=str(input('informe seu sexo em [M/F]:'))
    if sexo.lower() =='m':
        contm+=1 
    if idade < 20 and sexo.lower()== 'f':
        contf+=1 
# .lower() vai conferir a palavra e transformar para minuscula 
# frase.capitalize() transforma tudo para minusculo, mas so a primeira letra em maiusculo
    if idade > 18:
        conti+=1
    finalise=str(input('informe se voce quer continuar [S/N]:'))
    if finalise.lower() == 'n':
        break

print(f'o numero de pessoas que tem mais de 18 anos é {conti}')   
print(f'A quantidade de homens cadastrados é {contm}')
print(f'A quantidade de mulhes que tem menos de 20 anos é {contf}')