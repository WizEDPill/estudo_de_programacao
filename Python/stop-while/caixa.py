custo=0
totmil=0
menor=0
cont=0
barato=0 
while True: 
    name=str(input('informe o nome do produto:'))
    preco=int(input('informe o preço do produto R$'))
    lupin= str(input('voce vai continuar [S/N]'))
    cont+=1
    custo+=preco
    if preco >= 1000:
        totmil+=1
    if lupin.lower()=='n':
        break 
    if cont ==1:
        menor = preco
    else:
        if preco < menor:
            menor = preco 
            barato= name
print('--------------Fim do Programa--------------')   
print(f'o total de gasto é R${custo:.2f}')
print(f'a quantidade de produtos que custam mais de 1000 reais é {totmil}')
print(f'o produto mais barato é : {barato}')

     