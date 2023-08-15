
lanche='hamburguer','suco','pizza','Pudim'
print(lanche[:-2])# vai mostrar o os anteriores da pizza
#lanche[1]='refrigerante' > tuple' object does not support item assignment as tuplas são imultáveis
print(lanche[-2:])# vai mostrar os posteriores junto da pizza
'''for comida in lanche:
    print(comida) # primeiro ele vai emprimir um depois o outro e assim por sequencia '''
# Outra forma é : 
for cont in range (0, len(lanche)): # ele vai fazer um por vez assim até completar a quant de elementos
    #print(cont) vai mostrar o numero de itens 
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
print('comi muito !')
for pos,comida in enumerate(lanche):# a difereça é que aqui não estou usando o range  e agora vou pedir o dado e a posição
    print(f'e vou comer {comida} na posição {pos}')
print(sorted(lanche))# vai colocar em ordem os itens da tupla
 