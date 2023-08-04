cont=valor=som=0
while True:
    valor=int(input('informe o primeiro valor: (digite 1000 para parar)'))
    if valor==1000:
        break
    # o local onde é inserido o break afeta diretamente o funcionamento do programa. 
    som+=valor
    cont+=1 
   

print(f'a soma dos {cont} valores foi {som} ! ')
        
 
